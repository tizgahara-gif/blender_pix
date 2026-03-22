import bpy

from ..enums import MAP_TYPES


class BAC_AddonProps(bpy.types.PropertyGroup):
    map_type: bpy.props.EnumProperty(name="Map Type", items=MAP_TYPES, default="ALBEDO")
    include_uv_guide: bpy.props.BoolProperty(name="Export UV Guide", default=True)
    uv_guide_size: bpy.props.IntProperty(name="Guide Size", default=1024, min=64, max=8192)
