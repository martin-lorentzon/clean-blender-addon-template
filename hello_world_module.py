import bpy
from bpy.props import EnumProperty, StringProperty


# ——————————————————————————————————————————————————————————————————————
# MARK: PROPERTIES
# ——————————————————————————————————————————————————————————————————————


class HelloWorldProperties(bpy.types.PropertyGroup):
    # Examples
    color: EnumProperty(
        name="Color",
        items=[
            ("CYAN", "Cyan", "The color of tropical waters"),
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


class HELLO_WORLD_PT_main_panel(bpy.types.Panel):
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

        # This is how we define a subpanel
        header, panel = layout.panel("my_panel_id", default_closed=True)
        header.label(text="Look Inside")
        if panel:
            panel.label(text="Success")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class HELLO_WORLD_OT_print_hello_world(bpy.types.Operator):
    bl_idname = "scene.hello_world"  # {category}.{operator_name}
    bl_label = "Print Hello, World!"
    bl_description = "A short description of what the operator does"
    bl_options = {"REGISTER", "UNDO"}
    # Some operators shouldn't include an 'UNDO' (e.g. read-only and temporary UI)
    # bl_options = {"INTERNAL"}  # this would be more suitable in such cases

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        # This is how we access add-on preferences
        addon_prefs = context.preferences.addons[__package__].preferences

        # Similarly, this is how we access property groups
        props = context.scene.hello_world_properties

        print(addon_prefs.username, props.message, sep=": ")
        return {"FINISHED"}


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


basic_register, basic_unregister = bpy.utils.register_classes_factory(
    (
        HelloWorldProperties,
        HELLO_WORLD_PT_main_panel,
        HELLO_WORLD_OT_print_hello_world,
    ))


# Wrap the generated functions to register additional properties
def register():
    basic_register()
    bpy.types.Scene.hello_world_properties = bpy.props.PointerProperty(type=HelloWorldProperties)


def unregister():
    basic_unregister()
    del bpy.types.Scene.hello_world_properties
