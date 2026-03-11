import bpy


# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class SIMPLE_PT_panel(bpy.types.Panel):
    bl_label = "Simple Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"

    def draw(self, context):
        layout = self.layout

        layout.operator("wm.simple_operator")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class SIMPLE_OT_operator(bpy.types.Operator):
    bl_idname = "wm.simple_operator"
    bl_label = "Simple Operator"

    def execute(self, context):
        ...
        return {"FINISHED"}


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


register, unregister = bpy.utils.register_classes_factory(
    (
        SIMPLE_PT_panel,
        SIMPLE_OT_operator,
    ))
