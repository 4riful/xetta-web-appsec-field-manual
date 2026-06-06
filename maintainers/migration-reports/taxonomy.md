---
title: "Taxonomy"
summary: "Semantic taxonomy for the professionalized AppSec knowledge repository."
tags:
  - report
  - migration
related_topics:
  - "Repository Migration"
references:
---
# Taxonomy

## Design Principles

- Use semantic AppSec domains, not Notion export folders.
- Separate methodology, reconnaissance, vulnerability classes, tooling, resources, and code review.
- Keep raw provenance while making canonical documents maintainable.
- Treat link dumps as curated resource collections unless they contain procedural testing steps.

## Top-Level Taxonomy

| Domain | Purpose | Representative Documents |
|---|---|---|
| Methodology | End-to-end hunting workflow and repeatable testing process. | `methodology/bug-bounty-workflow.md`, `methodology/recon-methodology.md` |
| Reconnaissance | Discover targets, assets, endpoints, subdomains, vhosts, and OSINT signals. | `recon/subdomain-enumeration.md`, `recon/osint-and-dorking.md`, `recon/javascript-recon.md` |
| Vulnerabilities | Bug-class notes grouped by how AppSec teams test and triage issues. | `vulnerabilities/ssrf.md`, `vulnerabilities/access-control-and-business-logic.md`, `vulnerabilities/api-and-graphql.md` |
| Tooling | Operational tools, automation, payloads, fuzzing, Burp Suite extensions, and wordlists. | `tooling/burp-suite-and-toolkit.md`, `tooling/automation-and-fuzzing.md`, `tooling/payloads-and-wordlists.md` |
| Resources | External references, cheat sheets, blogs, writeups, videos, mindmaps, and training. | `resources/cheat-sheets.md`, `resources/blogs-writeups-and-gitbooks.md` |
| Code Review | Source analysis and secure review references. | `code-review/source-code-analysis.md` |
| Source Archive | Immutable raw export for traceability. | `source-archive/notion-export/` |

## Security SME Grouping

- Authentication and account security: auth bypass, account takeover, password reset.
- Authorization and business logic: IDOR, 403 bypass, logic bypass.
- Injection: XSS, SQL injection, command injection, XXE, RCE-adjacent material.
- Server-side and infrastructure: SSRF, LFI, HTTP request smuggling, DNS, port scanning.
- Cloud: AWS and S3 misconfiguration material.
- API security: REST/API notes and GraphQL.
- Testing operations: recon, fuzzing, payloads, wordlists, Burp Suite, automation.

## Folder Justification

- `methodology/` exists because workflow notes cut across all vulnerability classes.
- `recon/` exists because asset discovery and OSINT are prerequisites to most testing.
- `vulnerabilities/` exists because bug-class references need direct discoverability.
- `tooling/` exists because tools and commands support many domains and should not be hidden inside bug notes.
- `resources/` exists because many pages are curated external learning resources rather than procedural instructions.
- `code-review/` exists because source-code analysis is a distinct testing mode.
