import bpy
from bpy.types import AddonPreferences
from bpy.props import StringProperty


class YourAddonPreferences(AddonPreferences):  # <AddonNamePreferences>
    bl_idname = __package__

    # Examples
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


register, unregister = bpy.utils.register_classes_factory((YourAddonPreferences,))
# NOTE: The trailing comma here is required to make a tuple
