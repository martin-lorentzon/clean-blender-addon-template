# Clean Blender Add-on Template
## Complete structure • Reloadable in Blender • Formatted with autopep8
A commented template for multifile add-on development that is fully compliant with the Blender Extensions platform

## Script Directory
I recommend placing your add-on inside of a [script directory](https://docs.blender.org/manual/en/latest/editors/preferences/file_paths.html#script-directories) during development for an easy install
```
Some Local Projects or Tools Folder/
├── Blender Add-ons/ (script directory)
│      └── addons/
│            └── my_useful_tool/ (add-on)
```
> [!NOTE]
> Remember to install your newly created script directory in Blender Preferences > File Paths > Script Directories

## Features
* Formatted with autopep8
* Ability to reload in Blender with `bpy.ops.script.reload()`
* Includes bl_info metadata
* Includes Blender manifest file
* Includes examples of add-on preferences, property group, operator and panel
* Includes a bat file for simple packaging

> [!TIP]
> Add the Reload Scripts operator to your Quick Favorites menu inside of Blender

## How to use the template via GitHub
1. At the top right corner of the repository page, click Use this template
2. Click Create a new repository
3. You may need to select your account if you're in one or more organisations
4. Name your repository and press Create repository
5. 🎉 Finished! 🎉
