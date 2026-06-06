---
title: "Sample Finding: XSS"
summary: "Sample structure for an XSS report."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - xss
  - sample-finding
related:
  - ../../03-vulnerability-guides/injection/xss.md
references: []
---
# Sample Finding: XSS

## Summary

User-controlled input is rendered in an executable browser context without proper encoding.

## Evidence To Include

- Injection request.
- Rendered response context.
- Browser execution proof.
- Affected user role and impact path.
