bl_info = {
    "name": "Blender Aseprite Companion",
    "author": "Codex",
    "version": (0, 1, 0),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > PixelArt",
    "description": "Generate Aseprite edit jobs and safely reload exported textures.",
    "category": "Import-Export",
}

from .addon.registration import register, unregister

__all__ = ["register", "unregister"]
