---
title: "Resource-First Organization"
summary: "How to use this repository as a resource library first and a field manual second."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - navigation
  - repository-structure
related:
  - RESOURCES.md
  - 08-reference-library/README.md
  - FIELD-MANUAL.md
references: []
---
# Resource-First Organization

## Principle

This repository should deliver resources first.

The original ZIP export was full of links, tools, payload references, writeups, GitBooks, cheat sheets, videos, and topic-specific resources. Those resources should be visible immediately before a reader has to understand the field-manual structure.

## Primary Path

1. Open [RESOURCES.md](RESOURCES.md).
2. Pick the category you need.
3. Follow the source-backed links.
4. Use the field manual only when you want workflow, testing structure, or reporting guidance.

## Resource Layers

| Layer | Location | Purpose |
|---|---|---|
| Main resource list | [RESOURCES.md](RESOURCES.md) | Root-level, all categories inline, every extracted resource visible. |
| Category indexes | [08-reference-library/resource-indexes/](08-reference-library/resource-indexes/) | Topic-specific resource pages. |
| Source-folder list | [08-reference-library/all-source-resources.md](08-reference-library/all-source-resources.md) | Resources grouped by the original Notion folder/file context. |
| Source URL audit | [maintainers/source-resource-links.md](maintainers/source-resource-links.md) | Every URL occurrence and exact source file. |
| Source file audit | [maintainers/exhaustive-source-catalog.md](maintainers/exhaustive-source-catalog.md) | Every Markdown file, headings, counts, coverage, assets. |

## Categories

- [Recon and OSINT](08-reference-library/resource-indexes/recon-osint.md)
- [Payloads, Cheat Sheets, and Wordlists](08-reference-library/resource-indexes/payloads-cheatsheets-wordlists.md)
- [Blogs, Writeups, GitBooks, and Bug Bounty References](08-reference-library/resource-indexes/blogs-writeups-gitbooks.md)
- [Burp Suite and Tooling](08-reference-library/resource-indexes/burp-tooling.md)
- [XSS and Client-Side](08-reference-library/resource-indexes/xss-client-side.md)
- [SQL Injection](08-reference-library/resource-indexes/sql-injection.md)
- [SSRF](08-reference-library/resource-indexes/ssrf.md)
- [XXE, LFI, and File Read](08-reference-library/resource-indexes/xxe-lfi-file-read.md)
- [File Upload and Parser Abuse](08-reference-library/resource-indexes/file-upload-parser-abuse.md)
- [API, Auth, OAuth, and GraphQL](08-reference-library/resource-indexes/api-auth-graphql.md)
- [Cloud and Infrastructure](08-reference-library/resource-indexes/cloud-infra.md)
- [RCE, CVE, and Research](08-reference-library/resource-indexes/rce-cve-research.md)
- [WAF, CORS, CSRF, Smuggling, and Web Platform Bypass](08-reference-library/resource-indexes/web-platform-bypass.md)
- [Training, Labs, Videos, OSCP, AD, and Red Team](08-reference-library/resource-indexes/training-labs-videos.md)
- [Miscellaneous Unsorted Source Links](08-reference-library/resource-indexes/misc-uncategorized.md)

## How The Manual Fits

The field-manual sections are the second layer:

- Use `01-reconnaissance/` when you want to run recon.
- Use `02-mapping-and-triage/` when you need to turn resources and findings into leads.
- Use `03-vulnerability-guides/` when you need testing steps for a bug class.
- Use `05-toolkit/` when a tool needs usage notes, not just a link.
- Use `07-reporting/` when you need to write findings.

## Non-Negotiable Resource Rule

If a source URL exists in the ZIP export, it must remain findable from [RESOURCES.md](RESOURCES.md) or an explicitly linked source-audit page.
