---
title: "Contributing"
summary: "Contribution and maintenance rules for the Xetta Web AppSec Field Manual."
tags:
  - contributing
  - maintenance
  - appsec
related_topics:
  - "Repository Standards"
  - "Repository Plan"
references:
  - reports/repository_plan.md
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
- `related_topics`
- `references`

## Writing Format

Use this order for new canonical documents:

1. Summary
2. Scope
3. Prerequisites
4. Testing Notes
5. Tools and Payloads
6. Related Topics
7. References
8. Source Provenance, if migrated from another source

## Merge Policy

Merge notes only when they clearly describe the same topic, workflow, bug class, or reference set. If overlap is uncertain, keep the note separate and link it from the nearest canonical document.

## Archive Policy

The `source-archive/` folder is provenance, not the working knowledge base. Keep it intact unless a future migration explicitly replaces it with a better source-of-truth archive.
