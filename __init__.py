# bl_info is only read when installed as a legacy add-on,
# extensions use blender_manifest.toml instead (keep the two in sync)
bl_info = {
    "name": "My Example Extension",
    "description": "Your add-on description.",
    "author": "Your Signature",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "3D Viewport > Sidebar > Hello World",
    # "doc_url": "https://github.com/{username}/{repo-name}",
    # "tracker_url": "https://github.com/{username}/{repo-name}/issues",
    # "warning": "Experimental",
    "support": "COMMUNITY",
    "category": "Pick a Category",
    # Categories: 3D View, Add Curve, Add Mesh, Animation, Bake, Camera, Compositing,
    # Development, Grease Pencil, Import-Export, Lighting, Material,
    # Mesh, Node, Object, Paint, Physics, Render, Rigging, Scene, Sequencer,
    # System, Text Editor, Tracking, UV, User Interface
}


# NOTE: Set BLENDER_EXE in package.bat to your blender.exe path (or use the BLENDER_PATH env variable)


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
