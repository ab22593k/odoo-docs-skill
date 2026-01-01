---
name: odoo-docs
description: Comprehensive reference for LLM agents to navigate and work with Odoo documentation. Use when working with Odoo-related documentation tasks like finding installation guides, locating application documentation, searching developer tutorials/reference materials, understanding documentation structure, and assisting with queries about Odoo features, development, and maintenance. This skill provides organized domain-based references and search strategies for efficiently locating information across the entire Odoo documentation tree.
---

# Odoo Documentation Reference

## Overview

Navigate and search the Odoo documentation efficiently. The documentation is organized into five main domains: Administration, Applications, Developer, Contributing, and Legal. Each domain has dedicated reference files with detailed structure, search patterns, and common use cases.

## Quick Start

### Identify the Domain

Determine which domain your query relates to:

| Domain | When to Use |
|--------|--------------|
| **Administration** | Installation, hosting, upgrades, database management, Odoo.sh |
| **Applications** | User guides, feature documentation, app-specific functionality |
| **Developer** | Tutorials, API references, module development, framework guides |
| **Contributing** | Code contributions, documentation contributions, CLA, guidelines |
| **Legal** | Licenses, terms, legal agreements, compliance |

### Use the Search Tool

For quick file searches:

```bash
python3 scripts/search_docs.py keyword <keyword>
```

Examples:
- `python3 scripts/search_docs.py keyword install`
- `python3 scripts/search_docs.py keyword sales`
- `python3 scripts/search_docs.py keyword module`

### Use Domain-Specific References

Load the appropriate reference file for detailed guidance:
- `references/structure.md` - Complete documentation structure and organization
- `references/administration.md` - Database management, installation, hosting
- `references/applications.md` - Business applications and user guides
- `references/developer.md` - Development tutorials, howtos, reference
- `references/contributing.md` - Contribution guidelines
- `references/legal.md` - Licenses, terms, legal information
- `references/search_patterns.md` - Advanced search strategies

## Common Query Patterns

### Installation & Setup
**Query:** "How do I install Odoo?"

1. Load `references/administration.md`
2. Review installation options (Online, Packages, Source, Docker)
3. Navigate to specific installation guide

**Keywords:** install, setup, deployment, get started

### Feature Documentation
**Query:** "How does [feature] work?"

1. Load `references/applications.md`
2. Identify relevant application category
3. Navigate to application-specific documentation

**Keywords:** how to, documentation, guide, tutorial

### Development Tasks
**Query:** "How do I create a custom module?"

1. Load `references/developer.md`
2. Check learning path section
3. Navigate to tutorials and howtos

**Keywords:** module, model, Python, JavaScript, API, framework

### Upgrading Odoo
**Query:** "How do I upgrade my Odoo installation?"

1. Load `references/administration.md`
2. Search for upgrade documentation
3. Check version support information

**Keywords:** upgrade, migration, version, update

## Documentation Navigation Strategy

### Level 1: Domain Identification
Use `references/search_patterns.md` to identify which domain contains the information you need.

### Level 2: Domain Reference
Load the domain-specific reference file (`references/administration.md`, `references/applications.md`, etc.) to understand the structure and available topics.

### Level 3: Specific Location
Use the file paths and search patterns in the reference files to locate the exact documentation.

### Level 4: Script Search
Use `scripts/search_docs.py` for keyword-based file discovery when specific locations aren't known.

## File Search Tool

Use `scripts/search_docs.py` to search documentation:

```bash
# Find files by keyword
python3 scripts/search_docs.py keyword <keyword>

# List documentation structure
python3 scripts/search_docs.py structure

# List main sections
python3 scripts/search_docs.py sections

# Show help
python3 scripts/search_docs.py help
```

The script searches for keywords in file paths and names, providing matching file locations.

## Reference Files by Domain

### Structure (`references/structure.md`)
Complete documentation tree organization, file structure, and RST directives. Use this to understand the overall documentation layout.

### Administration (`references/administration.md`)
Installation methods, hosting options, database management, upgrades, Odoo accounts, and version support. Essential for system administrators and DevOps tasks.

### Applications (`references/applications.md`)
User documentation organized by business application (finance, HR, sales, websites, etc.). Use this to find feature guides and configuration tutorials.

### Developer (`references/developer.md`)
Complete learning path for developers, including tutorials, how-to guides, and API reference materials. Covers server framework, web framework, testing, and advanced development topics.

### Contributing (`references/contributing.md`)
Guidelines for contributing code and documentation to Odoo. Includes CLA information, contribution workflows, and community guidelines.

### Legal (`references/legal.md`)
Licensing information, terms of service, and legal documentation. Use this to understand Odoo Community vs Enterprise licensing and legal requirements.

### Search Patterns (`references/search_patterns.md`)
Advanced search strategies, domain identification techniques, and query optimization tips. Use this when having trouble finding specific information.

## Domain-Based Search Strategies

### For Beginners
1. Start with `references/applications.md` for user guides
2. Use `references/developer.md` tutorials for development
3. Check `references/search_patterns.md` for search strategies

### For Developers
1. Load `references/developer.md` for API and framework information
2. Use `scripts/search_docs.py keyword <api/term>` for API searches
3. Check `references/structure.md` for file locations

### For Administrators
1. Load `references/administration.md` for installation and hosting
2. Use `scripts/search_docs.py keyword <term>` for specific operations
3. Check upgrade and maintenance sections

### For Contributors
1. Load `references/contributing.md` for contribution guidelines
2. Review CLA and code of conduct in `references/legal.md`
3. Use `references/developer.md` for technical contribution context

## Working with RST Files

The Odoo documentation uses reStructuredText (RST) format. Key RST directives:

- `.. toctree::` - Table of contents for linking pages
- `.. cards::` - Card-based layout for related content
- `.. seealso::` - Cross-references to related documentation
- `:nosearch:`, `:show-content:`, `:hide-page-toc:`, `:show-toc:` - Page-level options

When reading RST files:
1. Look for `.. toctree::` directives to see related pages
2. Check `.. cards::` sections for overview of topics
3. Follow `.. seealso::` links for additional information

## Resources

### scripts/
Executable code for documentation search and exploration:
- `search_docs.py` - Search and explore documentation structure

### references/
Domain-specific reference documentation:
- `structure.md` - Complete documentation structure
- `administration.md` - Administration domain reference
- `applications.md` - Applications domain reference
- `developer.md` - Developer domain reference
- `contributing.md` - Contributing guidelines
- `legal.md` - Legal information
- `search_patterns.md` - Search strategies and patterns

### assets/
None required for this reference skill.
