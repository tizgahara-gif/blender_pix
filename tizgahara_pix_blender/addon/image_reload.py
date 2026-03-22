from pathlib import Path

import bpy

from .utils.time_utils import now_iso


def reload_image_from_export(image: bpy.types.Image, exported_path: Path, *, event_id: str = "") -> None:
    if not exported_path.exists():
        raise FileNotFoundError(f"Exported image missing: {exported_path}")
    image.filepath = str(exported_path)
    image.reload()

    props = getattr(image, "bac_image", None)
    if props:
        if event_id:
            props.last_seen_event_id = event_id
        props.last_reload_at = now_iso()
        props.sync_status = "reloaded"
