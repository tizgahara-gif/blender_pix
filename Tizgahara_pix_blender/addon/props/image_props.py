import bpy


class BAC_ImageProps(bpy.types.PropertyGroup):
    linked_revision: bpy.props.IntProperty(name="Linked Revision", default=0, min=0)
    linked_export_path: bpy.props.StringProperty(name="Linked Export Path", default="")
