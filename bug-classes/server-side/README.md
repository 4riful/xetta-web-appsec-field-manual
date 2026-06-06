---
title: "Server-Side"
summary: "Server-side trust boundary issues including SSRF, LFI, path traversal, request smuggling, and parser behavior."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
related: []
references: []
---
# Server-Side

Server-side bugs appear where the backend fetches URLs, reads files, parses requests, normalizes paths, or talks to internal infrastructure.

## Pages

- [SSRF](./ssrf.md)
- [LFI / Path Traversal](./lfi.md)
- [Request Smuggling](./request-smuggling.md)

## Related

- [SSRF Resources](../../resources/ssrf.md)
- [XXE / LFI / File Read Resources](../../resources/xxe-lfi-and-file-read.md)
- [WAF / CORS / CSRF / Smuggling Resources](../../resources/waf-cors-csrf-smuggling.md)
