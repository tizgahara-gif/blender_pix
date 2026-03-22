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

    # Relay-based auto sync settings.
    relay_enabled: bpy.props.BoolProperty(
        name="Relay Auto Sync Enabled",
        description="Enable localhost relay inbox polling for texture_exported events",
        default=True,
    )
    relay_poll_interval: bpy.props.FloatProperty(
        name="Relay Poll Interval",
        description="Polling interval (seconds) for relay inbox",
        default=0.5,
        min=0.1,
        max=10.0,
    )
    relay_inbox_path: bpy.props.StringProperty(
        name="Relay Inbox Path",
        subtype="FILE_PATH",
        description="Path to relay inbox JSONL file (texture_exported events)",
        default="",
    )
    reload_settle_delay: bpy.props.FloatProperty(
        name="Reload Settle Delay",
        description="Delay (seconds) before queued Image.reload() after notify",
        default=0.35,
        min=0.0,
        max=5.0,
    )
    debug_sync_logging: bpy.props.BoolProperty(
        name="Debug Sync Logging",
        description="Print relay sync debug logs to console",
        default=False,
    )

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "root_dir")
        layout.prop(self, "aseprite_executable")

        box = layout.box()
        box.label(text="Relay Auto Sync")
        box.prop(self, "relay_enabled")
        box.prop(self, "relay_poll_interval")
        box.prop(self, "relay_inbox_path")
        box.prop(self, "reload_settle_delay")
        box.prop(self, "debug_sync_logging")
