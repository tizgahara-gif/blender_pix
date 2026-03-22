from pathlib import Path

import bpy


def export_uv_layout(context: bpy.types.Context, filepath: Path, size: int = 1024, opacity: float = 0.25) -> Path:
    obj = context.view_layer.objects.active
    if not obj or obj.type != "MESH":
        raise ValueError("Active object must be a mesh.")

    prev_mode = obj.mode
    bpy.ops.object.mode_set(mode="EDIT")
    try:
        bpy.ops.uv.export_layout(filepath=str(filepath), size=(size, size), opacity=opacity)
    finally:
        bpy.ops.object.mode_set(mode=prev_mode)
    return filepath
