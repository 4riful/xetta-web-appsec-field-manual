---
title: "Repository Plan"
summary: "Long-term GitHub repository architecture and maintenance plan."
tags:
  - report
  - migration
related_topics:
  - "Repository Migration"
references:
---
# Repository Plan

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
