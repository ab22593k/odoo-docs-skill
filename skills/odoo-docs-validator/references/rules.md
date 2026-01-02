# Odoo Documentation Validation Rules

This reference outlines the specific rules enforced by the `odoo-docs-validator`.

## Structural Rules

### Headings
- **H1:** Exactly one H1 per document. Format: Overlined and underlined with `=` (e.g., `=======`).
- **Hierarchy:**
  - H2: Underlined with `=`
  - H3: Underlined with `-`
  - H4: Underlined with `~`
  - H5: Underlined with `*`
  - H6: Underlined with `^`

### Toctree
- All RST files in a directory must be listed in a `toctree` in the parent or index page, unless marked with `:orphan:`.

## Formatting Rules

### Line Length
- Maximum 100 characters per line.
- Exceptions: Long URLs or specific technical blocks where wrapping breaks functionality.

### Indentation
- Use spaces only (no tabs).
- Align indented lines with the first character of the markup above (usually 3 spaces).
- Bulleted lists use 2 spaces for alignment.

## Content Guidelines

### Images
- Must include an `:alt:` tag.
- Should be stored in a subfolder named after the RST file.
- Filenames must be lower-case, descriptive, and hyphen-separated.

### Tone & Style
- Use American English.
- Prefer imperative mood (e.g., "Select..." instead of "You can select...").
- Titles should be concise and use sentence case.
- Avoid "How to" in titles.

## UI Elements
- Use `:guilabel:` for buttons and fields.
- Use `:menuselection:` for menu paths.
- Follow icons with a bracketed label: `:icon:`fa-bug` :guilabel:`(bug)``.
