import bpy

from .operators.browse_recent_jobs import BAC_OT_browse_recent_jobs
from .operators.export_uv_guide import BAC_OT_export_uv_guide
from .operators.generate_job import BAC_OT_generate_job
from .operators.launch_aseprite import BAC_OT_launch_aseprite
from .operators.open_job_folder import BAC_OT_open_job_folder
from .operators.reload_exported_image import BAC_OT_reload_exported_image
from .operators.sync_paths import BAC_OT_sync_paths
from .operators.validate_asset import BAC_OT_validate_asset
from .panels import BAC_PT_main_panel
from .preferences import BAC_AddonPreferences
from .props.addon_props import BAC_AddonProps
from .props.image_props import BAC_ImageProps
from .props.scene_props import BAC_SceneProps
from .relay_sync import ensure_timer_registered, on_load_post, stop_timer

CLASSES = (
    BAC_AddonPreferences,
    BAC_AddonProps,
    BAC_SceneProps,
    BAC_ImageProps,
    BAC_OT_validate_asset,
    BAC_OT_generate_job,
    BAC_OT_export_uv_guide,
    BAC_OT_launch_aseprite,
    BAC_OT_reload_exported_image,
    BAC_OT_browse_recent_jobs,
    BAC_OT_open_job_folder,
    BAC_OT_sync_paths,
    BAC_PT_main_panel,
)


def register():
    for cls in CLASSES:
        bpy.utils.register_class(cls)

    bpy.types.Scene.bac_addon = bpy.props.PointerProperty(type=BAC_AddonProps)
    bpy.types.Scene.bac_scene = bpy.props.PointerProperty(type=BAC_SceneProps)
    bpy.types.Image.bac_image = bpy.props.PointerProperty(type=BAC_ImageProps)

    ensure_timer_registered()
    if on_load_post not in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.append(on_load_post)


def unregister():
    stop_timer()
    if on_load_post in bpy.app.handlers.load_post:
        bpy.app.handlers.load_post.remove(on_load_post)

    del bpy.types.Image.bac_image
    del bpy.types.Scene.bac_scene
    del bpy.types.Scene.bac_addon

    for cls in reversed(CLASSES):
        bpy.utils.unregister_class(cls)
