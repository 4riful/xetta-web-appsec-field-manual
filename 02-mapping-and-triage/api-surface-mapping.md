---
title: "API Surface Mapping"
summary: "Map REST, GraphQL, mobile, and JavaScript-discovered APIs before testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - api
  - mapping
related:
  - ../03-vulnerability-guides/api-security/rest-api-testing.md
  - ../03-vulnerability-guides/api-security/graphql.md
references: []
---
# API Surface Mapping

## Sources

- JavaScript bundles.
- Swagger/OpenAPI docs.
- Mobile traffic.
- Burp history.
- Archive URLs.
- GraphQL introspection when allowed.

## Capture

- base URL,
- version,
- authentication method,
- content type,
- endpoint list,
- parameters and JSON fields,
- object identifiers,
- role requirements,
- rate limits.

## Prioritize

Focus on APIs that handle identity, money, files, tenant data, admin features, exports, webhooks, or integrations.
