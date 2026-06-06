---
title: "SSRF Payloads"
summary: "SSRF payload references and OOB testing patterns."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - ssrf
  - payloads
related:
  - ../../03-vulnerability-guides/server-side/ssrf.md
references:
  - "https://github.com/akincibor/SSRFexploit"
  - "https://highon.coffee/blog/ssrf-cheat-sheet/"
---
# SSRF Payloads

## Contexts

- URL parameters.
- Webhooks.
- SVG external resources.
- Document rendering.
- Cloud metadata tests where allowed.

## OOB Pattern

Use a collector you control and record timestamp, source IP, and request path.
