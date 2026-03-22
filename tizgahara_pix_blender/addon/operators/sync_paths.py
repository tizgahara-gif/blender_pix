from pathlib import Path

import bpy

from ..asset_resolver import resolve_active_asset
from ..sync_watch import register_watch_for_image


class BAC_OT_sync_paths(bpy.types.Operator):
    bl_idname = "bac.sync_paths"
    bl_label = "Sync Paths"

    def execute(self, context):
        scene_props = context.scene.bac_scene
        try:
            asset = resolve_active_asset(context)
            if asset.image.bac_image.linked_export_path:
                scene_props.last_export_path = asset.image.bac_image.linked_export_path
                register_watch_for_image(asset.image, Path(asset.image.bac_image.linked_export_path))
            scene_props.last_revision = asset.image.bac_image.linked_revision
            self.report({"INFO"}, "Synced scene state from image")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}
