from pathlib import Path

import bpy

from .config import as_path, get_prefs
from .constants import DEFAULT_EXPORT_DIRNAME, DEFAULT_JOB_DIRNAME, DEFAULT_SOURCE_DIRNAME
from .utils.file_utils import ensure_dir


def root_from_context(context: bpy.types.Context) -> Path:
    prefs = get_prefs(context)
    if prefs and prefs.root_dir:
        return as_path(prefs.root_dir)
    if bpy.data.filepath:
        return Path(bpy.path.abspath("//")).resolve()
    return Path.home() / "blender_aseprite_companion"


def ensure_base_dirs(context: bpy.types.Context) -> dict[str, Path]:
    root = ensure_dir(root_from_context(context))
    job_dir = ensure_dir(root / DEFAULT_JOB_DIRNAME)
    source_dir = ensure_dir(root / DEFAULT_SOURCE_DIRNAME)
    export_dir = ensure_dir(root / DEFAULT_EXPORT_DIRNAME)
    return {"root": root, "job": job_dir, "source": source_dir, "export": export_dir}


def file_stem_safe(name: str) -> str:
    cleaned = "".join(ch if ch.isalnum() or ch in ("-", "_") else "_" for ch in name)
    return cleaned.strip("_") or "asset"
