---
title: "API Assessment"
summary: "Workflow for REST and GraphQL API testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - api
  - workflow
related:
  - ../02-mapping-and-triage/api-surface-mapping.md
  - ../03-vulnerability-guides/api-security/rest-api-testing.md
references: []
---
# API Assessment

## Procedure

1. Identify API base URLs and versions.
2. Collect docs from Swagger/OpenAPI, GraphQL, JavaScript, and traffic.
3. Map auth and token behavior.
4. Build object and role matrices.
5. Test BOLA/IDOR, BFLA, mass assignment, excessive data exposure, and rate limits.
6. Validate findings with clean requests and role context.
