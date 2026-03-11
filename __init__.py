bl_info = {
    "name": "Your Add-on Name",
    "description": "Your add-on description.",
    "author": "Your Signature",
    "version": (1, 0, 0),
    "blender": (5, 1, 0),
    "location": "3D Viewport > Sidebar > Hello World",
    # "doc_url": "https://github.com/{username}/{repo-name}",
    # "tracker_url": "https://github.com/{username}/{repo-name}/issues",
    # "warning": "Experimental",
    "support": "COMMUNITY",
    "category": "Some Category",
    # Categories: 3D View, Add Curve, Add Mesh, Animation, Bake, Camera, Compositing,
    # Development, Game Engine, Grease Pencil, Import-Export, Lighting, Material,
    # Mesh, Node, Object, Paint, Physics, Render, Rigging, Scene, Sequencer,
    # System, Text Editor, Tracking, UV, User Interface
}


# NOTE: Edit package.bat and specify the path to your blender.exe file


# ——————————————————————————————————————————————————————————————————————
# MARK: IMPORTS
# ——————————————————————————————————————————————————————————————————————


# fmt: off
_needs_reload = "bpy" in locals()

import bpy
from . import addon_preferences
from . import hello_world_module
from . import simple_module


if _needs_reload:
    from importlib import reload

    # Specify the modules to reload during development
    reload(addon_preferences)
    reload(hello_world_module)
    reload(simple_module)
# fmt: on


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


modules = [
    addon_preferences,
    hello_world_module,
    simple_module,
]


def register():
    for module in modules:
        module.register()


def unregister():
    for module in reversed(modules):
        module.unregister()


if __name__ == "__main__":
    register()
