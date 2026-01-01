# Applications Reference

## Overview

The applications section provides user documentation organized by business application. Each application contains user guides, configuration tutorials, and feature explanations.

## Main Categories

### 1. Essentials (`content/applications/essentials/`)

Core functionality used across all Odoo applications.

**Topics:**
- **Activities** - Activity tracking and management: `activities/`
- **Contacts** - Contact management: `contacts/`
- **Data Export/Import** - Data transfer: `export_import_data/`
- **HTML Editor** - Rich text editing: `html_editor/`
- **In-App Purchase** - Purchasing within Odoo: `in_app_purchase/`
- **Keyboard Shortcuts** - Productivity shortcuts: `keyboard_shortcuts.rst`
- **Property Fields** - Dynamic properties: `property_fields.rst`
- **Reporting** - General reporting features: `reporting/`
- **Search** - Advanced search capabilities: `search/`
- **Stages** - Stage/kanban management: `stages/`

**Use when:** Users need help with basic Odoo features that apply across multiple apps.

### 2. Finance (`content/applications/finance/`)

Financial management and accounting features.

**Use when:** Queries about accounting, invoicing, payments, financial reporting.

### 3. Sales (`content/applications/sales/`)

Sales process and customer relationship management.

**Use when:** Queries about sales orders, quotations, CRM, invoicing.

### 4. Websites (`content/applications/websites/`)

Website building and management tools.

**Use when:** Queries about website builder, themes, eCommerce, blog.

### 5. Inventory & MRP (`content/applications/inventory_and_mrp/`)

Inventory management and manufacturing operations.

**Use when:** Queries about stock, warehouses, manufacturing, bills of materials.

### 6. HR (`content/applications/hr/`)

Human resources and employee management.

**Use when:** Queries about employees, recruitment, leaves, payroll, time tracking.

### 7. Marketing (`content/applications/marketing/`)

Marketing and campaign management.

**Use when:** Queries about email marketing, campaigns, mass mailing.

### 8. Services (`content/applications/services/`)

Service-oriented applications.

**Use when:** Queries about services, projects, helpdesk, field service.

### 9. Productivity (`content/applications/productivity/`)

Productivity-enhancing applications.

**Use when:** Queries about calendars, notes, discussions, automation.

### 10. Studio (`content/applications/studio/`)

Studio customization tool.

**Use when:** Queries about customizing apps without coding.

### 11. General (`content/applications/general/`)

General features and settings.

**Use when:** Queries about system-wide settings, configurations.

## Common Use Cases

### Finding application-specific help
1. Identify the relevant application category
2. Navigate to the subdirectory
3. Search for specific feature documentation

### Learning core Odoo features
Start with `content/applications/essentials/` for foundational knowledge.

### Understanding a specific business process
1. Identify which applications are involved
2. Cross-reference between application documentation
3. Check for integration guides

## Search Patterns

### By Application Type
- **Essentials**: "activities", "contacts", "search", "export", "import"
- **Finance**: "accounting", "invoice", "payment", "chart of accounts"
- **Sales**: "sales order", "CRM", "customer", "quotation"
- **Websites**: "website", "eCommerce", "blog", "theme"
- **Inventory**: "stock", "warehouse", "inventory", "manufacturing"
- **HR**: "employee", "recruitment", "leave", "timesheet", "payroll"
- **Marketing**: "campaign", "email", "marketing", "automation"
- **Services**: "project", "helpdesk", "field service"
- **Productivity**: "calendar", "note", "automation", "integration"
- **Studio**: "studio", "customize", "app builder"
- **General**: "settings", "configuration", "user preferences"

### By Feature Type
- **Reporting**: Search in relevant application directory + "reporting"
- **Configuration**: Search in relevant application directory + "configuration"
- **Integration**: Check multiple application directories
- **Setup**: Start with essentials, then application-specific setup

### By User Level
- **Beginner**: Start with essentials and general documentation
- **Intermediate**: Application-specific guides
- **Advanced**: Complex workflows and integrations

## File Structure

```
content/applications/
├── essentials.rst
├── finance.rst
├── general.rst
├── hr.rst
├── inventory_and_mrp.rst
├── marketing.rst
├── productivity.rst
├── sales.rst
├── services.rst
├── studio.rst
├── websites.rst
├── essentials/
├── finance/
├── general/
├── hr/
├── inventory_and_mrp/
├── marketing/
├── productivity/
├── sales/
├── services/
├── studio/
└── websites/
```

## Cross-Application Topics

Some features span multiple applications:
- **Reporting**: Many applications have specific reporting features
- **Automation**: Workflow automation may be configured in multiple places
- **Integration**: Applications integrate with each other; check multiple sources
- **Settings**: System-wide settings may affect multiple applications
