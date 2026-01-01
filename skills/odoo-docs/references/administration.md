# Administration Reference

## Overview

The administration section covers database management, installation, hosting, and maintenance of Odoo systems.

## Installation Options

### Odoo Online
- Easiest way to use Odoo in production
- No installation required
- Location: `content/administration/odoo_online.rst`

### Packaged Installers
- Suitable for testing and development
- Can be used for production with additional deployment work
- Location: `content/administration/on_premise/packages/`

### Source Install
- Greater flexibility
- Allows running multiple Odoo versions on same system
- Suitable for development and production deployment
- Location: `content/administration/on_premise/source/`

### Docker
- Base image available for development and deployment
- URL: https://hub.docker.com/_/odoo/

## Key Topics

### Database Management

**Installation methods:**
- Packaged installers guide: `content/administration/on_premise/packages.rst`
- Source install guide: `content/administration/on_premise/source.rst`
- Docker usage: External Docker Hub documentation

**Upgrades:**
- General upgrade process: `content/administration/upgrade.rst`
- Upgrading customized databases: `content/developer/howtos/upgrade_custom_db.rst`

**Database operations:**
- Neutralized databases: `content/administration/neutralized_database.rst`

### Hosting

- Hosting options overview: `content/administration/hosting.rst`
- Odoo.sh platform: `content/administration/odoo_sh/` (multiple files)
- On-premise hosting: `content/administration/on_premise/`

### Odoo Accounts

- Account management: `content/administration/odoo_accounts.rst`
- Subdirectory: `content/administration/odoo_accounts/`

### Versions and Support

- Standard and extended support: `content/administration/standard_extended_support.rst`

### Mobile

- Mobile access: `content/administration/mobile.rst`

## Editions

### Odoo Community
- Free and open-source
- Licensed under GNU LGPLv3
- Core of Odoo Enterprise

### Odoo Enterprise
- Shared source version
- More functionalities
- Functional support included
- Upgrades included
- Hosting included
- Pricing starts from one app free

### Switching Editions

- Switch from Community to Enterprise: `content/administration/on_premise/community_to_enterprise.rst`
- Note: Not available for source install

## Common Use Cases

### Setting up Odoo for the first time
1. Choose installation method (Online, Packages, Source, Docker)
2. Follow relevant installation guide
3. Configure Odoo account if needed

### Upgrading Odoo
1. Check version support: `content/administration/standard_extended_support.rst`
2. Follow upgrade guide: `content/administration/upgrade.rst`
3. For custom modules, see: `content/developer/howtos/upgrade_custom_db.rst`

### Hosting on Odoo.sh
1. Review Odoo.sh documentation: `content/administration/odoo_sh.rst`
2. Explore Odoo.sh subdirectory for specific topics

### Database maintenance
1. Database management guides in `content/administration/odoo_sh/`
2. Neutralized database: `content/administration/neutralized_database.rst`

## File Structure

```
content/administration/
├── hosting.rst
├── mobile.rst
├── neutralized_database.rst
├── odoo_accounts.rst
├── odoo_online.rst
├── odoo_sh.rst
├── on_premise.rst
├── standard_extended_support.rst
├── upgrade.rst
├── odoo_accounts/
├── odoo_sh/
└── on_premise/
```

## Search Patterns

For installation-related queries:
- Keywords: "install", "setup", "deployment", "package", "source", "docker"

For upgrade-related queries:
- Keywords: "upgrade", "migration", "version", "update"

For hosting-related queries:
- Keywords: "hosting", "server", "deployment", "cloud", "on-premise"

For database management:
- Keywords: "database", "backup", "restore", "neutralized", "db"
