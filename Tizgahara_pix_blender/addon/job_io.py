from pathlib import Path

from .asset_resolver import ResolvedAsset
from .revision import revision_tag
from .utils.json_utils import write_json
from .utils.time_utils import now_iso


def build_job_payload(*, asset: ResolvedAsset, map_type: str, source_path: Path, export_path: Path, guide_paths: list[Path], revision: int):
    return {
        "schema": "blender-aseprite-job.v1",
        "created_at": now_iso(),
        "revision": revision,
        "revision_tag": revision_tag(revision),
        "asset": {
            "object_name": asset.object_name,
            "material_name": asset.material_name,
            "image_name": asset.image.name,
            "image_path": str(asset.image_path),
        },
        "task": {
            "map_type": map_type,
            "source_path": str(source_path),
            "export_path": str(export_path),
            "guides": [str(p) for p in guide_paths],
        },
    }


def write_job(path: Path, payload: dict):
    write_json(path, payload)
