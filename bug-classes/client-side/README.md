---
title: "Client-Side"
summary: "Browser-side trust boundaries, XSS, CORS, CSRF, postMessage, JavaScript analysis, and frontend issues."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
related: []
references: []
---
# Client-Side

Client-side testing starts with browser-controlled inputs, JavaScript behavior, origins, storage, message passing, and rendering context.

Prioritize features where attacker-controlled data crosses into the browser: rendered profile fields, markdown, file previews, redirects, postMessage handlers, OAuth callbacks, embedded widgets, cross-origin APIs, and upload previews.

## Pages

- [XSS](./xss.md)
- [CORS / CSRF](./cors-and-csrf.md)

## Related

- [XSS And Client-Side Resources](../../resources/xss-and-client-side.md)
- [JavaScript Tools](../../tools/javascript-analysis.md)
- [XSS Payloads](../../payloads/xss.md)
