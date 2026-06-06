---
title: "Resource Map"
summary: "Clean front door for the Web AppSec resource library. Start here before the exhaustive raw resource dump."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - navigation
  - appsec
related:
  - RESOURCES.md
  - RESOURCE-FIRST.md
  - 08-reference-library/README.md
  - maintainers/agentic-resource-audit.md
references: []
---
# Resource Map

Start here. This page is the clean navigation layer.

`RESOURCES.md` is the exhaustive source dump. It proves every URL from the ZIP is preserved, but it is intentionally noisy because the original export was noisy. Use this map first, then open the raw lists only when you need every link.

## Best Starting Points

| Need | Start here | Why |
|---|---|---|
| Recon, subdomains, dorks, OSINT | [Recon and OSINT](08-reference-library/resource-indexes/recon-osint.md) | Best first stop for target discovery and recon resources. |
| Payloads, checklists, wordlists | [Payloads, Cheat Sheets, and Wordlists](08-reference-library/resource-indexes/payloads-cheatsheets-wordlists.md) | Central place for reusable payload and checklist collections. |
| Bug bounty writeups and GitBooks | [Blogs, Writeups, GitBooks, and Bug Bounty References](08-reference-library/resource-indexes/blogs-writeups-gitbooks.md) | Largest learning/reference bucket from the source export. |
| Burp extensions and tools | [Burp Suite and Tooling](08-reference-library/resource-indexes/burp-tooling.md) | Tools from the original Burp/toolkit folders. |
| API, auth, OAuth, GraphQL | [API, Auth, OAuth, and GraphQL](08-reference-library/resource-indexes/api-auth-graphql.md) | API security, OAuth, SSO, GraphQL, and checklist resources. |
| XSS and browser-side testing | [XSS and Client-Side](08-reference-library/resource-indexes/xss-client-side.md) | XSS payloads, client-side writeups, DOM/browser material. |
| SSRF | [SSRF](08-reference-library/resource-indexes/ssrf.md) | SSRF cheat sheets, tools, and writeups. |
| SQL injection | [SQL Injection](08-reference-library/resource-indexes/sql-injection.md) | SQLi payloads, cheat sheets, writeups, and tools. |
| File upload, parser abuse | [File Upload and Parser Abuse](08-reference-library/resource-indexes/file-upload-parser-abuse.md) | Upload, SVG, parser, XML/ZIP, and impact-chain resources. |
| XXE, LFI, file read | [XXE, LFI, and File Read](08-reference-library/resource-indexes/xxe-lfi-file-read.md) | Parser/file-read references and LFI material. |
| WAF, CORS, CSRF, smuggling | [WAF, CORS, CSRF, Smuggling, and Web Platform Bypass](08-reference-library/resource-indexes/web-platform-bypass.md) | Web platform and bypass references. |
| Cloud and infrastructure | [Cloud and Infrastructure](08-reference-library/resource-indexes/cloud-infra.md) | AWS, S3, metadata, and exposed infrastructure resources. |
| RCE, CVE, research | [RCE, CVE, and Research](08-reference-library/resource-indexes/rce-cve-research.md) | CVE, RCE, AEM, Log4j, ProxyShell, and research links. |
| Training, labs, videos | [Training, Labs, Videos, OSCP, AD, and Red Team](08-reference-library/resource-indexes/training-labs-videos.md) | Videos, OSCP, labs, AD, mindmaps, and red-team material. |

## Clean Reading Order

1. Use this page to pick a topic.
2. Open the matching category index.
3. If the category still feels too broad, use browser search inside that page.
4. Use [RESOURCES.md](RESOURCES.md) only when you need the full raw list.
5. Use [Source Resource Links](maintainers/source-resource-links.md) only when auditing exact source provenance.

## What Each Layer Means

| Layer | File | Use it for |
|---|---|---|
| Clean resource navigation | `RESOURCE-MAP.md` | Human-friendly starting point. |
| Resource-first explanation | `RESOURCE-FIRST.md` | Repository philosophy and structure. |
| Category pages | `08-reference-library/resource-indexes/*.md` | Topic-specific resource lists. |
| Exhaustive public list | `RESOURCES.md` | Every extracted URL grouped by category. |
| Source-folder exhaustive list | `08-reference-library/all-source-resources.md` | Every URL grouped by original ZIP folder/file. |
| Exact source audit | `maintainers/source-resource-links.md` | Every URL occurrence and source file. |
| Agentic verification | `maintainers/agentic-resource-audit.md` | Independent agent findings and remaining cleanup notes. |

## Known Noise

The original ZIP contained placeholders, localhost examples, payload URLs, malformed snippets, and duplicate links. They are preserved for completeness, but they are not all recommended resources.

Use category indexes for browsing. Use exhaustive lists for audit.
