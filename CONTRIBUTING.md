---
title: "Contributing"
summary: "Contribution and maintenance rules for the Xetta Web AppSec Field Manual."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - contributing
  - maintenance
  - appsec
related:
  - "maintainers/content-quality-checklist.md"
  - "maintainers/migration-reports/repository-plan.md"
references:
  - "maintainers/migration-reports/repository-plan.md"
---
# Contributing

## Content Rules

- Add new knowledge to the semantic folder where it belongs.
- Do not create catch-all dump folders for unrelated links.
- Use lowercase kebab-case filenames.
- Preserve technical commands, payloads, links, and references.
- Prefer improving canonical documents over editing raw source archive files.

## Required Document Metadata

Every Markdown document should include:

- `title`
- `summary`
- `tags`
- `related`
- `references`
- `status`
- `last_reviewed`

## Writing Format

Use the templates in `templates/` for new field-manual content. At minimum, new guides should contain:

1. Purpose or mental model.
2. Preconditions or where-to-look signals.
3. Manual workflow.
4. Tooling or commands, if relevant.
5. False positives.
6. Evidence requirements.
7. References and provenance.

## Merge Policy

Merge notes only when they clearly describe the same topic, workflow, bug class, or reference set. If overlap is uncertain, keep the note separate and link it from the nearest canonical document.

## Archive Policy

The `source-archive/` folder is provenance, not the working knowledge base. Keep it intact unless a future migration explicitly replaces it with a better source-of-truth archive.
