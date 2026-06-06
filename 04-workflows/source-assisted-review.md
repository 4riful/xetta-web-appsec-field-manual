---
title: "Source-Assisted Review"
summary: "Workflow for combining source-code review with dynamic validation."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - code-review
  - workflow
related:
  - ../06-code-review/review-methodology.md
references: []
---
# Source-Assisted Review

## Procedure

1. Identify routes, controllers, and handlers.
2. Map sources: requests, headers, files, cookies, webhooks, queues.
3. Map sinks: database queries, shell commands, file paths, URL fetchers, template renderers.
4. Trace authorization checks before sensitive operations.
5. Validate candidate bugs dynamically when possible.
6. Report the vulnerable flow with both code and request evidence.
