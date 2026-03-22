import bpy


class BAC_SceneProps(bpy.types.PropertyGroup):
    last_job_path: bpy.props.StringProperty(name="Last Job", default="")
    last_export_path: bpy.props.StringProperty(name="Last Export", default="")
    last_revision: bpy.props.IntProperty(name="Last Revision", default=0, min=0)
