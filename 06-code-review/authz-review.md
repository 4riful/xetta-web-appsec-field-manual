---
title: "Authorization Review"
summary: "Code-review checklist for authorization and IDOR bugs."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - authorization
  - code-review
related:
  - ../03-vulnerability-guides/access-control/idor.md
references: []
---
# Authorization Review

## Check

- Every object read checks ownership or permission.
- Every state change checks role and tenant.
- Authorization is enforced server-side, not only in UI.
- Collection endpoints filter by current user/tenant.
- Background jobs do not bypass permission checks.
