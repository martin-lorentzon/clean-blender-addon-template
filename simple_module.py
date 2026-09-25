import bpy


# ——————————————————————————————————————————————————————————————————————
# MARK: INTERFACE
# ——————————————————————————————————————————————————————————————————————


class SIMPLE_PT_main(bpy.types.Panel):  # {MODULE_NAME}_PT_{panel_name}
    # MODULE_NAME: simple_module -> SIMPLE (_module is excluded)
    # The class name doubles as the panel's bl_idname, so it must be unique across all add-ons
    bl_label = "Simple Panel"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Hello World"

    def draw(self, context):
        layout = self.layout

        layout.operator("object.simple_operator")


# ——————————————————————————————————————————————————————————————————————
# MARK: OPERATORS
# ——————————————————————————————————————————————————————————————————————


class OBJECT_OT_simple_operator(bpy.types.Operator):  # {CATEGORY}_OT_{operator_name}
    bl_idname = "object.simple_operator"  # {category}.{operator_name}
    bl_label = "Simple Operator"
    bl_description = "A short description of what the operator does"
    bl_options = {"REGISTER"}

    def execute(self, context):
        ...
        return {"FINISHED"}


# ——————————————————————————————————————————————————————————————————————
# MARK: REGISTRATION
# ——————————————————————————————————————————————————————————————————————


classes = [
    SIMPLE_PT_main,
    OBJECT_OT_simple_operator,
]

register, unregister = bpy.utils.register_classes_factory(classes)

# register_classes_factory generates the equivalent of these two functions:
#
# def register():
#     for cls in classes:
#         bpy.utils.register_class(cls)
#
# def unregister():
#     for cls in reversed(classes):
#         bpy.utils.unregister_class(cls)
#
# See hello_world_module.py for registration with properties
