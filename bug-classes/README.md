---
title: "Bug Classes"
summary: "Vulnerability families grouped by how a learner or hunter should approach testing."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-classes
related: []
references: []
---
# Bug Classes

Use this section after recon gives you a signal. Do not start with payloads. Start with the feature, trust boundary, parser, or protocol behavior that makes a bug class worth testing.

## Main Families

- [Access Control](./access-control/README.md): IDOR, object ownership, role boundaries, 403 bypass, and business logic access mistakes.
- [Authentication](./auth/README.md): auth bypass, account takeover, password reset, OAuth/SSO, and login flow weaknesses.
- [Injection](./injection/README.md): XSS, SQL injection, XXE, command execution, and related input-to-execution bugs.
- [Server-Side](./server-side/README.md): SSRF, LFI/path traversal, request smuggling, and server-side trust boundary issues.
- [Files And Parsers](./files-parsers/README.md): upload, parser confusion, archive handling, SVG/XML/PDF/document processing.
- [API](./api/README.md): API auth, GraphQL, endpoint discovery, mass assignment, rate limits, and object access.
- [Client-Side](./client-side/README.md): browser trust boundaries, CORS/CSRF, DOM behavior, and XSS-adjacent client-side issues.
- [Cloud](./cloud/README.md): S3, metadata exposure, cloud assets, storage misconfiguration, and leaked cloud material.
- [Defensive Bypass](./defensive-bypass/README.md): WAF bypass, filtering weaknesses, encoding, and platform/proxy edge cases.
- [AI And LLM](./ai-llm/README.md): prompt injection, indirect prompt injection, RAG, agents, tool calling, and LLM app data leakage.

## How To Use

1. Pick the family that matches the signal you found.
2. Open the matching resource page and one related writeup.
3. Use payload pages only after the feature appears testable.
4. Capture evidence with [reports/](../reports/README.md) once behavior is reproducible.
