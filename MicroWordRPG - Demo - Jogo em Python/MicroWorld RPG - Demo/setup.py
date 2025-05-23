from cx_Freeze import setup, Executable

setup(
    name="MicroWorld RPG - Demo",
    version="1.0",
    description="MicroWorld RPG Demo version",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=[Executable("main.py")]
)