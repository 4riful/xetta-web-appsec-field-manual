---
title: "Xetta Web Hacker Vault"
summary: "A browsable Web AppSec resource vault generated from the ZIP source."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - appsec
  - resources
  - bug-bounty
  - vault
related: []
references: []
---
# Xetta Web Hacker Vault

A browsable Web AppSec resource vault built from the ZIP source: recon, payloads, tools, writeups, GitBooks, cheat sheets, labs, bug classes, and practical hunting playbooks.

`407 source URLs` `resource database` `payloads` `tools` `writeups` `labs` `bug classes`

## Jump In

| Need | Start |
|---|---|
| Browse resources | [resources/](resources/README.md) |
| Best links only | [awesome-lists/top-25-web-appsec-links.md](awesome-lists/top-25-web-appsec-links.md) |
| Grab payloads or wordlists | [payloads/](payloads/README.md) |
| Pick tools | [tools/](tools/README.md) |
| Learn by bug class | [bug-classes/](bug-classes/README.md) |
| Follow a workflow | [playbooks/](playbooks/README.md) |
| Practice or watch training | [labs/](labs/README.md) |
| Write reports | [reports/](reports/README.md) |
| Query the database | [data/resources.csv](data/resources.csv) |

## Vault Sections

- [Resources](resources/README.md): topic-sorted resource pages.
- [Awesome Lists](awesome-lists/README.md): curated best-of views.
- [Payloads](payloads/README.md): payload, wordlist, and snippet resources.
- [Tools](tools/README.md): tools, Burp extensions, scanners, command snippets.
- [Bug Classes](bug-classes/README.md): vulnerability-specific resource indexes.
- [Playbooks](playbooks/README.md): practical workflows.
- [Maps](maps/README.md): alternate navigation paths.
- [Labs](labs/README.md): videos, labs, OSCP, AD, mindmaps.
- [Reports](reports/README.md): reporting templates and evidence standards.
- [Data](data/README.md): generated resource database.
- [Provenance](provenance/README.md): source archive and audit trail.

## Database First

The reset is built around `data/resources.csv` and `data/resource_occurrences.csv`.

- One row per deduplicated resource/snippet in `resources.csv`.
- One row per source occurrence in `resource_occurrences.csv`.
- One row per raw Markdown file in `source_documents.csv`.

## Source Stats

- Raw Markdown files scanned: 66
- Raw image assets preserved: 3
- Source URL/resource records and snippets are traceable through `data/` and `provenance/`.

## Provenance

The raw ZIP/Notion export is preserved under `provenance/raw-archive/notion-export/`. It is kept for audit only; the vault folders are the primary browsing path.
