from dataclasses import dataclass
from pathlib import Path

import bpy


@dataclass
class ResolvedAsset:
    image: bpy.types.Image
    image_path: Path | None
    object_name: str
    material_name: str
    is_generated: bool
    is_packed: bool


def resolve_active_asset(context: bpy.types.Context) -> ResolvedAsset:
    obj = context.view_layer.objects.active
    if not obj:
        raise ValueError("No active object.")
    if not obj.active_material:
        raise ValueError("Active object has no active material.")

    mat = obj.active_material
    if not mat.use_nodes or not mat.node_tree:
        raise ValueError("Material does not use nodes.")

    active_node = mat.node_tree.nodes.active
    image = None
    if active_node and active_node.type == "TEX_IMAGE" and active_node.image:
        image = active_node.image
    else:
        for node in mat.node_tree.nodes:
            if node.type == "TEX_IMAGE" and node.image:
                image = node.image
                break

    if not image:
        raise ValueError("No image texture node with image found.")

    has_filepath = bool(image.filepath)
    image_path = Path(bpy.path.abspath(image.filepath)).expanduser().resolve() if has_filepath else None

    return ResolvedAsset(
        image=image,
        image_path=image_path,
        object_name=obj.name,
        material_name=mat.name,
        is_generated=not has_filepath,
        is_packed=bool(image.packed_file),
    )
