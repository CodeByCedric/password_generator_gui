'''setup for cx_freeze'''

from cx_Freeze import setup, Executable

# Define the executable
executables = [
    Executable(
        script="gui_password_generator.py",
        base="Win32GUI",
        icon="assets\icons\lock_and_key.ico"
    )
]

# Setup configuration
setup(
    name="Password Generator",
    version="1.0",
    description="Password generator",
    executables=executables
)
