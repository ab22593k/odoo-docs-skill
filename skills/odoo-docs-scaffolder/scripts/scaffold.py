#!/usr/bin/env python3
import os
import sys
import shutil
from pathlib import Path

TEMPLATES_DIR = Path(__file__).parent.parent / "assets" / "templates"


def scaffold(target_path, template_name="standard_page.rst"):
    template_file = TEMPLATES_DIR / template_name
    if not template_file.exists():
        print(f"Error: Template '{template_name}' not found.")
        return False

    target_path = Path(target_path)
    if not target_path.suffix == ".rst":
        target_path = target_path.with_suffix(".rst")

    if target_path.exists():
        print(f"Error: File '{target_path}' already exists.")
        return False

    # Ensure directory exists
    target_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        shutil.copy(template_file, target_path)
        print(f"✅ Successfully scaffolded '{target_path}' using '{template_name}'.")

        # Create media folder
        media_folder = target_path.parent / target_path.stem
        media_folder.mkdir(exist_ok=True)
        print(f"✅ Created media directory: '{media_folder}/'")

        return True
    except Exception as e:
        print(f"Error during scaffolding: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 scaffold.py <target_path> [template_name]")
        sys.exit(1)

    target = sys.argv[1]
    template = sys.argv[2] if len(sys.argv) > 2 else "standard_page.rst"

    success = scaffold(target, template)
    sys.exit(0 if success else 1)
