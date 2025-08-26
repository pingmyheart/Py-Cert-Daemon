import platform

import PyInstaller.__main__ as pyinstaller

import app

excluded_files = ["*.env",
                  ".env",
                  "**/.env"]
pyinstaller_commands = ["--onefile",
                        "--name",
                        f"py-cert-daemon-{platform.system()}"]

for excluded_file in excluded_files:
    pyinstaller_commands.append("--exclude")
    pyinstaller_commands.append(f"{excluded_file}")

pyinstaller_commands.append(f"{app.__name__}.py")

print(f"Command preview: \npyinstaller {' '.join(pyinstaller_commands)}")
pyinstaller.run(pyinstaller_commands)
