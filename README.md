---
title: "Xetta's Web Application Hacking Vault"
summary: "A polished web application hacking resource vault built from the ZIP source: links, payloads, tools, writeups, labs, bug classes, and source-traceable data."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - appsec
  - resources
  - bug-bounty
  - vault
related:
  - QUICKSTART.md
  - RESOURCES.md
  - resources/README.md
  - awesome-lists/README.md
  - data/README.md
references: []
---
# Xetta's Web Application Hacking Vault

> A resource-first web application hacking vault for recon, payloads, tools, writeups, GitBooks, cheat sheets, labs, bug classes, and practical hunting playbooks.

`407 source URLs`  `540 resource records`  `128 extracted snippets`  `66 source notes`  `3 preserved assets`

This repo is built from the ZIP source, but it is not a ZIP dump. Every useful link, command, payload, dork, tool reference, and source occurrence was extracted into a database first, then reshaped into browsable vault sections.

## Start Fast

Open these first:

- [resources/](resources/README.md) for the full topic-sorted vault.
- [awesome-lists/top-25-web-appsec-links.md](awesome-lists/top-25-web-appsec-links.md) when you want the strongest links first.
- [payloads/](payloads/README.md) when you want payloads, wordlists, and reusable snippets.
- [tools/](tools/README.md) when you need scanners, Burp extensions, recon tooling, OOB tooling, or automation.
- [bug-classes/](bug-classes/README.md) when you already know the vulnerability type.
- [maps/](maps/README.md) when you want a path by goal, bug class, tool, resource type, or skill level.
- [data/resources.csv](data/resources.csv) when you want the raw structured database.

## The Vault

### Resources

Topic-sorted link collections live in [resources/](resources/README.md). This is the main library.

Start with:

- [Recon and OSINT](resources/recon-and-osint.md)
- [Payloads, Cheat Sheets, and Wordlists](resources/payloads-cheat-sheets-and-wordlists.md)
- [Bug Bounty Writeups, Blogs, and GitBooks](resources/bug-bounty-writeups-blogs-and-gitbooks.md)
- [Burp Suite and Tooling](resources/burp-suite-and-tooling.md)
- [XSS and Client-Side](resources/xss-and-client-side.md)
- [SSRF](resources/ssrf.md)
- [SQL Injection](resources/sql-injection.md)
- [File Upload and Parser Abuse](resources/file-upload-and-parser-abuse.md)
- [RCE, CVEs, and 0days](resources/rce-cves-and-0days.md)

### Best Of

The `awesome-lists/` folder is the curated layer. It is meant for fast browsing without drowning in every source link.

- [Top 25 Web AppSec Links](awesome-lists/top-25-web-appsec-links.md)
- [Best Recon Resources](awesome-lists/best-recon-resources.md)
- [Best Bug Bounty Writeups](awesome-lists/best-bug-bounty-writeups.md)
- [Best Cheat Sheets](awesome-lists/best-cheat-sheets.md)
- [Best Burp Extensions](awesome-lists/best-burp-extensions.md)
- [Best Payload Repositories](awesome-lists/best-payload-repositories.md)
- [Hidden Gems](awesome-lists/hidden-gems.md)

### Payloads

The [payloads/](payloads/README.md) section pulls payload-heavy resources and snippets into direct bug-class pages:

- XSS
- SQL injection
- SSRF
- LFI and path traversal
- Command injection
- File upload bypass
- WAF bypass
- Request smuggling
- Wordlists

### Tools

The [tools/](tools/README.md) section groups usable tooling references instead of leaving them buried inside old note titles.

- Recon
- Content discovery
- JavaScript analysis
- Burp extensions
- Fuzzing
- Out-of-band testing
- Cloud
- API and GraphQL
- Automation

### Bug Classes

The [bug-classes/](bug-classes/README.md) section is sorted by vulnerability family:

- Access control
- Authentication
- API
- Client-side
- Cloud
- Defensive bypass
- Files and parsers
- Injection
- Server-side

### Playbooks, Labs, Reports

Use these when you want structure around the resources:

- [playbooks/](playbooks/README.md) for workflows like recon-to-first-bug, API assessment, cloud exposure review, and report writing.
- [labs/](labs/README.md) for training, videos, OSCP, Active Directory, practice platforms, and mindmaps.
- [reports/](reports/README.md) for evidence standards, templates, severity notes, and remediation language.

## Database First

The real source of truth is the database, not the Markdown pages.

- [data/resources.csv](data/resources.csv) contains one row per deduplicated resource or snippet.
- [data/resource_occurrences.csv](data/resource_occurrences.csv) keeps every source occurrence traceable.
- [data/source_documents.csv](data/source_documents.csv) maps every raw Markdown source file.
- [data/resources.json](data/resources.json) is the machine-readable export.

The vault pages are generated from this model so links, snippets, and source provenance stay connected.

## Why This Version Is Different

The old structure was too book-like. This reset is built for browsing and reuse:

- resources first, explanations second;
- best-of lists before exhaustive dumps;
- bug-class folders when you know what you are hunting;
- payload and tool sections when you need something practical fast;
- CSV/JSON data when you want to search, filter, or rebuild the vault;
- raw source preserved only for audit, not as the main experience.

## Source Stats

- Raw Markdown files scanned: `66`
- Raw image assets preserved: `3`
- Deduplicated resource/snippet records: `540`
- Source occurrences: `583`
- URL resources: `412`
- Non-URL snippet resources: `128`

## Provenance

The raw ZIP/Notion export is preserved under [provenance/raw-archive/notion-export/](provenance/raw-archive/notion-export/). It is kept for audit and recovery only.

Public browsing should start from [resources/](resources/README.md), [awesome-lists/](awesome-lists/README.md), [payloads/](payloads/README.md), [tools/](tools/README.md), or [bug-classes/](bug-classes/README.md).
