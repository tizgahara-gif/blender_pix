import bpy

from .constants import ADDON_ID


class BAC_AddonPreferences(bpy.types.AddonPreferences):
    bl_idname = ADDON_ID

    root_dir: bpy.props.StringProperty(
        name="Workspace Root",
        subtype="DIR_PATH",
        description="Root directory to store jobs, sources, and exports",
        default="",
    )
    aseprite_executable: bpy.props.StringProperty(
        name="Aseprite Executable",
        subtype="FILE_PATH",
        description="Optional path to Aseprite executable",
        default="",
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "root_dir")
        layout.prop(self, "aseprite_executable")
