---
title: "Xetta Web AppSec Field Manual"
summary: "An operator-focused Web AppSec field manual for recon, attack-surface mapping, vulnerability testing, tooling, source review, and reporting."
tags:
  - appsec
  - pentesting
  - bug-bounty
  - knowledge-base
related:
  - "START-HERE.md"
  - "FIELD-MANUAL.md"
  - "maintainers/exhaustive-source-catalog.md"
status: "reviewed"
last_reviewed: "2026-06-06"
references: []
---
# Xetta Web AppSec Field Manual

An operator-focused manual for web application security work: recon, attack-surface mapping, vulnerability playbooks, tooling, payloads, source review, and report writing.

This is not a raw Notion dump. The original workspace is preserved for provenance, but the working repository is organized as a field manual: start with a target, build coverage, find testable leads, validate impact, and write useful reports.

## Why This Exists

Most security note repos become one of three things: link dumps, payload dumps, or personal notes that nobody else can navigate. This repo is designed around practical use:

- Where do I start?
- What should I collect?
- What signals matter?
- How do I test safely?
- How do I validate impact?
- How do I report it clearly?

## Start Here

- New to the repo: [START-HERE.md](START-HERE.md)
- Want the full flow: [FIELD-MANUAL.md](FIELD-MANUAL.md)
- Doing recon: [01-reconnaissance/](01-reconnaissance/README.md)
- Turning recon into testable leads: [02-mapping-and-triage/](02-mapping-and-triage/README.md)
- Testing a bug class: [03-vulnerability-guides/](03-vulnerability-guides/README.md)
- Need tools, payloads, or wordlists: [05-toolkit/](05-toolkit/README.md)
- Need the full resource/link list: [RESOURCES.md](RESOURCES.md)
- Need to write a report: [07-reporting/](07-reporting/README.md)

## Use This Repo By Task

| Task | Start here |
|---|---|
| Build a recon workflow | [01-reconnaissance/workflow.md](01-reconnaissance/workflow.md) |
| Enumerate subdomains and vhosts | [01-reconnaissance/subdomain-enumeration.md](01-reconnaissance/subdomain-enumeration.md), [01-reconnaissance/virtual-host-discovery.md](01-reconnaissance/virtual-host-discovery.md) |
| Mine archives and JavaScript | [01-reconnaissance/url-and-archive-recon.md](01-reconnaissance/url-and-archive-recon.md), [01-reconnaissance/javascript-recon.md](01-reconnaissance/javascript-recon.md) |
| Decide what is worth testing | [02-mapping-and-triage/finding-testable-leads.md](02-mapping-and-triage/finding-testable-leads.md) |
| Test IDOR/access control | [03-vulnerability-guides/access-control/idor.md](03-vulnerability-guides/access-control/idor.md) |
| Test SSRF | [03-vulnerability-guides/server-side/ssrf.md](03-vulnerability-guides/server-side/ssrf.md) |
| Test file upload issues | [03-vulnerability-guides/files-and-parsers/file-upload.md](03-vulnerability-guides/files-and-parsers/file-upload.md) |
| Pick Burp extensions | [05-toolkit/burp-suite/extensions.md](05-toolkit/burp-suite/extensions.md) |
| Pick payloads | [05-toolkit/payloads/README.md](05-toolkit/payloads/README.md) |
| Browse every source resource link | [RESOURCES.md](RESOURCES.md) |
| Review source code | [06-code-review/review-methodology.md](06-code-review/review-methodology.md) |

## Field Manual Map

| Section | Purpose |
|---|---|
| [00-orientation](00-orientation/README.md) | Scope discipline, setup assumptions, and how to use the manual. |
| [01-reconnaissance](01-reconnaissance/README.md) | Asset discovery, subdomains, vhosts, OSINT, archives, JavaScript, and content discovery. |
| [02-mapping-and-triage](02-mapping-and-triage/README.md) | Convert raw recon into models, leads, and test priorities. |
| [03-vulnerability-guides](03-vulnerability-guides/README.md) | Focused vulnerability playbooks with tests, tools, payloads, evidence, and reporting notes. |
| [04-workflows](04-workflows/README.md) | End-to-end workflows for bug bounty, API assessment, cloud exposure, and source-assisted review. |
| [05-toolkit](05-toolkit/README.md) | Burp, automation, payloads, wordlists, and command workflows. |
| [06-code-review](06-code-review/README.md) | Source-to-sink review, code audit methodology, and framework notes. |
| [07-reporting](07-reporting/README.md) | Evidence standards, severity, remediation language, and sample findings. |
| [08-reference-library](08-reference-library/README.md) | Curated cheat sheets, writeups, books, videos, labs, and external tools. |

## Daily Testing Flow

1. Confirm scope and rules of engagement.
2. Build a target and asset inventory.
3. Enumerate subdomains, virtual hosts, live services, URLs, and JavaScript endpoints.
4. Model authentication, authorization, API surfaces, and high-value workflows.
5. Pick vulnerability playbooks based on real signals, not random payload spraying.
6. Validate findings manually with clean evidence.
7. Write a report that explains impact and remediation.

## Vulnerability Index

| Category | Guides |
|---|---|
| Access control | [IDOR](03-vulnerability-guides/access-control/idor.md), [403 Bypass](03-vulnerability-guides/access-control/403-bypass.md), [Business Logic Bypass](03-vulnerability-guides/access-control/business-logic-bypass.md) |
| Authentication | [Account Takeover](03-vulnerability-guides/authentication/account-takeover.md), [Password Reset](03-vulnerability-guides/authentication/password-reset.md), [OAuth and SSO](03-vulnerability-guides/authentication/oauth-and-sso.md) |
| Injection | [XSS](03-vulnerability-guides/injection/xss.md), [SQL Injection](03-vulnerability-guides/injection/sql-injection.md), [Command Injection](03-vulnerability-guides/injection/command-injection.md), [XXE](03-vulnerability-guides/injection/xxe.md) |
| Server-side | [SSRF](03-vulnerability-guides/server-side/ssrf.md), [LFI and Path Traversal](03-vulnerability-guides/server-side/lfi-and-path-traversal.md), [Request Smuggling](03-vulnerability-guides/server-side/request-smuggling.md) |
| Files and parsers | [File Upload](03-vulnerability-guides/files-and-parsers/file-upload.md), [Archive Processing](03-vulnerability-guides/files-and-parsers/archive-processing.md) |
| API security | [REST API Testing](03-vulnerability-guides/api-security/rest-api-testing.md), [GraphQL](03-vulnerability-guides/api-security/graphql.md), [Mass Assignment](03-vulnerability-guides/api-security/mass-assignment.md) |
| Client-side | [CORS](03-vulnerability-guides/client-side/cors.md), [postMessage](03-vulnerability-guides/client-side/postmessage.md), [CSRF](03-vulnerability-guides/client-side/csrf.md) |
| Cloud and infrastructure | [AWS S3](03-vulnerability-guides/cloud-and-infra/aws-s3.md), [Cloud Metadata](03-vulnerability-guides/cloud-and-infra/cloud-metadata.md), [Exposed Services](03-vulnerability-guides/cloud-and-infra/exposed-services.md) |
| Defensive bypass | [WAF Bypass](03-vulnerability-guides/defensive-bypass/waf-bypass.md), [Content-Type and Parser Confusion](03-vulnerability-guides/defensive-bypass/content-type-and-parser-confusion.md) |

## What Makes A Guide Good

Every serious guide should answer:

- What is the mental model?
- Where do I find this bug?
- What setup or accounts do I need?
- What manual tests should I run?
- Which tools help and what output matters?
- What false positives should I avoid?
- What evidence proves impact?
- How should the report be written?

## Curation Status

This repo was rebuilt from a Notion export with mixed quality. Canonical field-manual content separates:

- practical operator guidance,
- curated references,
- legacy migration notes,
- raw source archive.

Not every external link is endorsed. Links inherited from the source workspace are kept for provenance and promoted only when they are useful.

## Source Accountability

The original ZIP export has now been cataloged file-by-file and link-by-link:

| Catalog | What it proves |
|---|---|
| [RESOURCES.md](RESOURCES.md) | Root-level practical resource listing with all extracted URLs grouped by AppSec category. |
| [Exhaustive Source Catalog](maintainers/exhaustive-source-catalog.md) | Every original Markdown file, folder, heading sample, word count, link count, asset, and coverage destination. |
| [Source Coverage Matrix](maintainers/source-coverage-matrix.md) | Every source file mapped to maintained manual coverage or preservation location. |
| [Source Resource Links](maintainers/source-resource-links.md) | Every external URL occurrence extracted from the raw Markdown files. |
| [All Source Resources](08-reference-library/all-source-resources.md) | Public-facing exhaustive resource list grouped by original source folder. |

Current source inventory: 66 raw Markdown files, 3 image assets, 534 URL occurrences, and 407 unique external URLs.

## Maintainer Material

| Report | Purpose |
|---|---|
| [Audit Report](maintainers/migration-reports/audit-report.md) | Full source inventory, stubs, duplicate groups, and destination mapping. |
| [Taxonomy](maintainers/migration-reports/taxonomy.md) | Semantic organization model used for the migration. |
| [Knowledge Graph](maintainers/migration-reports/knowledge-graph.md) | Topic relationships, prerequisites, and navigation graph. |
| [Merge Report](maintainers/migration-reports/merge-report.md) | Source-to-destination merge decisions and rationale. |
| [Repository Plan](maintainers/migration-reports/repository-plan.md) | Long-term structure and maintenance plan. |
| [QA Report](maintainers/migration-reports/qa-report.md) | Validation status for metadata, links, and provenance. |
| [Exhaustive Source Catalog](maintainers/exhaustive-source-catalog.md) | Folder-by-folder source inventory from the preserved ZIP. |
| [Source Coverage Matrix](maintainers/source-coverage-matrix.md) | Source-to-manual coverage mapping for every original Markdown file. |
| [Source Resource Links](maintainers/source-resource-links.md) | Every external URL occurrence extracted from the original Markdown files. |

## Repository Standards

- Canonical files use lowercase kebab-case names.
- User-facing top-level sections use numeric prefixes to create a reading path.
- Commands must include purpose, input assumptions, expected output, and safety notes.
- Payloads must explain context and validation signals.
- Raw link dumps belong in `08-reference-library/`, not vulnerability guides.
- Migration internals belong in `maintainers/`, not the main reader path.

## Provenance

The original Notion export is preserved under [source-archive/notion-export](source-archive/notion-export/). Use canonical field-manual docs for daily work. Use the archive only to verify original wording, recover source context, or audit migration decisions.
