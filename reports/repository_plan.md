---
title: "Repository Plan"
summary: "Long-term architecture and maintenance plan for the Xetta Web AppSec Field Manual."
tags:
  - report
  - migration
related_topics:
  - "Repository Migration"
references:
---
# Repository Plan

## Repository Name

Recommended project name: `xetta-web-appsec-field-manual`.

This is clearer than the original export name because it communicates the repository's purpose: a practical, maintained field manual for web application security work, not a raw Notion dump or a generic pentesting folder.

## Target Structure

```text
.
├── README.md
├── methodology/
├── recon/
├── vulnerabilities/
├── tooling/
├── resources/
├── code-review/
├── assets/
│   └── images/
├── reports/
└── source-archive/
    └── notion-export/
```

## Maintenance Model

- Canonical content lives in semantic folders.
- Raw Notion export is read-only provenance.
- Reports explain migration reasoning and should be updated after major reorganizations.
- New documents must use lowercase kebab-case filenames and metadata frontmatter.
- Section README files should provide direct navigation, not placeholder text.
- High-value notes should move from resource lists toward structured guides with prerequisites, testing steps, validation notes, and references.

## Contributor Workflow

1. Add or edit canonical documents in the semantic folders.
2. Keep source provenance when migrating additional raw notes.
3. Add external references to the `references` frontmatter and relevant body section.
4. Update `reports/knowledge_graph.md` if a new topic changes prerequisites or relationships.
5. Run link/reference QA before committing.

## Long-Term Improvements

- Convert high-value link dumps into original explanatory guides.
- Add testing checklists per vulnerability class.
- Validate external links periodically.
- Add severity, impact, detection, exploitation, and remediation sections to each vulnerability note.
