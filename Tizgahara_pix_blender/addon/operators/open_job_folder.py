import bpy

from ..paths import ensure_base_dirs


class BAC_OT_open_job_folder(bpy.types.Operator):
    bl_idname = "bac.open_job_folder"
    bl_label = "Open Job Folder"

    def execute(self, context):
        dirs = ensure_base_dirs(context)
        bpy.ops.wm.path_open(filepath=str(dirs["job"]))
        return {"FINISHED"}
