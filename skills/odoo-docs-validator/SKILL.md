---
name: odoo-docs-validator
description: Automated style and structure validation for Odoo documentation. Use when creating or modifying RST files to ensure compliance with Odoo's heading hierarchy, line length limits, image metadata requirements, and UI element formatting rules. This skill provides a validation script and a comprehensive rule reference for maintaining documentation quality.
---

# Odoo Documentation Validator

Validate your documentation changes against Odoo's official style and structural guidelines.

## Quick Start

### Validate a File
Run the validation script on your modified RST file:

```bash
python3 scripts/validate_docs.py <path_to_rst_file>
```

The script checks for:
- **H1 Headings:** Ensures exactly one H1 per page.
- **Line Length:** Flags lines exceeding 100 characters.
- **Image Metadata:** Verifies the presence of `:alt:` tags.

### Consult the Rules
For a detailed breakdown of all documentation standards (including those not yet automated), refer to:
- `references/rules.md` - Complete Odoo documentation rule set.

## Common Validation Errors

| Error | Fix |
| :--- | :--- |
| "Line exceeds 100 characters" | Break the line at a space. RST handles line breaks without forcing them in HTML. |
| "Missing :alt: tag" | Add `:alt: Description of the image` below the `.. image::` directive. |
| "Incorrect H1 heading" | Ensure the title is both overlined and underlined with `=`. |

## Resources

### scripts/
- `validate_docs.py` - CLI tool for checking RST files.

### references/
- `rules.md` - Detailed style guide and structural rules.
