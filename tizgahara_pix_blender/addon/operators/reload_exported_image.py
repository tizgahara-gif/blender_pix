from pathlib import Path

import bpy

from ..asset_resolver import resolve_active_asset
from ..image_reload import reload_image_from_export


class BAC_OT_reload_exported_image(bpy.types.Operator):
    bl_idname = "bac.reload_exported_image"
    bl_label = "Reload Exported Image"

    def execute(self, context):
        scene_props = context.scene.bac_scene
        if not scene_props.last_export_path:
            self.report({"ERROR"}, "No export path recorded")
            return {"CANCELLED"}
        try:
            asset = resolve_active_asset(context)
            reload_image_from_export(asset.image, Path(scene_props.last_export_path))
            self.report({"INFO"}, "Image reloaded from export")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}
