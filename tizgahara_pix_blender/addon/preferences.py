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
    auto_sync_enabled: bpy.props.BoolProperty(
        name="Auto Sync Enabled",
        description="Auto reload watched export PNG changes",
        default=True,
    )
    sync_poll_interval: bpy.props.FloatProperty(
        name="Sync Poll Interval",
        description="Polling interval (seconds) for export file watcher",
        default=0.5,
        min=0.1,
        max=10.0,
    )
    reload_settle_delay: bpy.props.FloatProperty(
        name="Reload Settle Delay",
        description="Delay (seconds) before reloading changed file to avoid mid-write reload",
        default=0.35,
        min=0.0,
        max=5.0,
    )
    debug_sync_logging: bpy.props.BoolProperty(
        name="Debug Sync Logging",
        description="Print watcher debug logs to console",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "root_dir")
        layout.prop(self, "aseprite_executable")

        box = layout.box()
        box.label(text="Auto Sync")
        box.prop(self, "auto_sync_enabled")
        box.prop(self, "sync_poll_interval")
        box.prop(self, "reload_settle_delay")
        box.prop(self, "debug_sync_logging")
