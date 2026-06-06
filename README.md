---
title: "Xettas Web App Pentesting Handbook"
summary: "A normalized GitHub knowledge repository migrated from a Notion AppSec and bug bounty workspace."
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
# Xettas Web App Pentesting Handbook

## Summary

This repository is a professionalized migration of the exported Notion workspace. The structure prioritizes semantic AppSec practice areas over historical Notion folders, keeps all source material traceable, and normalizes naming to lowercase kebab-case.

## Repository Map

- `methodology/` - workflows, checklists, and end-to-end operating guidance.
- `recon/` - asset discovery, OSINT, subdomain enumeration, dorking, JavaScript recon, and vhost enumeration.
- `vulnerabilities/` - bug classes grouped by security domain.
- `tooling/` - tools, Burp Suite extensions, fuzzing, automation, payloads, and wordlists.
- `resources/` - cheat sheets, writeups, blogs, videos, mindmaps, and training resources.
- `code-review/` - source-code-analysis and code-review references.
- `assets/` - normalized media assets.
- `source-archive/` - raw Notion export preserved for provenance.
- `reports/` - migration reasoning, taxonomy, graph, merge, and QA reports.

## Canonical Documents

- [Source Code Analysis and Code Review](code-review/source-code-analysis.md) - Canonical source code analysis and code review note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Bug Bounty Workflow](methodology/bug-bounty-workflow.md) - Canonical bug bounty workflow note migrated from 4 Notion source page(s), preserving commands, links, and resource references.
- [Reconnaissance Methodology](methodology/recon-methodology.md) - Canonical reconnaissance methodology note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [JavaScript Recon for Bug Bounty](recon/javascript-recon.md) - Canonical javascript recon for bug bounty note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [OSINT and Dorking](recon/osint-and-dorking.md) - Canonical osint and dorking note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Subdomain Enumeration](recon/subdomain-enumeration.md) - Canonical subdomain enumeration note migrated from 3 Notion source page(s), preserving commands, links, and resource references.
- [Blogs, Writeups, and Gitbooks](resources/blogs-writeups-and-gitbooks.md) - Canonical blogs, writeups, and gitbooks note migrated from 6 Notion source page(s), preserving commands, links, and resource references.
- [Cheat Sheets](resources/cheat-sheets.md) - Canonical cheat sheets note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [Bugs](resources/uncategorized/bugs.md) - Preserved standalone source page for Bugs; retained separately because no verified semantic merge target was identified.
- [Twitter tips](resources/uncategorized/twitter-tips.md) - Preserved standalone source page for Twitter tips; retained separately because no verified semantic merge target was identified.
- [v1 recon](resources/uncategorized/v1-recon.md) - Preserved standalone source page for v1 recon; retained separately because no verified semantic merge target was identified.
- [Xetta Web AppSec Handbook](resources/uncategorized/xetta-web-appsec-handbook.md) - Preserved standalone source page for Xetta Web AppSec Handbook; retained separately because no verified semantic merge target was identified.
- [Videos, Mindmaps, and Training](resources/videos-mindmaps-and-training.md) - Canonical videos, mindmaps, and training note migrated from 5 Notion source page(s), preserving commands, links, and resource references.
- [Automation and Fuzzing](tooling/automation-and-fuzzing.md) - Canonical automation and fuzzing note migrated from 3 Notion source page(s), preserving commands, links, and resource references.
- [Burp Suite and Testing Toolkit](tooling/burp-suite-and-toolkit.md) - Canonical burp suite and testing toolkit note migrated from 3 Notion source page(s), preserving commands, links, and resource references.
- [Payloads and Wordlists](tooling/payloads-and-wordlists.md) - Canonical payloads and wordlists note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Access Control and Business Logic](vulnerabilities/access-control-and-business-logic.md) - Canonical access control and business logic note migrated from 3 Notion source page(s), preserving commands, links, and resource references.
- [API and GraphQL Security](vulnerabilities/api-and-graphql.md) - Canonical api and graphql security note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Authentication and Account Security](vulnerabilities/authentication-and-account-security.md) - Canonical authentication and account security note migrated from 3 Notion source page(s), preserving commands, links, and resource references.
- [Cloud and AWS Security](vulnerabilities/cloud-and-aws-security.md) - Canonical cloud and aws security note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Command Injection and RCE](vulnerabilities/command-injection-and-rce.md) - Canonical command injection and rce note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [CORS Misconfiguration](vulnerabilities/cors.md) - Canonical cors misconfiguration note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [DNS and Port Scanning](vulnerabilities/dns-and-port-scanning.md) - Canonical dns and port scanning note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [File Upload Vulnerabilities](vulnerabilities/file-upload.md) - Canonical file upload vulnerabilities note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [HTTP Request Smuggling](vulnerabilities/http-request-smuggling.md) - Canonical http request smuggling note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [SQL Injection](vulnerabilities/sql-injection.md) - Canonical sql injection note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [Server-Side Request Forgery](vulnerabilities/ssrf.md) - Canonical server-side request forgery note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [WAF Bypass](vulnerabilities/waf-bypass.md) - Canonical waf bypass note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Cross-Site Scripting](vulnerabilities/xss.md) - Canonical cross-site scripting note migrated from 1 Notion source page(s), preserving commands, links, and resource references.
- [XXE and Local File Inclusion](vulnerabilities/xxe-and-lfi.md) - Canonical xxe and local file inclusion note migrated from 2 Notion source page(s), preserving commands, links, and resource references.
- [Zero-Day and Miscellaneous Vulnerabilities](vulnerabilities/zero-day-and-miscellaneous.md) - Canonical zero-day and miscellaneous vulnerabilities note migrated from 3 Notion source page(s), preserving commands, links, and resource references.

## Maintenance Rules

- Prefer editing canonical documents over raw archive files.
- Keep filenames lowercase kebab-case.
- Add title, summary, tags, related topics, and references to every new document.
- Merge fragments only after verifying semantic overlap.
- Preserve source provenance when moving or consolidating notes.
