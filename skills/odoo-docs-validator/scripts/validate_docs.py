#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path


def check_headings(content):
    errors = []
    # Check for exactly one H1
    h1_matches = re.findall(r"^={3,}\n.*\n={3,}$", content, re.MULTILINE)
    if len(h1_matches) == 0:
        # Check alternate H1 (overlined and underlined with =)
        pass  # The regex above handles it

    # Simple check for H1 symbols
    lines = content.splitlines()
    h1_count = 0
    for i, line in enumerate(lines):
        if i < len(lines) - 2:
            if re.match(r"^={3,}$", lines[i]) and re.match(r"^={3,}$", lines[i + 2]):
                h1_count += 1

    if h1_count != 1:
        errors.append(f"Document must have exactly one H1 heading (found {h1_count})")

    return errors


def check_line_length(content):
    errors = []
    for i, line in enumerate(content.splitlines()):
        if len(line) > 100:
            # Skip if it looks like a URL
            if "http://" not in line and "https://" not in line:
                errors.append(
                    f"Line {i + 1} exceeds 100 characters ({len(line)} chars)"
                )
    return errors


def check_alt_tags(content):
    errors = []
    # Look for .. image:: without a following :alt:
    lines = content.splitlines()
    for i, line in enumerate(lines):
        if ".. image::" in line:
            has_alt = False
            # Check next 3 lines for :alt:
            for j in range(1, 4):
                if i + j < len(lines):
                    if ":alt:" in lines[i + j]:
                        has_alt = True
                        break
            if not has_alt:
                errors.append(f"Image on line {i + 1} is missing an :alt: tag")
    return errors


def validate_file(file_path):
    print(f"Validating {file_path}...")
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()

        errors = []
        errors.extend(check_headings(content))
        errors.extend(check_line_length(content))
        errors.extend(check_alt_tags(content))

        if errors:
            for err in errors:
                print(f"  [ERROR] {err}")
            return False
        else:
            print("  [OK] No major style violations found.")
            return True
    except Exception as e:
        print(f"  [CRITICAL] Could not read file: {e}")
        return False


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 validate_docs.py <path_to_rst_file>")
        sys.exit(1)

    target = sys.argv[1]
    if os.path.isfile(target):
        success = validate_file(target)
        sys.exit(0 if success else 1)
    else:
        print(f"Error: {target} is not a file")
        sys.exit(1)
