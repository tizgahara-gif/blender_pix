from pathlib import Path
import shutil

import bpy

from ..asset_resolver import resolve_active_asset
from ..job_io import build_job_payload, write_job
from ..paths import ensure_base_dirs, file_stem_safe
from ..recent_jobs import push_recent_job
from ..revision import next_revision
from ..uv_exporter import export_uv_layout


class BAC_OT_generate_job(bpy.types.Operator):
    bl_idname = "bac.generate_job"
    bl_label = "Generate Aseprite Job"
    bl_options = {"REGISTER"}

    def execute(self, context):
        scene_props = context.scene.bac_scene
        settings = context.scene.bac_addon
        try:
            asset = resolve_active_asset(context)
            dirs = ensure_base_dirs(context)
            base = file_stem_safe(f"{asset.object_name}_{asset.image.name}")
            rev = next_revision(dirs["job"], base)
            rev_tag = f"r{rev:03d}"

            source_path = dirs["source"] / f"{base}_{rev_tag}.png"
            export_path = dirs["export"] / f"{base}_{rev_tag}.png"
            shutil.copy2(asset.image_path, source_path)

            guide_paths = []
            if settings.include_uv_guide:
                guide_path = dirs["source"] / f"{base}_{rev_tag}_uv.png"
                export_uv_layout(context, guide_path, size=settings.uv_guide_size)
                guide_paths.append(guide_path)

            payload = build_job_payload(
                asset=asset,
                map_type=settings.map_type,
                source_path=source_path,
                export_path=export_path,
                guide_paths=guide_paths,
                revision=rev,
            )
            job_path = dirs["job"] / f"{base}_{rev_tag}.json"
            write_job(job_path, payload)
            push_recent_job(context, str(job_path))

            scene_props.last_job_path = str(job_path)
            scene_props.last_export_path = str(export_path)
            scene_props.last_revision = rev
            asset.image.bac_image.linked_revision = rev
            asset.image.bac_image.linked_export_path = str(export_path)

            self.report({"INFO"}, f"Generated job: {job_path.name}")
            return {"FINISHED"}
        except Exception as exc:
            self.report({"ERROR"}, str(exc))
            return {"CANCELLED"}
