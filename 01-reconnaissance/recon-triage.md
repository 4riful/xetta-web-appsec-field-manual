---
title: "Recon Triage"
summary: "How to turn recon output into prioritized testing leads."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - triage
related:
  - ../02-mapping-and-triage/finding-testable-leads.md
references: []
---
# Recon Triage

## Lead Quality

Good leads have at least one of:

- high-value feature,
- authentication or authorization boundary,
- user-controlled input,
- server-side fetch or parser behavior,
- sensitive file handling,
- old or unusual technology,
- admin or internal naming.

## Prioritization Table

| Signal | Likely follow-up |
|---|---|
| Object IDs in URLs/API bodies | Access control / IDOR |
| URL, callback, webhook parameters | SSRF / open redirect |
| Upload/import/export features | File upload / parser abuse |
| GraphQL endpoint | GraphQL authorization and introspection |
| Login/reset/MFA routes | Auth and account recovery |
| Swagger/OpenAPI docs | API mapping |
| Staging/dev hosts | Access control, secrets, debug exposure |

## Stop Conditions

Stop broad recon when you have enough high-quality leads to test manually. More data is not automatically better.
