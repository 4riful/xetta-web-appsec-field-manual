---
title: "Xetta Web AppSec Field Manual"
summary: "A structured web application security field manual for bug bounty, reconnaissance, vulnerability testing, tooling, and AppSec reference material."
tags:
  - appsec
  - pentesting
  - bug-bounty
  - knowledge-base
related_topics:
  - "Bug Bounty Workflow"
  - "Reconnaissance Methodology"
  - "Vulnerabilities"
references:
---
# Xetta Web AppSec Field Manual

## Overview

This repository is a cleaned, reorganized, and maintainable Web AppSec knowledge base migrated from a long-running Notion workspace.

The goal is not to mirror the old export. The goal is to make the material usable as a long-term security field manual: easy to search, easy to extend, and organized around how application security work is actually performed.

## Start Here

- New to the repo: start with [Bug Bounty Workflow](methodology/bug-bounty-workflow.md).
- Building target coverage: use [Reconnaissance Methodology](methodology/recon-methodology.md) and [Subdomain Enumeration](recon/subdomain-enumeration.md).
- Testing a specific bug class: go to [Vulnerabilities](vulnerabilities/README.md).
- Looking for tools, payloads, or automation: go to [Tooling](tooling/README.md).
- Auditing how this migration was done: read the [Reports](reports/).

## Repository Map

- [`methodology/`](methodology/README.md) - operating workflows, checklists, and end-to-end testing process.
- [`recon/`](recon/README.md) - asset discovery, OSINT, subdomain enumeration, JavaScript recon, dorking, and vhost discovery.
- [`vulnerabilities/`](vulnerabilities/README.md) - bug classes grouped by AppSec testing domain.
- [`tooling/`](tooling/README.md) - Burp Suite, automation, fuzzing, payloads, wordlists, and testing utilities.
- [`resources/`](resources/README.md) - cheat sheets, writeups, blogs, videos, mindmaps, and training material.
- [`code-review/`](code-review/README.md) - source-code analysis and secure code review references.
- [`assets/`](assets/) - normalized images and media copied from the export.
- [`reports/`](reports/) - audit, taxonomy, merge, graph, repository plan, and QA reports.
- [`source-archive/`](source-archive/README.md) - raw Notion export preserved for provenance.

## Core Reading Path

1. [Bug Bounty Workflow](methodology/bug-bounty-workflow.md)
2. [Reconnaissance Methodology](methodology/recon-methodology.md)
3. [Subdomain Enumeration](recon/subdomain-enumeration.md)
4. [JavaScript Recon for Bug Bounty](recon/javascript-recon.md)
5. [Burp Suite and Testing Toolkit](tooling/burp-suite-and-toolkit.md)
6. [Payloads and Wordlists](tooling/payloads-and-wordlists.md)

## Vulnerability Index

| Area | Documents |
|---|---|
| Authentication | [Authentication and Account Security](vulnerabilities/authentication-and-account-security.md) |
| Authorization | [Access Control and Business Logic](vulnerabilities/access-control-and-business-logic.md) |
| Injection | [SQL Injection](vulnerabilities/sql-injection.md), [Command Injection and RCE](vulnerabilities/command-injection-and-rce.md), [Cross-Site Scripting](vulnerabilities/xss.md) |
| Server-side bugs | [SSRF](vulnerabilities/ssrf.md), [XXE and LFI](vulnerabilities/xxe-and-lfi.md), [HTTP Request Smuggling](vulnerabilities/http-request-smuggling.md) |
| Upload and parsing | [File Upload Vulnerabilities](vulnerabilities/file-upload.md) |
| API security | [API and GraphQL Security](vulnerabilities/api-and-graphql.md) |
| Cloud and infrastructure | [Cloud and AWS Security](vulnerabilities/cloud-and-aws-security.md), [DNS and Port Scanning](vulnerabilities/dns-and-port-scanning.md) |
| Defensive bypass | [CORS Misconfiguration](vulnerabilities/cors.md), [WAF Bypass](vulnerabilities/waf-bypass.md) |
| Research backlog | [Zero-Day and Miscellaneous Vulnerabilities](vulnerabilities/zero-day-and-miscellaneous.md) |

## Migration Reports

| Report | Purpose |
|---|---|
| [Audit Report](reports/audit_report.md) | Full source inventory, stubs, duplicate groups, and destination mapping. |
| [Taxonomy](reports/taxonomy.md) | The semantic organization model used for the repository. |
| [Knowledge Graph](reports/knowledge_graph.md) | Topic relationships, prerequisites, and navigation graph. |
| [Merge Report](reports/merge_report.md) | Source-to-destination merge decisions and rationale. |
| [Repository Plan](reports/repository_plan.md) | Long-term maintenance and structure plan. |
| [QA Report](reports/qa_report.md) | Final validation status for metadata, links, and provenance. |

## Repository Standards

- Canonical files use lowercase kebab-case names.
- Canonical documents include title, summary, tags, related topics, references, and source provenance.
- Raw export files are preserved but should not be edited as the primary knowledge base.
- New material should be added to semantic folders, not dumped into `resources/` by default.
- Fragmented notes should only be merged after verifying semantic overlap.

## Provenance

The original Notion export is preserved in [source-archive/notion-export](source-archive/notion-export/) so no source knowledge is lost. Use canonical documents for daily reading and editing; use the archive when you need to inspect the original imported material.

## Maintenance Rules

- Prefer editing canonical documents over raw archive files.
- Keep filenames lowercase kebab-case.
- Add title, summary, tags, related topics, and references to every new document.
- Merge fragments only after verifying semantic overlap.
- Preserve source provenance when moving or consolidating notes.
