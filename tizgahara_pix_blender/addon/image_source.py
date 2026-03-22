from pathlib import Path
import shutil

import bpy

from .asset_resolver import ResolvedAsset


PACKED_IMAGE_ERROR = "Packed image is unsupported. Please unpack or save externally."


def ensure_image_file_for_job(*, asset: ResolvedAsset, source_path: Path, scene: bpy.types.Scene) -> Path:
    """Ensure a real PNG file exists for Aseprite input and return its path."""
    source_path.parent.mkdir(parents=True, exist_ok=True)

    if asset.is_packed:
        raise ValueError(PACKED_IMAGE_ERROR)

    # External image file path case: keep existing behavior (copy to revisioned source).
    if asset.image_path:
        if not asset.image_path.exists():
            raise FileNotFoundError(f"Image file does not exist: {asset.image_path}")
        shutil.copy2(asset.image_path, source_path)
        return source_path

    # Generated image (no filepath): render/save image datablock to PNG source file.
    try:
        asset.image.save_render(filepath=str(source_path), scene=scene)
    except Exception as exc:
        raise RuntimeError(f"Failed to save generated image to PNG: {source_path}") from exc

    if not source_path.exists() or source_path.stat().st_size == 0:
        raise RuntimeError(f"Generated image export produced no file: {source_path}")

    return source_path
