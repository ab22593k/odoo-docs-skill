# Developer Reference

## Overview

The developer section provides technical documentation for Odoo development, including tutorials, how-to guides, and reference materials.

## Structure

The developer documentation is organized into three main sections:
- **Tutorials** - Hands-on learning exercises for beginners
- **How-to guides** - Step-by-step guides for specific development tasks
- **Reference** - Technical API and framework documentation

## Learning Path

### For New Developers

1. **Start with the Setup Guide**
   - Location: `content/developer/tutorials/setup_guide`
   - Prerequisites and environment setup

2. **Server Framework Basics**
   - Location: `content/developer/tutorials/server_framework_101`
   - Essential server framework concepts
   - Create a simple module from scratch

3. **Web Framework Introduction**
   - Location: `content/developer/tutorials/discover_js_framework`
   - Basic web framework concepts
   - Working with Owl components

4. **Advanced Topics**
   - Master web framework: `content/developer/tutorials/master_odoo_web_framework`
   - Module data: `content/developer/tutorials/define_module_data`
   - Security: `content/developer/tutorials/restrict_data_access`
   - Testing: `content/developer/tutorials/unit_tests`

## Tutorials (`content/developer/tutorials/`)

Hands-on learning exercises.

### Beginner Tutorials
- **setup_guide** - Environment setup and prerequisites
- **server_framework_101** - Server framework fundamentals, create a module
- **discover_js_framework** - Web framework basics, Owl components
- **define_module_data** - Master and demo data using CSV and XML
- **restrict_data_access** - Security: groups, access rights, record rules
- **unit_tests** - Python unit testing

### Intermediate Tutorials
- **importable_modules** - Data-only modules (no code, just data files)
- **mixins** - Code reusability across models
- **pdf_reports** - QWeb templating for PDF reports
- **website_theme** - Custom website themes

### Advanced Tutorials
- **master_odoo_web_framework** - Advanced web framework topics

## How-to Guides (`content/developer/howtos/`)

Practical guides for specific development tasks.

### Frontend Development

**CSS & Styling:**
- **scss_tips** - Lean, maintainable CSS: `scss_tips.rst`

**JavaScript Framework:**
- **javascript_field** - Customize field components: `javascript_field.rst`
- **javascript_view** - Customize view types: `javascript_view.rst`
- **javascript_client_action** - Create client actions: `javascript_client_action.rst`

**Owl Components:**
- **standalone_owl_application** - Public-facing Owl app: `standalone_owl_application.rst`
- **frontend_owl_components** - Owl on portal/website: `frontend_owl_components.rst`

**Website Themes:**
- **website_themes** - Custom website themes: `website_themes/` (subdirectory)

### Server-Side Development

**Multi-Company:**
- **company** - Multi-company management: `company.rst`

**Reports:**
- **create_reports** - Custom reports with SQL Views: `create_reports.rst`

**Localization:**
- **accounting_localization** - Localization modules: `accounting_localization/` (subdirectory)

**Translations:**
- **translations** - Module translation: `translations/` (subdirectory)

**IoT:**
- **connect_device** - Device communication: `connect_device.rst`

### Custom Development

**Upgrades:**
- **upgrade_custom_db** - Upgrade customized databases and modules: `upgrade_custom_db.rst`

## Reference Documentation (`content/developer/reference/`)

Technical API and framework reference.

### Core Reference
- **backend/** - Backend API and framework
- **frontend/** - Frontend API (JavaScript, Owl)
- **user_interface/** - UI components and widgets
- **standard_modules/** - Standard module documentation

### Tools & APIs
- **cli/** - Command-line interface reference
- **upgrades/** - Upgrade API
- **external_api/** - External API documentation
- **external_rpc_api/** - External RPC API
- **extract_api/** - Extract API

### Glossary
- **glossary.rst** - Development terminology and concepts

## Common Use Cases

### Creating a New Module
1. Setup: `content/developer/tutorials/setup_guide`
2. Basics: `content/developer/tutorials/server_framework_101`
3. Data: `content/developer/tutorials/define_module_data`
4. Security: `content/developer/tutorials/restrict_data_access`
5. Testing: `content/developer/tutorials/unit_tests`

### Customizing the Web Interface
1. Fields: `content/developer/howtos/javascript_field.rst`
2. Views: `content/developer/howtos/javascript_view.rst`
3. Client actions: `content/developer/howtos/javascript_client_action.rst`
4. Advanced: `content/developer/tutorials/master_odoo_web_framework`

### Creating Reports
1. PDF reports: `content/developer/tutorials/pdf_reports`
2. Custom reports: `content/developer/howtos/create_reports.rst`

### Creating Website Themes
1. Theme tutorial: `content/developer/tutorials/website_theme`
2. Advanced theming: `content/developer/howtos/website_themes/`

### Working with Data
1. Module data: `content/developer/tutorials/define_module_data`
2. Importable modules: `content/developer/tutorials/importable_modules`
3. Multi-company: `content/developer/howtos/company.rst`

### Security & Access Control
1. Security basics: `content/developer/tutorials/restrict_data_access`
2. Reference: `content/developer/reference/backend/` (security section)

### Localization & Translation
1. Localization: `content/developer/howtos/accounting_localization/`
2. Translation: `content/developer/howtos/translations/`

## Search Patterns

### By Development Phase
- **Getting started**: "setup", "environment", "prerequisites"
- **Module creation**: "module", "model", "manifest"
- **Frontend**: "javascript", "owl", "widget", "view", "field"
- **Backend**: "api", "model", "method", "compute", "onchange"
- **Testing**: "test", "unittest", "assert"
- **Deployment**: "upgrade", "migration", "deployment"

### By Technology
- **Python**: "python", "model", "orm", "api", "decorator"
- **JavaScript/Owl**: "javascript", "owl", "component", "state", "props"
- **QWeb/XML**: "qweb", "xml", "template", "report", "view"
- **SQL**: "sql", "query", "database", "view"
- **CSS/SCSS**: "css", "scss", "style", "theme"

### By Feature
- **Reports**: "report", "pdf", "qweb", "print"
- **Access control**: "access", "security", "groups", "rules", "record"
- **Multi-company**: "multi-company", "company", "inter-company"
- **IoT**: "device", "iot", "hardware"
- **Web**: "website", "theme", "eCommerce", "portal"

### By Difficulty
- **Beginner**: Tutorial files in `content/developer/tutorials/`
- **Intermediate**: How-to guides in `content/developer/howtos/`
- **Advanced**: Reference documentation in `content/developer/reference/` and advanced tutorials

## File Structure

```
content/developer/
├── glossary.rst
├── howtos.rst
├── reference.rst
├── tutorials.rst
├── howtos/
│   ├── accounting_localization/
│   ├── translations/
│   ├── website_themes/
│   ├── accounting_localization.rst
│   ├── company.rst
│   ├── connect_device.rst
│   ├── create_reports.rst
│   ├── frontend_owl_components.rst
│   ├── javascript_client_action.rst
│   ├── javascript_field.rst
│   ├── javascript_view.rst
│   ├── scss_tips.rst
│   ├── standalone_owl_application.rst
│   ├── translations.rst
│   ├── upgrade_custom_db.rst
│   └── website_themes.rst
├── reference/
│   ├── backend/
│   ├── external_api/
│   ├── external_rpc_api/
│   ├── extract_api/
│   ├── frontend/
│   ├── standard_modules/
│   ├── upgrades/
│   └── user_interface/
└── tutorials/
    ├── define_module_data/
    ├── discover_js_framework/
    ├── importable_modules/
    ├── master_odoo_web_framework/
    ├── mixins/
    ├── pdf_reports/
    ├── restrict_data_access/
    ├── server_framework_101/
    ├── setup_guide/
    ├── unit_tests/
    └── website_theme/
```

## Key Concepts

### Odoo Framework
- **Server Framework**: Python-based ORM and business logic
- **Web Framework**: JavaScript-based UI built on Owl
- **Module System**: Modular architecture for extending functionality

### Development Tools
- **Odoo.sh**: Development and hosting platform
- **Odoo Bin**: Command-line tool for local development
- **Sphinx**: Documentation generation

### Common Patterns
- **Model-View-Controller**: Separation of concerns
- **Record Rules**: Data-level access control
- **Groups/Permissions**: Feature-level access control
- **Mixins**: Reusable code components
- **Computed Fields**: Automatic value calculation
- **Onchange Methods**: Dynamic field updates
