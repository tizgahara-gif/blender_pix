import bpy

from ..validation import validate_ready


class BAC_OT_validate_asset(bpy.types.Operator):
    bl_idname = "bac.validate_asset"
    bl_label = "Validate Asset"

    def execute(self, context):
        try:
            errors = validate_ready(context)
            if errors:
                for line in errors:
                    self.report({"ERROR"}, line)
                return {"CANCELLED"}
            self.report({"INFO"}, "Validation passed")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}
