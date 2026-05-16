import os

# -------------------------------
# Project Structure Definition
# -------------------------------

PROJECT_STRUCTURE = {
    "src": {
        "component": {
            "__init__.py": "",
            "example_component.py": """class ExampleComponent:
    def __init__(self):
        print("ExampleComponent initialized")

    def run(self):
        print("Running ExampleComponent...")
"""
        },
        "constant": {
            "__init__.py": "",
            "config.py": """APP_NAME = "My Python Project"
VERSION = "1.0.0"
"""
        },
        "__init__.py": ""
    },
    "app.py": """#!/usr/bin/env python3

import sys
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(ROOT_DIR, "src")
sys.path.append(SRC_DIR)

from component.example_component import ExampleComponent
from constant.config import APP_NAME, VERSION


def initialize():
    print(f"Starting {APP_NAME} v{VERSION}")


def main():
    initialize()
    comp = ExampleComponent()
    comp.run()


if __name__ == "__main__":
    main()
"""
,
    "requirements.txt": "",
    ".gitignore": """__pycache__/
*.pyc
.env
""",
    "README.md": "# Project Initialized\n\nGenerated using project bootstrap script."
}


# -------------------------------
# Folder + File Creation Function
# -------------------------------

def create_structure(base_path, structure_dict):
    for name, content in structure_dict.items():
        path = os.path.join(base_path, name)

        # If content is a dict → it's a folder
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            create_structure(path, content)

        # Else → it's a file
        else:
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)


# -------------------------------
# Run Script
# -------------------------------

if __name__ == "__main__":
    base = os.getcwd()
    print(f"Creating project structure in: {base}")
    create_structure(base, PROJECT_STRUCTURE)
    print("\n✨ Project structure created successfully!")
