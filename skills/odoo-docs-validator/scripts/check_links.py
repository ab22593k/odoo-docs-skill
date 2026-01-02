#!/usr/bin/env python3
import os
import sys
import re
from pathlib import Path
import argparse


def collect_targets(root_dir):
    """Scan all RST files to find available targets and documents."""
    targets = set()
    docs = set()

    # Regex for .. _target-name:
    target_re = re.compile(r"^\.\. _([^:]+):", re.MULTILINE)

    root_path = Path(root_dir)
    for rst_file in root_path.rglob("*.rst"):
        rel_path = rst_file.relative_to(root_path)
        doc_name = str(rel_path.with_suffix(""))
        docs.add(doc_name)

        try:
            with open(rst_file, "r", encoding="utf-8") as f:
                content = f.read()
                # Find explicit targets
                for match in target_re.finditer(content):
                    targets.add(match.group(1))
                # Find headings as targets (Sphinx creates them automatically)
                # This is more complex, we'll skip for now to avoid false positives
        except Exception as e:
            print(f"Error reading {rst_file}: {e}")

    return targets, docs


def check_links_in_file(file_path, all_targets, all_docs, root_dir):
    """Check for broken :ref: and :doc: links in a single file."""
    errors = []
    root_path = Path(root_dir)
    file_path = Path(file_path)
    file_dir = file_path.parent

    # Regex for :ref:`label <target>` or :ref:`target`
    ref_re = re.compile(r":ref:`(?:[^<]*<)?([^>`\s]+)(?:>)?`")
    # Regex for :doc:`label <path>` or :doc:`path`
    doc_re = re.compile(r":doc:`(?:[^<]*<)?([^>`\s]+)(?:>)?`")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            for lno, line in enumerate(lines):
                # Check refs
                for match in ref_re.finditer(line):
                    target = match.group(1)
                    if target not in all_targets:
                        # Skip standard ones or external
                        if not any(
                            target.startswith(x) for x in ["http", "mailto", "std:"]
                        ):
                            errors.append((lno + 1, f"Broken :ref: target '{target}'"))

                # Check docs
                for match in doc_re.finditer(line):
                    target = match.group(1)
                    # Sphinx :doc: resolution logic
                    if target.startswith("/"):
                        resolved_doc = target[1:]
                    else:
                        # Relative to current file's directory
                        rel_dir = file_dir.relative_to(root_path)
                        resolved_doc = os.path.normpath(
                            os.path.join(str(rel_dir), target)
                        )

                    if resolved_doc not in all_docs:
                        errors.append(
                            (
                                lno + 1,
                                f"Broken :doc: path '{target}' (resolved to '{resolved_doc}')",
                            )
                        )
    except Exception as e:
        errors.append((0, f"Error processing file: {e}"))

    return errors


def main():
    parser = argparse.ArgumentParser(description="Odoo Documentation Link Checker")
    parser.add_argument("path", help="Path to RST file or directory to check")
    parser.add_argument(
        "--root",
        default="content",
        help="Root documentation directory (default: content)",
    )

    args = parser.parse_args()

    if not os.path.exists(args.root):
        print(f"Error: Root directory '{args.root}' not found.")
        sys.exit(1)

    print(f"Scanning '{args.root}' for targets and documents...")
    all_targets, all_docs = collect_targets(args.root)
    print(f"Found {len(all_targets)} targets and {len(all_docs)} documents.")

    target_path = Path(args.path)
    if target_path.is_file():
        files = [target_path]
    else:
        files = list(target_path.rglob("*.rst"))

    all_success = True
    for file in files:
        errors = check_links_in_file(file, all_targets, all_docs, args.root)
        if errors:
            all_success = False
            print(f"Link errors in {file}:")
            for lno, msg in errors:
                print(f"  [Line {lno}] {msg}")
        else:
            # print(f"  [OK] {file}")
            pass

    if all_success:
        print("✅ No broken :ref: or :doc: links found in the specified path.")
    else:
        print("❌ Found broken links.")
        sys.exit(1)


if __name__ == "__main__":
    main()
