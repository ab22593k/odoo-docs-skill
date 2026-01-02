#!/usr/bin/env python3
"""
Utility script for searching and exploring Odoo documentation structure.
This script helps locate relevant documentation files based on keywords or file paths.
"""

import os
import sys
from pathlib import Path
from typing import List, Dict, Union

# Default documentation path relative to project root
DEFAULT_DOC_PATH = "content"


def find_files_by_keyword(
    keyword: str, doc_path: Union[str, Path, None] = None
) -> List[str]:
    """
    Find documentation files containing a specific keyword in their path or name.

    Args:
        keyword: The keyword to search for
        doc_path: Path to documentation directory (defaults to DEFAULT_DOC_PATH)

    Returns:
        List of matching file paths
    """
    if doc_path is None:
        doc_path = Path(DEFAULT_DOC_PATH)
    else:
        doc_path = Path(doc_path)

    if not doc_path.exists():
        print(f"Error: Documentation path not found: {doc_path}")
        return []

    matches = []
    keyword_lower = keyword.lower()

    for rst_file in doc_path.rglob("*.rst"):
        path_str = str(rst_file.relative_to(doc_path))
        if keyword_lower in path_str.lower():
            matches.append(path_str)

    return matches


def find_files_by_content(
    keyword: str, doc_path: Union[str, Path, None] = None
) -> List[str]:
    """
    Find documentation files containing a specific keyword in their content.

    Args:
        keyword: The keyword to search for
        doc_path: Path to documentation directory (defaults to DEFAULT_DOC_PATH)

    Returns:
        List of matching file paths
    """
    if doc_path is None:
        doc_path = Path(DEFAULT_DOC_PATH)
    else:
        doc_path = Path(doc_path)

    if not doc_path.exists():
        print(f"Error: Documentation path not found: {doc_path}")
        return []

    matches = []
    for rst_file in doc_path.rglob("*.rst"):
        if search_in_file(keyword, rst_file):
            path_str = str(rst_file.relative_to(doc_path))
            matches.append(path_str)

    return matches


def list_structure(
    doc_path: Union[str, Path, None] = None, max_depth: int = 2
) -> Dict[str, List[str]]:
    """
    List the documentation structure up to a specified depth.

    Args:
        doc_path: Path to documentation directory
        max_depth: Maximum depth to explore (default: 2)

    Returns:
        Dictionary with directories as keys and file lists as values
    """
    if doc_path is None:
        doc_path = Path(DEFAULT_DOC_PATH)
    else:
        doc_path = Path(doc_path)

    if not doc_path.exists():
        print(f"Error: Documentation path not found: {doc_path}")
        return {}

    structure = {}

    for item in doc_path.iterdir():
        if item.is_dir():
            # List files in directory (shallow, only immediate .rst files)
            files = sorted([f.name for f in item.glob("*.rst")])
            structure[item.name] = files

    return structure


def search_in_file(keyword: str, file_path: Union[str, Path]) -> bool:
    """
    Check if a keyword appears in a specific file's content.

    Args:
        keyword: The keyword to search for
        file_path: Path to the file

    Returns:
        True if keyword is found in the file, False otherwise
    """
    file_path = Path(file_path)

    if not file_path.exists():
        return False

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().lower()
            return keyword.lower() in content
    except Exception:
        return False


def get_main_sections(doc_path: Union[str, Path, None] = None) -> List[str]:
    """
    Get the main documentation sections (top-level RST files).

    Args:
        doc_path: Path to documentation directory

    Returns:
        List of main section files
    """
    if doc_path is None:
        doc_path = Path(DEFAULT_DOC_PATH)
    else:
        doc_path = Path(doc_path)

    if not doc_path.exists():
        print(f"Error: Documentation path not found: {doc_path}")
        return []

    main_files = sorted([f.name for f in doc_path.glob("*.rst")])
    return main_files


def print_help():
    """Print usage information."""
    print("""
Odoo Documentation Search Utility

Usage:
    python search_docs.py <command> [arguments]

Commands:
    keyword <keyword>           - Find files by keyword in path/name
    content <keyword>           - Find files by keyword in content
    structure [path]             - List documentation structure (optional path)
    sections [path]              - List main documentation sections (optional path)
    help                        - Show this help message

Examples:
    python search_docs.py keyword installation
    python search_docs.py keyword sales
    python search_docs.py structure
    python search_docs.py sections
    python search_docs.py structure ../../content
""")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print_help()
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "keyword" and len(sys.argv) >= 3:
        keyword = " ".join(sys.argv[2:])
        doc_path_arg = None
        if len(sys.argv) >= 4 and sys.argv[3].endswith("content"):
            doc_path_arg = sys.argv[3]
        results = find_files_by_keyword(keyword, doc_path_arg)
        if results:
            print(f"\nFound {len(results)} file(s) matching '{keyword}':\n")
            for result in results:
                print(f"  - {result}")
        else:
            print(f"\nNo files found matching '{keyword}'")
            print(
                "\nTip: Try broader keywords or check the documentation structure with 'structure' command"
            )

    elif command == "content" and len(sys.argv) >= 3:
        keyword = " ".join(sys.argv[2:])
        doc_path_arg = None
        # Check if the last argument is a path
        if len(sys.argv) >= 4 and sys.argv[-1].endswith("content"):
            doc_path_arg = sys.argv[-1]
            keyword = " ".join(sys.argv[2:-1])

        results = find_files_by_content(keyword, doc_path_arg)
        if results:
            print(f"\nFound {len(results)} file(s) containing '{keyword}':\n")
            for result in results:
                print(f"  - {result}")
        else:
            print(f"\nNo files found containing '{keyword}'")

    elif command == "structure":
        doc_path_arg = sys.argv[2] if len(sys.argv) >= 3 else None
        structure = list_structure(doc_path_arg)
        if structure:
            print("\nDocumentation Structure:\n")
            for section, files in structure.items():
                print(f"  {section}/")
                for file in files:
                    print(f"    - {file}")

    elif command == "sections":
        doc_path_arg = sys.argv[2] if len(sys.argv) >= 3 else None
        sections = get_main_sections(doc_path_arg)
        if sections:
            print("\nMain Documentation Sections:\n")
            for section in sections:
                print(f"  - {section}")

    elif command == "help" or command == "-h" or command == "--help":
        print_help()

    else:
        print(f"Unknown command: {command}")
        print_help()
        sys.exit(1)
