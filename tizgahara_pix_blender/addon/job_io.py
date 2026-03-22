from pathlib import Path

from .asset_resolver import ResolvedAsset
from .revision import revision_tag
from .utils.json_utils import write_json
from .utils.time_utils import now_iso


def _color_mode_from_image(asset: ResolvedAsset) -> str:
    channels = int(getattr(asset.image, "channels", 4) or 4)
    return "rgba" if channels >= 4 else "rgb"


def _guides_payload(guide_paths: list[Path]) -> dict:
    uv_guide_path = str(guide_paths[0]) if guide_paths else ""
    extra_paths = [str(p) for p in guide_paths[1:]] if len(guide_paths) > 1 else []
    return {
        "uv_guide_path": uv_guide_path,
        "id_map_path": "",
        "palette_path": "",
        "mask_paths": [],
        "extra_paths": extra_paths,
    }


def build_job_payload(*, asset: ResolvedAsset, map_type: str, source_path: Path, export_path: Path, guide_paths: list[Path], revision: int):
    created_at = now_iso()
    rev_tag = revision_tag(revision)
    width = int(asset.image.size[0])
    height = int(asset.image.size[1])
    color_mode = _color_mode_from_image(asset)

    asset_obj = {
        "object_name": asset.object_name,
        "material_name": asset.material_name,
        "image_name": asset.image.name,
        "image_path": str(asset.image_path),
    }

    # Backward-compatible top-level task format (guides list kept).
    task_legacy = {
        "map_type": map_type,
        "source_path": str(source_path),
        "export_path": str(export_path),
        "guides": [str(p) for p in guide_paths],
        "width": width,
        "height": height,
        "color_mode": color_mode,
    }

    # Preferred nested data.task format for Aseprite parser.
    task_data = {
        "map_type": map_type,
        "source_path": str(source_path),
        "export_path": str(export_path),
        "guides": _guides_payload(guide_paths),
        "width": width,
        "height": height,
        "color_mode": color_mode,
    }

    return {
        "schema": "blender-aseprite-job.v1",
        "created_at": created_at,
        "revision": revision,
        "revision_tag": rev_tag,
        "asset": asset_obj,
        "task": task_legacy,
        "data": {
            "schema": "blender-aseprite-job.v1",
            "created_at": created_at,
            "revision": revision,
            "revision_tag": rev_tag,
            "asset": asset_obj,
            "task": task_data,
        },
    }


def write_job(path: Path, payload: dict):
    write_json(path, payload)
