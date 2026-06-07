---
title: "Resources"
summary: "Curated reference map for standards, labs, writeups, tools, payload references, and source material."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - resources
related:
  - ../QUICKSTART.md
  - ../playbooks/README.md
  - ../awesome-lists/top-25-web-appsec-links.md
  - ../data/resources.csv
  - ../provenance/source-catalog.md
references: []
---
# Resources

Use this section to find reputable references after you know what you are trying to learn, test, validate, or remediate.

This is not the first stop during an assessment. Start with [Quickstart](../QUICKSTART.md), [Playbooks](../playbooks/README.md), and [Bug Classes](../bug-classes/README.md). Use resources to deepen or verify a specific topic.

## Resource Trust Model

| Type | Use for | Trust note |
|---|---|---|
| Standards and official docs | methodology and requirements | highest confidence |
| Labs and training | safe practice | use before live testing |
| Original research | patterns and root causes | verify freshness |
| Public reports/writeups | examples and report quality | do not cargo-cult payloads |
| Tools | workflow support | validate output manually |
| Payload references | input ideas | use only with context |
| Imported/generated data | search and triage | not reviewed guidance |

## Best Starting Points

- [Top 25 Web AppSec Links](../awesome-lists/top-25-web-appsec-links.md)
- OWASP WSTG
- OWASP ASVS
- OWASP Cheat Sheet Series
- OWASP API Security Top 10
- PortSwigger Web Security Academy
- OWASP Top 10 for LLM Applications
- MDN Web Security
- Burp Suite Documentation

## Browse By Topic

Use [data/resources.csv](../data/resources.csv) for the full database view.

- [AI/LLM Security](./ai-llm-security.md) — curated standards, labs, tools, and safe prompt-injection references
- [API, Auth, OAuth, and GraphQL](./api-auth-oauth-and-graphql.md) — API authorization, schema, token, and identity references
- [Bug Bounty Writeups, Blogs, and GitBooks](./bug-bounty-writeups-blogs-and-gitbooks.md) — pattern mining and report-quality examples
- [Burp Suite and Tooling](./burp-suite-and-tooling.md) — proxy workflows and tool documentation
- [Cloud and Infrastructure](./cloud-and-infrastructure.md) — cloud exposure and provider testing rules
- [File Upload and Parser Abuse](./file-upload-and-parser-abuse.md) — parser, upload, archive, SVG/XML/PDF references
- [Mixed and Extra Resources](./mixed-and-extra-resources.md) — useful but less curated or cross-topic material
- [Payloads, Cheat Sheets, and Wordlists](./payloads-cheat-sheets-and-wordlists.md) — context-dependent testing aids
- [RCE, CVEs, and 0days](./rce-cves-and-0days.md) — historical research and prioritization context, not a testing plan
- [Recon and OSINT](./recon-and-osint.md) — asset discovery and public exposure references
- [SQL Injection](./sql-injection.md) — SQLi learning, detection, and remediation references
- [SSRF](./ssrf.md) — URL fetcher and server-side request boundary references
- [Training, Labs, Videos, OSCP, AD, and Red Team](./training-labs-videos-oscp-ad-and-red-team.md) — learning material; not all web-app-specific
- [WAF, CORS, CSRF, Smuggling](./waf-cors-csrf-smuggling.md) — browser/proxy/filter edge cases
- [XSS and Client-Side](./xss-and-client-side.md) — browser execution and client-side bug references
- [XXE, LFI, and File Read](./xxe-lfi-and-file-read.md) — file parser and local file access references

## How To Use A Resource

For each resource, ask:

- Is it official, original, or a repost?
- Is it current?
- Is it lab-safe or live-target oriented?
- Does it explain root cause?
- Does it include remediation?
- Does it apply to my bug class?
- Does it require special authorization?

## Raw Database

The raw database is useful for search and triage:

- [data/resources.csv](../data/resources.csv)
- [data/resources.json](../data/resources.json)
- [provenance/source-catalog.md](../provenance/source-catalog.md)

Do not treat imported/generated entries as reviewed instructions until they pass the [content quality checklist](../maintainers/content-quality-checklist.md).

## Curation Criteria

A resource belongs in reviewed pages when it has:

- a canonical URL
- a clear reason for inclusion
- topic relevance
- safe usage guidance
- no duplicate better source
- no private/login-only dependency unless intentionally documented

## When Not To Use Resources

Do not use resources as a substitute for understanding scope, target behavior, evidence, or authorization.
