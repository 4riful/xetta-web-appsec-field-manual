---
title: "Severity Rating"
summary: "Impact-focused severity guidance for AppSec findings."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - severity
  - reporting
related:
  - evidence-standards.md
references: []
---
# Severity Rating

## Severity Inputs

- Data sensitivity.
- Number of affected users or tenants.
- Privilege level gained.
- Authentication required.
- Exploit reliability.
- Business process affected.

## Impact Examples

| Severity | Typical example |
|---|---|
| Low | limited metadata exposure or best-practice gap |
| Medium | unauthorized access to low-sensitivity user data |
| High | cross-user or cross-tenant sensitive data access, privilege escalation |
| Critical | account takeover, RCE, broad tenant compromise, key material exposure |

## Rule

Do not inflate severity. Explain the actual impact you proved.
