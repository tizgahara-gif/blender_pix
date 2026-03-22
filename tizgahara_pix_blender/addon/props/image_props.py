import bpy


class BAC_ImageProps(bpy.types.PropertyGroup):
    linked_revision: bpy.props.IntProperty(name="Linked Revision", default=0, min=0)
    linked_export_path: bpy.props.StringProperty(name="Linked Export Path", default="")
    last_seen_event_id: bpy.props.StringProperty(name="Last Seen Event ID", default="")
    last_reload_at: bpy.props.StringProperty(name="Last Reload At", default="")
    sync_status: bpy.props.StringProperty(name="Sync Status", default="idle")
