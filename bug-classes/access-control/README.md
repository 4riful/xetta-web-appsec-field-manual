---
title: "Access Control"
summary: "Authorization, IDOR, 403 bypass, object ownership, and business logic access testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
related: []
references: []
---
# Access Control

Access-control bugs happen when a feature trusts the wrong user, role, object ID, tenant, method, or workflow state.

Start here when recon finds user-owned objects, admin-only routes, numeric IDs, exported files, hidden endpoints, or role-specific actions.

## Pages

- [Access Control Resources](./access-control.md)

## Related

- [API Resources](../api/README.md)
- [Bug Bounty Writeups](../../resources/bug-bounty-writeups-blogs-and-gitbooks.md)
- [Reporting](../../reports/README.md)
