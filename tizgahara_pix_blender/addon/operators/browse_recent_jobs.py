import bpy

from ..recent_jobs import list_recent_jobs


class BAC_OT_browse_recent_jobs(bpy.types.Operator):
    bl_idname = "bac.browse_recent_jobs"
    bl_label = "Print Recent Jobs"

    def execute(self, context):
        jobs = list_recent_jobs(context)
        if not jobs:
            self.report({"INFO"}, "No recent jobs")
            return {"CANCELLED"}
        for job in jobs:
            self.report({"INFO"}, job)
        return {"FINISHED"}
