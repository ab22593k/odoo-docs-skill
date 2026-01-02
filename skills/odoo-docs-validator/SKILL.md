---
name: odoo-docs-validator
description: Automated style and structure validation for Odoo documentation. Use when creating or modifying RST files to ensure compliance with Odoo's heading hierarchy, line length limits, image metadata requirements, and UI element formatting rules. This skill provides validation scripts and a comprehensive rule reference for maintaining documentation quality.
---

# Odoo Documentation Validator

Validate and automatically fix documentation changes against Odoo's official style and structural guidelines.

## Quick Start

### Validate and Fix a File
Run the validation script on your modified RST file. Use `--fix` to automatically correct common issues like heading lengths and trailing whitespace.

```bash
# Basic validation
python3 scripts/validate_docs.py <path_to_rst_file>

# Validation with auto-fix
python3 scripts/validate_docs.py <path_to_rst_file> --fix

# Recursive validation on a directory
python3 scripts/validate_docs.py content/applications/sales/ -r
```

### Check Internal Links
Verify that all `:ref:` and `:doc:` links target valid existing resources.

```bash
python3 scripts/check_links.py <path_to_check>
```

## Features

### `validate_docs.py`
- **H1 Headings:** Ensures exactly one H1 per page, properly overlined and underlined.
- **Heading Hierarchy:** Validates the correct order of symbols (`=`, `-`, `~`, `*`, `^`).
- **Delimiter Length:** Ensures underlines match the heading text length (Auto-fixable).
- **Line Length:** Flags lines exceeding 100 characters (excluding URLs).
- **Image Metadata:** Verifies the presence of `:alt:` tags and correct folder structure.
- **Cleanliness:** Detects tabs, trailing whitespace (Auto-fixable), and Git conflict markers.

### `check_links.py`
- **Reference Check:** Validates `:ref:` targets against all explicit labels in the project.
- **Document Check:** Validates `:doc:` paths against existing RST files, handling both absolute and relative paths.

## Resources

### scripts/
- `validate_docs.py` - CLI tool for style and structure validation.
- `check_links.py` - CLI tool for internal link verification.

### references/
- `rules.md` - Detailed style guide and structural rules.
