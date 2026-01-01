# Search Patterns

## Overview

This file provides common search patterns and strategies for quickly finding information in the Odoo documentation.

## General Search Strategy

1. **Identify the domain** - Determine if the query is related to:
   - Administration (installation, hosting, upgrades)
   - Applications (user guides, features)
   - Developer (code, modules, framework)
   - Contributing (contributions, documentation)
   - Legal (licenses, terms)

2. **Use domain-specific keywords** - Refer to the appropriate reference file for domain keywords

3. **Narrow down by feature** - Once in the right domain, search for specific features

## Domain Identification

### Administration Queries
Keywords: "install", "setup", "upgrade", "hosting", "server", "database", "deployment"
→ Search in `references/administration.md` and `content/administration/`

### Application Queries
Keywords: "CRM", "sales", "invoicing", "website", "inventory", "HR", "manufacturing"
→ Search in `references/applications.md` and `content/applications/`

### Developer Queries
Keywords: "module", "model", "Python", "JavaScript", "API", "code", "framework", "tutorial"
→ Search in `references/developer.md` and `content/developer/`

### Contributing Queries
Keywords: "contribute", "PR", "pull request", "translation", "documentation", "guidelines"
→ Search in `references/contributing.md` and `content/contributing/`

### Legal Queries
Keywords: "license", "terms", "legal", "CLA", "copyright", "compliance"
→ Search in `references/legal.md` and `content/legal/`

## Common Query Patterns

### Installation & Setup
**Pattern: "How do I install Odoo?"**
1. Check `references/administration.md`
2. Look at installation options: Online, Packages, Source, Docker
3. Navigate to specific installation guide

**Keywords:** install, setup, deployment, get started, first time, new installation

### Configuration
**Pattern: "How do I configure [feature]?"**
1. Identify domain (application or administration)
2. Check application-specific guide in `references/applications.md`
3. Search for "configuration" or "settings"

**Keywords:** configure, settings, setup, preference, option

### Error Troubleshooting
**Pattern: "I'm getting error [error message]"**
1. Identify error type (server, database, module, etc.)
2. Search for error message in developer or administration docs
3. Check upgrade/migration guides if error occurred after upgrade

**Keywords:** error, troubleshooting, issue, problem, fix, resolve

### Feature Documentation
**Pattern: "How does [feature] work?"**
1. Identify which application uses the feature
2. Check `references/applications.md` for the application
3. Navigate to application-specific documentation

**Keywords:** how to, documentation, guide, tutorial, learn, understand

### Development Tasks
**Pattern: "How do I [development task]?"**
1. Check `references/developer.md` for learning path
2. Search for specific task in tutorials or howtos
3. Check reference documentation for API details

**Keywords:** create, develop, module, model, view, widget, component

## Advanced Search Techniques

### Compound Queries
For queries involving multiple domains:
- Example: "How do I create a custom module that integrates with sales?"
- Strategy: Search developer docs for module creation, then application docs for sales integration

### Version-Specific Queries
For queries about specific versions:
- Check `content/administration/standard_extended_support.rst` for version support
- Search for version number in relevant documentation

### Integration Queries
For queries about application integrations:
- Check both application documentation
- Look for integration guides
- Search for "integration" or "connect" keywords

### API Queries
For API-related questions:
- Developer reference: `content/developer/reference/`
- External API: `content/developer/reference/external_api/`
- External RPC API: `content/developer/reference/external_rpc_api/`

## File-Type Specific Searches

### RST Files (.rst)
- Main documentation files
- Use for general documentation queries
- Search for content within these files

### Python Files (.py)
- Code examples and scripts
- Use for implementation details
- Check `content/developer/` directories

### JavaScript Files (.js)
- Frontend code examples
- Use for web framework queries
- Check `content/developer/reference/frontend/`

## Context-Aware Search

### Based on User Role
**Administrator:**
- Focus on administration and application documentation
- Search patterns: installation, configuration, upgrades, backups

**Developer:**
- Focus on developer documentation
- Search patterns: module, API, framework, testing, customization

**End User:**
- Focus on application documentation
- Search patterns: how-to, guide, tutorial, feature explanation

**Contributor:**
- Focus on contributing documentation
- Search patterns: contribute, PR, guidelines, CLA

### Based on Experience Level
**Beginner:**
- Start with tutorials and essential documentation
- Check `content/applications/essentials/`
- Check `content/developer/tutorials/`

**Intermediate:**
- Use how-to guides for specific tasks
- Check `content/developer/howtos/`

**Advanced:**
- Use reference documentation for deep technical details
- Check `content/developer/reference/`

## Quick Reference Mapping

| Query Type | Primary Reference | Backup References |
|------------|-------------------|-------------------|
| Installation | `administration.md` | `developer.md` (setup guide) |
| Features | `applications.md` | Domain-specific app docs |
| Coding | `developer.md` | `structure.md` (file locations) |
| Upgrading | `administration.md` | `developer.md` (upgrade guides) |
| Contributing | `contributing.md` | `developer.md` (for code) |
| Licenses | `legal.md` | `administration.md` (editions) |
| Troubleshooting | Domain-specific | Error context |

## Search Optimization Tips

1. **Start broad, then narrow** - Begin with domain identification, then drill down to specific features

2. **Use multiple search terms** - Combine related keywords for better results

3. **Check file structure** - When unsure, consult `references/structure.md` to understand where information might be located

4. **Look for cross-references** - Documentation often links to related topics; follow these links

5. **Check tables of contents** - RST files use `.. toctree::` directives which show related documentation

6. **Use grep/search tools** - For large documentation sets, use pattern-based search to find relevant files

## Common File Path Patterns

**Administration:**
- Installation: `content/administration/on_premise/*.rst`
- Hosting: `content/administration/odoo_sh/*.rst`
- Upgrades: `content/administration/upgrade.rst`

**Applications:**
- Essentials: `content/applications/essentials/*.rst`
- Specific app: `content/applications/[app-name]/*.rst`

**Developer:**
- Tutorials: `content/developer/tutorials/[topic]/*.rst`
- How-tos: `content/developer/howtos/[topic].rst`
- Reference: `content/developer/reference/[topic]/*.rst`

**Contributing:**
- Code contribution: `content/contributing/development.rst`
- Documentation: `content/contributing/documentation.rst`

**Legal:**
- Licenses: `content/legal/licenses/*`
- Terms: `content/legal/terms/*`
- Main: `content/legal/*.rst`
