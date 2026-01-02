#!/usr/bin/env python3
import os
import sys
import re
import argparse
from pathlib import Path

# Constants from Odoo documentation guidelines
ALLOWED_HEADING_CHARS = ["=", "-", "~", "*", "^"]
MAIN_HEADING_CHAR = ALLOWED_HEADING_CHARS[0]
FORBIDDEN_HEADING_CHARS = ["#", '"', "'", "+", "`", "@", "!", ",", ".", "/"]

HEADING_DELIMITER_RE = re.compile(
    "^(" + "|".join(rf"\{char}+" for char in ALLOWED_HEADING_CHARS) + ")$"
)
FORBIDDEN_HEADING_DELIMITER_RE = re.compile(
    "^(" + "|".join(rf"\{char}+" for char in FORBIDDEN_HEADING_CHARS) + ")$"
)
MAIN_HEADING_RE = re.compile(
    rf"^{MAIN_HEADING_CHAR}+\n[^\n]+\n{MAIN_HEADING_CHAR}+$", re.MULTILINE
)

GIT_CONFLICT_MARKERS = ["<" * 7, ">" * 7]


def check_headings(lines, file_path):
    errors = []
    h1_count = 0
    last_delimiter_char_index = -1

    for lno, line in enumerate(lines):
        stripped_line = line.rstrip()

        # Check forbidden characters
        if FORBIDDEN_HEADING_DELIMITER_RE.match(stripped_line):
            errors.append(
                (
                    lno + 1,
                    f"Illegal use of character {stripped_line[0]} in heading delimiter; use one of {', '.join(ALLOWED_HEADING_CHARS)}",
                )
            )
            continue

        if HEADING_DELIMITER_RE.match(stripped_line):
            delimiter_char = stripped_line[0]
            delimiter_char_index = ALLOWED_HEADING_CHARS.index(delimiter_char)

            # Check H1 (overlined and underlined with =)
            if delimiter_char == MAIN_HEADING_CHAR:
                # Is it an overline?
                if lno + 2 < len(lines) and lines[lno + 2].rstrip() == stripped_line:
                    h1_count += 1

            # Check order
            if delimiter_char_index > last_delimiter_char_index + 1:
                last_delimiter_char = (
                    ALLOWED_HEADING_CHARS[last_delimiter_char_index]
                    if last_delimiter_char_index != -1
                    else "None"
                )
                errors.append(
                    (
                        lno + 1,
                        f"Heading delimiter {delimiter_char} not allowed after {last_delimiter_char}; follow order: {', '.join(ALLOWED_HEADING_CHARS)}",
                    )
                )

            last_delimiter_char_index = max(
                last_delimiter_char_index, delimiter_char_index
            )

            # Check length
            heading_lno = -1
            if (
                lno > 0
                and lines[lno - 1].strip()
                and not HEADING_DELIMITER_RE.match(lines[lno - 1].strip())
            ):
                heading_lno = lno - 1
            elif (
                lno + 1 < len(lines)
                and lines[lno + 1].strip()
                and not HEADING_DELIMITER_RE.match(lines[lno + 1].strip())
            ):
                heading_lno = lno + 1

            if heading_lno != -1:
                if len(stripped_line) != len(lines[heading_lno].rstrip()):
                    errors.append(
                        (
                            lno + 1,
                            f"Heading delimiter length ({len(stripped_line)}) must match heading text length ({len(lines[heading_lno].rstrip())})",
                        )
                    )

    if h1_count != 1:
        errors.append(
            (0, f"Document must have exactly one H1 heading (found {h1_count})")
        )

    return errors


def check_formatting(lines):
    errors = []
    for lno, line in enumerate(lines):
        # Line length
        if len(line.rstrip()) > 100:
            if not any(
                x in line for x in ["http://", "https://", ".. image::", ".. figure::"]
            ):
                errors.append(
                    (
                        lno + 1,
                        f"Line exceeds 100 characters ({len(line.rstrip())} chars)",
                    )
                )

        # Conflict markers
        if any(marker in line for marker in GIT_CONFLICT_MARKERS):
            errors.append((lno + 1, "Git conflict markers found"))

        # Tabs
        if "\t" in line:
            errors.append((lno + 1, "Use spaces, not tabs"))

    return errors


def check_resources(lines, file_path):
    errors = []
    file_dir = Path(file_path).parent
    media_dir_name = Path(file_path).stem
    media_dir = file_dir / media_dir_name

    for lno, line in enumerate(lines):
        # Image checks
        img_match = re.search(r"\.\. (image|figure):: (.*)", line)
        if img_match:
            img_path_str = img_match.group(2).strip()

            # Check alt tag
            has_alt = False
            for i in range(1, 5):
                if lno + i < len(lines):
                    if ":alt:" in lines[lno + i]:
                        has_alt = True
                        break
                    if lines[lno + i].strip() == "" or not lines[lno + i].startswith(
                        " "
                    ):  # End of block
                        break
            if not has_alt:
                errors.append((lno + 1, f"Image '{img_path_str}' missing :alt: tag"))

            # Check path/folder convention
            if "/" in img_path_str:
                path_parts = img_path_str.split("/")
                if path_parts[0] != media_dir_name:
                    if path_parts[0] not in [
                        "..",
                        "media",
                    ]:  # Some exceptions exist but generally it should be same name
                        errors.append(
                            (
                                lno + 1,
                                f"Image '{img_path_str}' should be in folder '{media_dir_name}'",
                            )
                        )

            # Check naming (no underscores)
            img_name = img_path_str.split("/")[-1]
            if "_" in img_name:
                errors.append(
                    (
                        lno + 1,
                        f"Image name '{img_name}' should use hyphens, not underscores",
                    )
                )

    return errors


def fix_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    new_lines = []
    modified = False

    for lno, line in enumerate(lines):
        stripped = line.rstrip()

        # Fix trailing whitespace
        if line.endswith(" \n") or line.endswith("\t\n"):
            line = stripped + "\n"
            modified = True

        # Fix heading delimiter length
        if HEADING_DELIMITER_RE.match(stripped):
            heading_lno = -1
            if (
                lno > 0
                and lines[lno - 1].strip()
                and not HEADING_DELIMITER_RE.match(lines[lno - 1].strip())
            ):
                heading_lno = lno - 1
            elif (
                lno + 1 < len(lines)
                and lines[lno + 1].strip()
                and not HEADING_DELIMITER_RE.match(lines[lno + 1].strip())
            ):
                heading_lno = lno + 1

            if heading_lno != -1:
                target_len = len(lines[heading_lno].rstrip())
                if len(stripped) != target_len:
                    line = stripped[0] * target_len + "\n"
                    modified = True

        new_lines.append(line)

    if modified:
        with open(file_path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print(f"  [FIXED] {file_path}")
    else:
        # print(f"  [UNCHANGED] {file_path}")
        pass


def validate_file(file_path, args):
    if args.fix:
        fix_file(file_path)

    with open(file_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    errors = []
    errors.extend(check_headings(lines, file_path))
    errors.extend(check_formatting(lines))
    errors.extend(check_resources(lines, file_path))

    if errors:
        print(f"Errors in {file_path}:")
        for lno, msg in sorted(errors):
            loc = f"Line {lno}" if lno > 0 else "File"
            print(f"  [{loc}] {msg}")
        return False
    else:
        print(f"  [OK] {file_path}")
        return True


def main():
    parser = argparse.ArgumentParser(description="Odoo Documentation Validator")
    parser.add_argument("path", help="Path to RST file or directory")
    parser.add_argument(
        "--fix", action="store_true", help="Automatically fix some issues"
    )
    parser.add_argument(
        "--recursive", "-r", action="store_true", help="Recursive validation"
    )

    args = parser.parse_args()

    path = Path(args.path)
    if not path.exists():
        print(f"Error: {path} not found")
        sys.exit(1)

    files = []
    if path.is_file():
        files.append(path)
    else:
        pattern = "**/*.rst" if args.recursive else "*.rst"
        files.extend(path.glob(pattern))

    all_success = True
    for file in files:
        if not validate_file(file, args):
            all_success = False

    sys.exit(0 if all_success else 1)


if __name__ == "__main__":
    main()
