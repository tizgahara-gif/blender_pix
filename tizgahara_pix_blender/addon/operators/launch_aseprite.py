import bpy

from ..aseprite_bridge import launch_aseprite
from ..config import get_prefs


class BAC_OT_launch_aseprite(bpy.types.Operator):
    bl_idname = "bac.launch_aseprite"
    bl_label = "Launch Aseprite"

    def execute(self, context):
        scene_props = context.scene.bac_scene
        if not scene_props.last_job_path:
            self.report({"ERROR"}, "No generated job to launch")
            return {"CANCELLED"}
        prefs = get_prefs(context)
        if not prefs or not prefs.aseprite_executable:
            self.report({"ERROR"}, "Aseprite executable not set in preferences")
            return {"CANCELLED"}
        result = launch_aseprite(prefs.aseprite_executable, scene_props.last_job_path)
        if result.returncode != 0:
            self.report({"ERROR"}, result.stderr.strip() or "Failed to launch Aseprite")
            return {"CANCELLED"}
        self.report({"INFO"}, "Aseprite launched")
        return {"FINISHED"}
