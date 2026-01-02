# Odoo UI Element Guidelines

Use these roles to maintain consistency when referring to Odoo's user interface.

## Menu Selections

### `:menuselection:`
Used for navigating through Odoo's menu hierarchy.
- **Rule:** Start with the App name.
- **Rule:** Use `-->` as a separator.
- **Rule:** Do NOT include menu section headers (static text in the menu).

**Example:**
- **Correct:** `:menuselection:`Accounting --> Customers --> Invoices`
- **Incorrect:** `:menuselection:`Accounting --> Journals --> Invoices` (Journals is a section header).

## Interface Elements

### `:guilabel:`
Used for buttons, fields, tabs, and specific UI options.
- **Rule:** Matches the text exactly as it appears in the software.
- **Rule:** Use Sentence Case if the software uses ALL CAPS.
- **Rule:** Avoid using for general concepts (e.g., use for the "Save" button, but not for the "Invoice" record).

**Example:**
- `Click :guilabel:`Confirm` to validate the order.`
- `In the :guilabel:`Payment Terms` field, select 'Immediate Payment'.`

## Icons

### `:icon:`
Used to display an icon next to its label.
- **Rule:** Always follow with the label in brackets using `:guilabel:`.

**Example:**
- `:icon:`fa-bug` :guilabel:`(bug)` icon.`
- `:icon:`oi-view-pivot` :guilabel:`(pivot table)` icon.`

## Summary Table

| Element Type | Role | Example |
| :--- | :--- | :--- |
| Main App / Menu | `:menuselection:` | `:menuselection:`Sales --> Products` |
| Button / Field | `:guilabel:` | `:guilabel:`Create` |
| UI Icon | `:icon:` | `:icon:`fa-check` |
| Technical Value | `literal` (backticks) | `Set the value to `0.00`.` |
