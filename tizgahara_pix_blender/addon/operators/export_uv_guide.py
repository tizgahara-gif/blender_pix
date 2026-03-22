from pathlib import Path

import bpy

from ..paths import ensure_base_dirs, file_stem_safe
from ..uv_exporter import export_uv_layout


class BAC_OT_export_uv_guide(bpy.types.Operator):
    bl_idname = "bac.export_uv_guide"
    bl_label = "Export UV Guide"

    def execute(self, context):
        obj = context.view_layer.objects.active
        if not obj:
            self.report({"ERROR"}, "No active object")
            return {"CANCELLED"}
        dirs = ensure_base_dirs(context)
        filename = file_stem_safe(obj.name) + "_uv.png"
        out = Path(dirs["source"]) / filename
        try:
            export_uv_layout(context, out, size=context.scene.bac_addon.uv_guide_size)
            self.report({"INFO"}, f"Exported UV guide: {out.name}")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}
