import bpy

from .constants import PANEL_CATEGORY


class BAC_PT_main_panel(bpy.types.Panel):
    bl_label = "Tizgahara Pix Blender"
    bl_idname = "BAC_PT_main_panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = PANEL_CATEGORY

    def draw(self, context):
        layout = self.layout
        settings = context.scene.bac_addon
        scene_props = context.scene.bac_scene

        col = layout.column(align=True)
        col.prop(settings, "map_type")
        col.prop(settings, "include_uv_guide")
        if settings.include_uv_guide:
            col.prop(settings, "uv_guide_size")

        col.separator()
        col.operator("bac.validate_asset", icon="CHECKMARK")
        col.operator("bac.generate_job", icon="FILE_TICK")
        col.operator("bac.export_uv_guide", icon="UV")
        col.operator("bac.launch_aseprite", icon="PLAY")
        col.operator("bac.reload_exported_image", icon="FILE_REFRESH")

        col.separator()
        col.operator("bac.sync_paths", icon="FILE_PARENT")
        col.operator("bac.browse_recent_jobs", icon="PRESET")
        col.operator("bac.open_job_folder", icon="FILE_FOLDER")

        box = layout.box()
        box.label(text="Last State")
        box.label(text=f"Revision: {scene_props.last_revision}")
        box.label(text=f"Job: {scene_props.last_job_path or '-'}")
        box.label(text=f"Export: {scene_props.last_export_path or '-'}")
