# Odoo Documentation Structure

## Overview

The Odoo documentation is organized as a Sphinx-based RST (reStructuredText) documentation tree located at `content/`.

## Top-Level Structure

```
content/
├── index.rst                 # Main documentation index
├── administration.rst        # Database management & installation
├── applications.rst          # User documentation by application
├── developer.rst             # Developer documentation
├── contributing.rst          # Contributing guidelines
└── legal.rst                 # Legal information
```

## Main Sections

### Administration (`content/administration/`)

Focuses on database management, installation, and maintenance.

**Sub-directories:**
- `odoo_accounts/` - Odoo account management
- `odoo_sh/` - Odoo.sh platform
- `on_premise/` - On-premise installation (packages, source, Docker)
- `upgrade/` - Database upgrades

**Key files:**
- `hosting.rst` - Hosting options
- `odoo_online.rst` - Odoo online platform
- `mobile.rst` - Mobile access
- `neutralized_database.rst` - Database neutralization
- `standard_extended_support.rst` - Version support information

### Applications (`content/applications/`)

User documentation organized by business application.

**Sub-directories:**
- `essentials/` - Core functionality (contacts, activities, search, reporting, etc.)
- `finance/` - Financial management
- `general/` - General features
- `hr/` - Human resources
- `inventory_and_mrp/` - Inventory and manufacturing
- `marketing/` - Marketing tools
- `productivity/` - Productivity apps
- `sales/` - Sales management
- `services/` - Service management
- `studio/` - Studio customization
- `websites/` - Website builder

Each application sub-directory contains `.rst` files for specific features and functionality.

### Developer (`content/developer/`)

Technical documentation for Odoo development.

**Sub-directories:**
- `tutorials/` - Hands-on tutorials for learning development
- `howtos/` - Step-by-step guides for specific tasks
- `reference/` - Technical reference materials

**Key files:**
- `glossary.rst` - Development terminology

#### Tutorials (`content/developer/tutorials/`)

Hands-on learning exercises organized by topic:
- `setup_guide` - Getting started
- `server_framework_101` - Server framework basics
- `discover_js_framework` - Web framework intro
- `master_odoo_web_framework` - Advanced web framework
- `define_module_data` - Module data definition
- `restrict_data_access` - Security and access control
- `unit_tests` - Unit testing
- `importable_modules` - Data-only modules
- `mixins` - Code reusability
- `pdf_reports` - PDF report creation
- `website_theme` - Website theme development

#### How-tos (`content/developer/howtos/`)

Practical guides for specific development tasks:
- Frontend development: CSS, JavaScript fields/views/client actions, Owl components, website themes
- Server-side development: Multi-company, reports, accounting localization, translations, device connectivity
- Custom development: Upgrading customized databases

**Sub-directories for complex topics:**
- `accounting_localization/`
- `translations/`
- `website_themes/`

#### Reference (`content/developer/reference/`)

Technical reference documentation:
- `backend/` - Backend API
- `frontend/` - Frontend API
- `user_interface/` - UI components
- `standard_modules/` - Standard module documentation
- `cli/` - Command-line interface
- `upgrades/` - Upgrade API
- `external_api/` - External API
- `external_rpc_api/` - External RPC API
- `extract_api/` - Extract API

### Contributing (`content/contributing/`)

Guidelines for contributing to Odoo.

**Sub-directories:**
- `development/` - Code contribution
- `documentation/` - Documentation contribution

### Legal (`content/legal/`)

Legal information including licenses, terms, and policies.

## Documentation Files

The documentation uses RST (reStructuredText) format with Sphinx extensions. Key RST directives used:
- `.. toctree::` - Table of contents for linking pages
- `.. cards::` - Card-based layout for related content
- `.. seealso::` - Cross-references to related documentation
- `:nosearch:`, `:show-content:`, `:hide-page-toc:`, `:show-toc:` - Page-level options

## Additional Resources

- `locale/` - Translations in multiple languages
- `redirects/` - Redirect rules for version migration
- `extensions/` - Custom Sphinx extensions
- `static/` - Static assets (CSS, JS, images)
- `invs/` - Inventory files for search
