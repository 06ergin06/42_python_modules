#!/usr/bin/env python3


import sys
import os
import site


if __name__ == "__main__":
    path: str = sys.prefix
    cur_python: str = sys.executable
    name: str = os.path.basename(path)
    site_packages: list[str] = site.getsitepackages()
    package_path: str = site_packages[0] if site_packages else "Unknown"

    if hasattr(sys, 'base_prefix') and sys.prefix != sys.base_prefix:
        print("MATRIX STATUS: Welcome to the construct\n")
        print(f"Current Python: {cur_python}")
        print(f"Virtual Environment: {name}")
        print(f"Environment Path: {path}\n")
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print("Package installation path: ")
        print(package_path)
    else:
        print("MATRIX STATUS: You're still plugged in\n")
        print(f"Current Python: {cur_python}")
        print("Virtual Environment: None detected\n")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.\n")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate # On Unix")
        print("matrix_env\\Scripts\\activate # On Windows\n")
        print("Then run this program again.")
