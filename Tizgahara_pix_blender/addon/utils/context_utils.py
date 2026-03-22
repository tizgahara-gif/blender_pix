import bpy


def active_object(context: bpy.types.Context):
    return context.view_layer.objects.active
