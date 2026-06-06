---
title: "Link Checking"
summary: "Maintainer notes for validating internal links and metadata."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - qa
  - links
related:
  - migration-reports/qa-report.md
references: []
---
# Link Checking

## Maintained Content Scope

Check numbered sections, root docs, templates, `assets/`, and maintainer docs.

Exclude from strict link enforcement:

- `source-archive/notion-export/`, because it preserves raw Notion links.
- `maintainers/legacy-generated/`, because it preserves first-pass generated docs during transition.

## Checks

- Markdown files have frontmatter.
- Internal links resolve.
- User-facing sections do not contain `uncategorized` folders.
