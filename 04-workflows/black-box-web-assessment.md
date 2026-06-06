---
title: "Black-Box Web Assessment"
summary: "Workflow for assessing a web app without source code."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - black-box
  - workflow
related:
  - ../01-reconnaissance/README.md
  - ../02-mapping-and-triage/README.md
references: []
---
# Black-Box Web Assessment

## Inputs

- Scope.
- Test accounts.
- Application URLs.
- Rules of engagement.

## Procedure

1. Browse the application manually.
2. Capture traffic with Burp.
3. Map roles, endpoints, and state-changing actions.
4. Test access control first.
5. Test input-handling bugs where reflections, parsers, or queries are likely.
6. Test file, export, webhook, and integration flows.
7. Report only stable, reproducible findings.
