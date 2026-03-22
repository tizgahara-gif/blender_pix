from pathlib import Path

import bpy


def reload_image_from_export(image: bpy.types.Image, exported_path: Path) -> None:
    if not exported_path.exists():
        raise FileNotFoundError(f"Exported image missing: {exported_path}")
    image.filepath = str(exported_path)
    image.reload()
