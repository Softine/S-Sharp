from cx_Freeze import setup, Executable
base = None
executables = [Executable("Main.py", base=base)]
packages = ["idna"]
options = {
    'build_exe': {
        'packages':packages,
    },
}
setup(
    name = "CUSTOM",
    options = options,
    version = "0.2",
    description = '',
    executables = executables
)
