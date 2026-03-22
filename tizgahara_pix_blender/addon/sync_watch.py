from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import time

import bpy
from bpy.app.handlers import persistent

from .config import get_prefs
from .image_reload import reload_image_from_export


@dataclass
class WatchTarget:
    image_name: str
    export_path: Path
    last_mtime: float | None = None
    last_size: int | None = None
    pending_until: float | None = None


WATCH_REGISTRY: dict[str, WatchTarget] = {}
_TIMER_RUNNING = False


def _log_debug(message: str) -> None:
    prefs = get_prefs(bpy.context)
    if prefs and prefs.debug_sync_logging:
        print(f"[tizgahara_pix_blender.sync] {message}")


def register_watch_for_image(image: bpy.types.Image, export_path: Path) -> None:
    if not export_path:
        return
    WATCH_REGISTRY[image.name] = WatchTarget(image_name=image.name, export_path=Path(export_path))
    _log_debug(f"watch registered: image={image.name} path={export_path}")


def remove_watch_for_image_name(image_name: str) -> None:
    WATCH_REGISTRY.pop(image_name, None)


def restore_registry_from_images() -> None:
    WATCH_REGISTRY.clear()
    for image in bpy.data.images:
        props = getattr(image, "bac_image", None)
        if not props:
            continue
        if props.linked_export_path:
            register_watch_for_image(image, Path(props.linked_export_path))
    _log_debug(f"registry restored: {len(WATCH_REGISTRY)} targets")


def _current_poll_interval() -> float:
    prefs = get_prefs(bpy.context)
    if prefs:
        return max(0.1, float(prefs.sync_poll_interval))
    return 0.5


def watch_tick() -> float:
    prefs = get_prefs(bpy.context)
    if not prefs or not prefs.auto_sync_enabled:
        return _current_poll_interval()

    now = time.monotonic()
    settle_delay = max(0.0, float(prefs.reload_settle_delay))

    for image_name, target in list(WATCH_REGISTRY.items()):
        image = bpy.data.images.get(image_name)
        if not image:
            _log_debug(f"image removed from blend, unregistering watch: {image_name}")
            remove_watch_for_image_name(image_name)
            continue

        try:
            if not target.export_path.exists():
                target.pending_until = None
                continue

            stat = target.export_path.stat()
            mtime = float(stat.st_mtime)
            size = int(stat.st_size)

            if target.last_mtime is None or target.last_size is None:
                target.last_mtime = mtime
                target.last_size = size
                continue

            changed = (mtime != target.last_mtime) or (size != target.last_size)
            if changed:
                target.last_mtime = mtime
                target.last_size = size
                target.pending_until = now + settle_delay
                _log_debug(f"change detected: {target.export_path} pending_until={target.pending_until:.3f}")
                continue

            if target.pending_until and now >= target.pending_until:
                reload_image_from_export(image, target.export_path)
                target.pending_until = None
                _log_debug(f"reloaded image={image_name} from {target.export_path}")
        except Exception as exc:
            # Fail safe per target: keep timer running for other targets.
            target.pending_until = None
            print(f"[tizgahara_pix_blender.sync] failed target={image_name}: {exc}")

    return _current_poll_interval()


def ensure_timer_registered() -> None:
    global _TIMER_RUNNING
    if not _TIMER_RUNNING:
        bpy.app.timers.register(watch_tick, first_interval=_current_poll_interval(), persistent=True)
        _TIMER_RUNNING = True
        _log_debug("timer registered")


def stop_timer() -> None:
    global _TIMER_RUNNING
    if _TIMER_RUNNING and bpy.app.timers.is_registered(watch_tick):
        bpy.app.timers.unregister(watch_tick)
    _TIMER_RUNNING = False


def sync_status_summary() -> str:
    pending = sum(1 for t in WATCH_REGISTRY.values() if t.pending_until is not None)
    timer_state = "ON" if _TIMER_RUNNING else "OFF"
    return f"Timer:{timer_state} Watched:{len(WATCH_REGISTRY)} Pending:{pending}"


@persistent
def on_load_post(_dummy):
    restore_registry_from_images()
    ensure_timer_registered()
