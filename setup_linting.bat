@echo off
rem Creates a local .venv with fake-bpy-module so VS Code can lint bpy code
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
    echo Creating virtual environment in .venv...
    py -3 -m venv .venv 2>nul || python -m venv .venv
    if errorlevel 1 (
        echo Failed to create .venv. Make sure Python 3 is installed and on PATH.
        pause
        exit /b 1
    )
)

echo Installing fake-bpy-module...
".venv\Scripts\python.exe" -m pip install --upgrade pip
".venv\Scripts\python.exe" -m pip install --upgrade fake-bpy-module
if errorlevel 1 (
    echo Failed to install fake-bpy-module.
    pause
    exit /b 1
)

echo.
echo Done. Reload VS Code and make sure the .venv interpreter is selected.
pause
