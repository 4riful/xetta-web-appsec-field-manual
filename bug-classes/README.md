---
title: "Bug Classes"
summary: "Decision guide for choosing vulnerability families based on features, trust boundaries, and observed signals."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-classes
related:
  - ../QUICKSTART.md
  - ../playbooks/README.md
  - ../payloads/README.md
  - ../reports/README.md
references: []
---
# Bug Classes

Use this section after recon gives you a signal. Do not start with payloads. Start with the feature, trust boundary, parser, or protocol behavior that makes a bug class worth testing.

## How To Choose A Bug Class

Ask:

1. What feature am I testing?
2. What trust boundary should protect it?
3. What user-controlled input, identity, object, state, parser, or protocol behavior affects it?
4. What should happen?
5. What behavior would prove a control failure safely?

## Decision Table

| Signal | Likely family | Start here |
|---|---|---|
| Object IDs, tenant IDs, role-specific actions | Access Control | [Access Control](./access-control/README.md) |
| Login, reset, invite, MFA, sessions, SSO | Authentication | [Authentication](./auth/README.md) |
| API routes, mobile backend, GraphQL, OpenAPI | API | [API](./api/README.md) |
| Browser rendering, DOM sinks, CORS/CSRF | Client-Side | [Client-Side](./client-side/README.md) |
| Search, filters, SQL-like errors, templates | Injection | [Injection](./injection/README.md) |
| URL importers, webhooks, previewers, metadata | Server-Side | [Server-Side](./server-side/README.md) |
| Uploads, converters, archives, XML/SVG/PDF | Files and Parsers | [Files And Parsers](./files-parsers/README.md) |
| Buckets, cloud metadata, exposed keys | Cloud | [Cloud](./cloud/README.md) |
| WAF, filter, proxy, encoding, normalization | Defensive Bypass | [Defensive Bypass](./defensive-bypass/README.md) |
| Chat, RAG, tools, agents, memory | AI and LLM | [AI And LLM](./ai-llm/README.md) |

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

## Standard Bug-Class Page Shape

Every bug-class page should answer:

- What fails?
- Where does it appear?
- What are the signals?
- What are the preconditions?
- What is the safe manual test path?
- What tools can help without replacing validation?
- What payload context applies?
- What evidence proves the behavior?
- What are common false positives?
- What makes severity higher or lower?
- What remediation addresses the root cause?
- What references are worth reading?

## Hypothesis Template

> Because [feature] accepts or influences [input/state], [role/user/system] may be able to [unauthorized behavior] across [trust boundary], resulting in [impact].

Examples:

- A standard user may access another user’s invoice by changing an invoice ID.
- A support bot may retrieve documents from another tenant because retrieval filters are not enforced server-side.
- A URL previewer may fetch internal metadata because outbound requests are not restricted.

## How To Use This Section

1. Pick the family that matches the signal you found.
2. Open the family index and the most relevant canonical page.
3. Write a hypothesis before choosing tools or payloads.
4. Use [tools](../tools/README.md) only to support a job you can explain.
5. Use [payloads](../payloads/README.md) only after the input context and sink/parser are clear.
6. Capture evidence with [Reports](../reports/README.md) once behavior is reproducible.

## Reporting Expectations

Link every validated bug-class finding to:

- affected asset
- affected role, object, tenant, or data boundary
- expected behavior
- actual behavior
- reproducible request/response or trace
- realistic impact
- remediation and retest guidance

## When Not To Continue

Stop when:

- scope does not include the feature
- the test requires another user’s real data
- only scanner output exists
- behavior is expected by documented role permissions
- validation would be destructive or availability-impacting
