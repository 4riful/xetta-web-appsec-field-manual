---
title: "Authorization Modeling"
summary: "Build role and object models for IDOR, 403 bypass, and business logic testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - authorization
  - idor
  - triage
related:
  - ../03-vulnerability-guides/access-control/idor.md
  - ../03-vulnerability-guides/access-control/403-bypass.md
references: []
---
# Authorization Modeling

## Required Setup

Create at least two normal users. If allowed, add different roles or tenants.

## Role Matrix

| Role | Can read | Can write | Can invite | Can export | Can administer |
|---|---|---|---|---|---|
| User A | own objects | own objects | no | own exports | no |
| User B | own objects | own objects | no | own exports | no |
| Admin | team objects | team objects | yes | team exports | yes |

## Object Matrix

Track object IDs across accounts:

- user IDs,
- organization IDs,
- project IDs,
- file IDs,
- invoice/order IDs,
- API token IDs.

## Testable Leads

- Same endpoint accepts object IDs from another user.
- API response includes objects beyond the visible UI.
- 403 response changes with method, path, headers, or content type.
- UI hides actions but API still executes them.
