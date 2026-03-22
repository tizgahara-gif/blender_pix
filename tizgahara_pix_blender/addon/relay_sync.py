from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import json
import time

import bpy
from bpy.app.handlers import persistent

from .config import get_prefs
from .image_reload import reload_image_from_export


@dataclass
class PendingReload:
    image_name: str
    export_path: Path
    due_at: float


EXPORT_TO_IMAGES: dict[str, set[str]] = {}
PENDING_RELOADS: list[PendingReload] = []
_LAST_OFFSET = 0
_TIMER_RUNNING = False


def _norm(path: Path | str) -> str:
    return str(Path(path).expanduser().resolve())


def _log_debug(message: str) -> None:
    prefs = get_prefs(bpy.context)
    if prefs and prefs.debug_sync_logging:
        print(f"[tizgahara_pix_blender.relay] {message}")


def register_export_target(image: bpy.types.Image, export_path: Path | str) -> None:
    key = _norm(export_path)
    names = EXPORT_TO_IMAGES.setdefault(key, set())
    names.add(image.name)
    _log_debug(f"registry add: {key} -> {sorted(names)}")


def rebuild_registry_from_images() -> None:
    EXPORT_TO_IMAGES.clear()
    for image in bpy.data.images:
        props = getattr(image, "bac_image", None)
        if props and props.linked_export_path:
            register_export_target(image, props.linked_export_path)


def _enqueue_reload(image_name: str, export_path: Path, settle_delay: float) -> None:
    due_at = time.monotonic() + settle_delay
    for item in PENDING_RELOADS:
        if item.image_name == image_name and item.export_path == export_path:
            item.due_at = due_at
            return
    PENDING_RELOADS.append(PendingReload(image_name=image_name, export_path=export_path, due_at=due_at))


def queue_reload_for_export(export_path: str, settle_delay: float) -> int:
    key = _norm(export_path)
    images = EXPORT_TO_IMAGES.get(key, set())
    if not images:
        _log_debug(f"no image bound for export path: {key}")
        return 0

    count = 0
    for image_name in images:
        _enqueue_reload(image_name, Path(key), settle_delay)
        count += 1
    _log_debug(f"queued reload for {count} image(s) from {key}")
    return count


def _poll_inbox_file(inbox_path: Path, settle_delay: float) -> None:
    global _LAST_OFFSET

    if not inbox_path.exists():
        return

    size = inbox_path.stat().st_size
    if size < _LAST_OFFSET:
        _LAST_OFFSET = 0

    with inbox_path.open("r", encoding="utf-8") as fh:
        fh.seek(_LAST_OFFSET)
        for raw_line in fh:
            line = raw_line.strip()
            if not line:
                continue
            try:
                payload = json.loads(line)
            except json.JSONDecodeError:
                _log_debug(f"invalid json line ignored: {line[:80]}")
                continue

            if payload.get("type") != "texture_exported":
                continue

            export_path = payload.get("export_path")
            if not export_path:
                _log_debug("texture_exported missing export_path")
                continue
            queue_reload_for_export(str(export_path), settle_delay)

        _LAST_OFFSET = fh.tell()


def consume_reload_queue() -> None:
    now = time.monotonic()
    next_queue: list[PendingReload] = []

    for item in PENDING_RELOADS:
        if now < item.due_at:
            next_queue.append(item)
            continue

        image = bpy.data.images.get(item.image_name)
        if not image:
            continue

        try:
            reload_image_from_export(image, item.export_path)
            _log_debug(f"reloaded {item.image_name} from {item.export_path}")
        except Exception as exc:
            print(f"[tizgahara_pix_blender.relay] reload failed image={item.image_name}: {exc}")

    PENDING_RELOADS.clear()
    PENDING_RELOADS.extend(next_queue)


def _current_poll_interval() -> float:
    prefs = get_prefs(bpy.context)
    if prefs:
        return max(0.1, float(prefs.relay_poll_interval))
    return 0.5


def relay_tick() -> float:
    prefs = get_prefs(bpy.context)
    if not prefs or not prefs.relay_enabled:
        return _current_poll_interval()

    try:
        inbox = Path(prefs.relay_inbox_path).expanduser() if prefs.relay_inbox_path else None
        if inbox:
            _poll_inbox_file(inbox, settle_delay=max(0.0, float(prefs.reload_settle_delay)))
        consume_reload_queue()
    except Exception as exc:
        print(f"[tizgahara_pix_blender.relay] tick failed: {exc}")

    return _current_poll_interval()


def relay_status_summary() -> str:
    timer_state = "ON" if _TIMER_RUNNING else "OFF"
    return f"Relay:{timer_state} Targets:{len(EXPORT_TO_IMAGES)} Queue:{len(PENDING_RELOADS)}"


def ensure_timer_registered() -> None:
    global _TIMER_RUNNING
    if not _TIMER_RUNNING:
        bpy.app.timers.register(relay_tick, first_interval=_current_poll_interval(), persistent=True)
        _TIMER_RUNNING = True


def stop_timer() -> None:
    global _TIMER_RUNNING
    if _TIMER_RUNNING and bpy.app.timers.is_registered(relay_tick):
        bpy.app.timers.unregister(relay_tick)
    _TIMER_RUNNING = False


@persistent
def on_load_post(_dummy):
    rebuild_registry_from_images()
    ensure_timer_registered()
