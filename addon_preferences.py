import bpy
from bpy.props import StringProperty


class MyExampleExtensionPreferences(bpy.types.AddonPreferences):  # Naming convention: {AddonName}Preferences
    bl_idname = __package__

    # Example properties
    username: StringProperty(
        name="Username",
        default="User"
    )
    password: StringProperty(
        name="Password",
        subtype="PASSWORD"
    )

    def draw(self, context):
        layout = self.layout
        layout.use_property_split = True

        layout.prop(self, "username")
        layout.prop(self, "password")


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


classes = [
    MyExampleExtensionPreferences,
]

register, unregister = bpy.utils.register_classes_factory(classes)
