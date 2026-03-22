from pathlib import Path

import bpy


def get_prefs(context: bpy.types.Context):
    addon = context.preferences.addons.get("Tizgahara_pix_blender")
    if not addon:
        return None
    return addon.preferences


def as_path(raw_value: str) -> Path:
    return Path(bpy.path.abspath(raw_value)).expanduser().resolve()
