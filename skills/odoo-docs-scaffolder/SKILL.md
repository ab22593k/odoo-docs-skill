---
name: odoo-docs-scaffolder
description: Streamlines creation of new Odoo documentation pages using standard templates. Use when starting a new documentation page, tutorial, or API reference to ensure correct initial structure, metadata, and media folder organization.
---

# Odoo Documentation Scaffolder

Quickly generate new documentation pages with standardized structure and associated media folders.

## Quick Start

### Scaffold a New Page
Run the scaffolding script with the target path and optional template name.

```bash
# Create a standard application page
python3 scripts/scaffold.py content/applications/sales/my_new_feature.rst

# Create a developer tutorial
python3 scripts/scaffold.py content/developer/tutorials/my_tutorial.rst tutorial.rst

# Create an API reference
python3 scripts/scaffold.py content/developer/reference/my_api.rst api_reference.rst
```

The script will:
1.  **Copy the template** to the target path.
2.  **Create a media folder** with the same name as the RST file (e.g., `content/applications/sales/my_new_feature/`).
3.  **Ensure correct metadata** (like `:show-content:`) is included.

## Available Templates

- `standard_page.rst`: Default template for general documentation.
- `tutorial.rst`: Structured for step-by-step learning.
- `api_reference.rst`: Template for documenting technical code and models.

## Resources

### scripts/
- `scaffold.py`: Main utility for creating pages and folders.

### assets/templates/
- Collection of `.rst` boilerplates.
