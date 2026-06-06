---
title: "Evidence Standards"
summary: "Minimum evidence requirements for reliable AppSec reports."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - evidence
  - reporting
related:
  - report-template.md
references: []
---
# Evidence Standards

## Required Evidence

- Exact request and response.
- Target asset and endpoint.
- Account, role, and tenant context.
- Timestamp.
- Before/after state when testing state changes.
- Explanation of why this is unauthorized or unsafe.

## Optional Evidence

- Screenshots.
- OOB logs.
- Minimal proof files.
- Source-code references when source-assisted.

## Avoid

- Scanner screenshots without reproduction.
- Claims about data you did not access or prove.
- Real user data when test-account proof is enough.
