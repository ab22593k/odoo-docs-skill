# Odoo Custom RST Directives

This reference catalogues custom reStructuredText (RST) directives available in the Odoo documentation environment.

## Layout & Navigation

### `cards` and `card`
Used to create grid-based navigation elements.
- **Container:** `.. cards::`
- **Item:** `.. card:: Title`
  - `:target:` (required): Path to the target document (without `.rst`).
  - `:tag:` (optional): Small badge text.
  - `:large:` (flag): Makes the card take more space.

**Example:**
```rst
.. cards::

   .. card:: Getting Started
      :target: setup/install
      :tag: Beginner

      Learn how to install Odoo on your machine.
```

## Content Highlighting

### `spoiler`
An accordion-style collapsible block.
- **Argument:** (Optional) The label for the spoiler button.
- **Content:** The hidden content.

**Example:**
```rst
.. spoiler:: Click to see the answer

   The answer is 42.
```

### `example` and `exercise`
Themed admonitions for pedagogical content.

**Example:**
```rst
.. example::
   This is a practical example of the feature.

.. exercise::
   Try to configure the tax as described above.
```

## Multimedia

### `youtube` and `vimeo`
Embed video players.
- **Argument:** Video ID.
- **Options:** `:height:`, `:width:`, `:align:` (left, center, right).

**Example:**
```rst
.. youtube:: anwy2MPT5RE
    :width: 500
    :align: center
```

## Roles

### `:dfn:`
Used for defining terms. Renders with a custom "dotted" underline style.

**Example:**
```rst
A :dfn:`Sales Order` is a contract between a seller and a buyer.
```

### `:abbr:`
Used for abbreviations with tooltips.

**Example:**
```rst
Odoo uses :abbr:`OCR (Optical Character Recognition)` for invoices.
```
