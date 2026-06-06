---
title: "Contributing"
summary: "Contribution and maintenance rules for Xetta's Web Application Hacking Vault."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - contributing
  - maintenance
  - appsec
related:
  - "maintainers/content-quality-checklist.md"
  - "data/resources.csv"
references: []
---
# Contributing

This repository is a resource vault. Contributions should improve browsing quality, resource accuracy, and learning value.

## Content Rules

- Add new resources to the semantic folder where they belong.
- Do not create catch-all dump folders for unrelated links.
- Use lowercase kebab-case filenames.
- Preserve technical commands, payloads, links, and references.
- Prefer improving vault pages, resource lists, templates, and data views.

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

Use the templates in `templates/` for new resource pages, tool notes, payload pages, workflows, and bug-class pages. At minimum, new pages should contain:

1. Purpose or mental model.
2. Preconditions or where-to-look signals.
3. Manual workflow.
4. Tooling or commands, if relevant.
5. False positives.
6. Evidence requirements.
7. References.

## Resource Submission Policy

Open an issue with the resource request template when suggesting a link, tool, payload list, writeup, lab, or snippet.

For pull requests, include:

- what was added;
- why it belongs in this vault;
- where it should live;
- whether it is a tool, writeup, payload list, cheat sheet, lab, command snippet, or reference.

## Merge Policy

Merge notes only when they clearly describe the same topic, workflow, bug class, or reference set. If overlap is uncertain, keep the note separate and link it from the nearest canonical document.

## Internal Archive Policy

Do not edit internal archive material unless the change is explicitly about repository maintenance. Public contributions should focus on `resources/`, `awesome-lists/`, `payloads/`, `tools/`, `bug-classes/`, `playbooks/`, `labs/`, `reports/`, `templates/`, or `data/`.
