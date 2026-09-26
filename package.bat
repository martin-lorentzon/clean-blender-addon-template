@echo off
setlocal

rem Set your blender.exe path here (or use the BLENDER_PATH env variable)
set "BLENDER_EXE=C:\...\Blender\blender.exe"

if defined BLENDER_PATH (
    set "BLENDER=%BLENDER_PATH:"=%"
    set "SOURCE=BLENDER_PATH environment variable"
) else (
    set "BLENDER=%BLENDER_EXE%"
    set "SOURCE=package.bat"
)

if not exist "%BLENDER%" (
    echo Blender not found at: "%BLENDER%" ^(from %SOURCE%^)
    echo Fix: set the BLENDER_PATH environment variable to your blender.exe,
    echo      or edit BLENDER_EXE at the top of package.bat.
    goto end
)

"%BLENDER%" --command extension build
if errorlevel 1 (
    echo.
    echo Build failed. Blender path used: "%BLENDER%" ^(from %SOURCE%^)
    echo Fix: check the Blender output above for the error, usually in blender_manifest.toml.
)

:end
pause
