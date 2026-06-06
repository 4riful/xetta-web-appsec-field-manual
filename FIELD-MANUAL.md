---
title: "Web AppSec Field Manual"
summary: "Single-page operating map for moving from scope to validated AppSec findings."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - field-manual
  - workflow
related:
  - START-HERE.md
references: []
---
# Web AppSec Field Manual

## Operating Loop

```text
scope -> assets -> live services -> URLs/endpoints -> models -> leads -> tests -> evidence -> report
```

## 1. Scope And Safety

- Confirm program scope before collecting or scanning.
- Separate root domains, wildcard domains, mobile/API assets, acquired companies, and explicitly excluded assets.
- Store tokens and API keys outside the repository.
- Prefer low-noise defaults. Escalate only when you understand rate limits and program rules.

## 2. Reconnaissance

- Build target files: `targets.txt`, `target-wildcards.txt`.
- Enumerate subdomains passively first.
- Resolve and filter wildcards.
- Probe live HTTP services.
- Mine archives and crawl only after live host validation.
- Extract JavaScript endpoints and secrets carefully.

## 3. Mapping And Triage

- Map authentication states and roles.
- Build endpoint and parameter inventories.
- Identify high-value workflows: billing, admin, team management, file handling, exports, integrations, webhooks, password reset, OAuth/SSO.
- Score leads by impact, reachability, confidence, and testing cost.

## 4. Vulnerability Testing

Test only where the model supports the bug class:

- Access control bugs need multiple users, roles, or tenants.
- SSRF needs URL-fetching behavior or server-side callbacks.
- XSS needs controllable input rendered in an executable context.
- SQLi needs query-like parameters, errors, timing behavior, or database-backed filters.
- File upload bugs need parser, storage, transformation, or serving behavior.

## 5. Evidence

Good evidence contains:

- exact request,
- exact response,
- account/role context,
- affected asset,
- reproducible steps,
- impact statement,
- safe proof of impact.

## 6. Report

Use `07-reporting/report-template.md`. The best report explains what broke, why it matters, how to reproduce it, and how to fix it without overselling scanner output.
