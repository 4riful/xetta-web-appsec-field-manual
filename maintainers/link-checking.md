---
title: "Link Checking"
summary: "Maintainer notes for validating internal links and metadata."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - qa
  - links
related:
  - ../data/README.md
  - ../provenance/README.md
references: []
---
# Link Checking

## Maintained Content Scope

Check root docs, vault folders, templates, `data/`, `provenance/` audit pages, and maintainer docs.

Exclude from strict link enforcement:

- `provenance/raw-archive/notion-export/`, because it preserves raw Notion links and original local references.
- Generated CSV/JSON content should be checked for existence, not Markdown frontmatter.

## Checks

- Markdown files have frontmatter.
- Internal links resolve.
- Raw archive stays under `provenance/raw-archive/`.
- The main README links the vault entry points, not old migration reports.
- Resource pages derive from `data/resources.csv` and source occurrences remain traceable.
