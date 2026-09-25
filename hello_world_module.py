import bpy
from bpy.props import EnumProperty, PointerProperty, StringProperty


# ——————————————————————————————————————————————————————————————————————
# MARK: PROPERTIES
# ——————————————————————————————————————————————————————————————————————


class HelloWorldProperties(bpy.types.PropertyGroup):
    # Example properties
    color: EnumProperty(
        name="Color",
        items=[
            ("CYAN", "Cyan", "The color of tropical waters"),  # (identifier, name, description)
            ("MAGENTA", "Magenta", "The color of orchids"),
            ("YELLOW", "Yellow", "The color of a rubber duck"),
        ]
    )
    message: StringProperty(
        name="Message",
        default="Hello, World!"
    )


# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class HELLO_WORLD_PT_main(bpy.types.Panel):
    bl_label = "Hello World"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"

    @classmethod
    def poll(cls, context) -> bool:
        return True  # Dictates when the panel should be enabled
        # can be used to restrict it to a specific state
        # return context.mode == "OBJECT"

    def draw(self, context):
        props = context.scene.hello_world_properties
        layout = self.layout

        layout.prop(props, "color")
        layout.prop(props, "message")
        layout.operator("scene.hello_world", text=f"Print {props.message}")

        # This is how we define a subpanel, its id follows the same convention: {MODULE_NAME}_PT_{panel_name}, and must be unique
        header, panel = layout.panel("HELLO_WORLD_PT_look_inside", default_closed=True)
        header.label(text="Look Inside")
        if panel:
            panel.label(text="Success")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class SCENE_OT_hello_world(bpy.types.Operator):
    bl_idname = "scene.hello_world"
    bl_label = "Print Hello, World!"
    bl_description = "Prints the username, color and message to the console"
    bl_options = {"REGISTER"}
    # Common bl_options values:
    # "REGISTER"     Show in the info window and support the redo (F9) panel
    # "UNDO"         Push an undo step when finished (required if the operator modifies Blender data)
    # "INTERNAL"     Hide the operator from search results
    # "PRESET"       Show a preset button for the operator's settings

    @classmethod
    def poll(cls, context) -> bool:
        return True

    def execute(self, context):
        # This is how we access add-on preferences
        addon_prefs = context.preferences.addons[__package__].preferences

        # Similarly, this is how we access property groups
        props = context.scene.hello_world_properties

        print(addon_prefs.username, props.color, props.message, sep=": ")
        return {"FINISHED"}


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


classes = [
    HelloWorldProperties,
    HELLO_WORLD_PT_main,
    SCENE_OT_hello_world,
]

# Registers classes in order and unregisters them in reverse order
basic_register, basic_unregister = bpy.utils.register_classes_factory(classes)


# Wrap the generated functions to register additional properties
def register():
    basic_register()
    bpy.types.Scene.hello_world_properties = PointerProperty(type=HelloWorldProperties)


# Unregister in the reverse order of registration
def unregister():
    del bpy.types.Scene.hello_world_properties
    basic_unregister()
