bl_info = {
    "name": "Tizgahara Pix Blender",
    "author": "tizgahara-gif",
    "version": (0, 1, 0),
    "blender": (4, 2, 0),
    "location": "View3D > Sidebar > PixelArt",
    "description": "Generate Aseprite edit jobs and safely reload exported textures.",
    "category": "Import-Export",
}

from .addon.registration import register, unregister

__all__ = ["register", "unregister"]
