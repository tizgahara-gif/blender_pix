from pathlib import Path

import bpy

from .utils.json_utils import read_json, write_json


def _state_path(context: bpy.types.Context) -> Path:
    blend_dir = Path(bpy.path.abspath("//")) if bpy.data.filepath else Path.home()
    return (blend_dir / ".aseprite_companion_state.json").resolve()


def load_state(context: bpy.types.Context) -> dict:
    path = _state_path(context)
    if not path.exists():
        return {"recent_jobs": []}
    return read_json(path)


def save_state(context: bpy.types.Context, state: dict) -> None:
    write_json(_state_path(context), state)
