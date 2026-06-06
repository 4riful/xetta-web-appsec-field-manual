---
title: "XSS Payloads"
summary: "XSS payload references and usage context."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - xss
  - payloads
related:
  - ../../03-vulnerability-guides/injection/xss.md
references:
  - "https://portswigger.net/web-security/cross-site-scripting/cheat-sheet"
  - "https://github.com/RenwaX23/XSS-Payloads/blob/master/Payloads.txt"
  - "https://tinyxss.terjanq.me/"
---
# XSS Payloads

## Use Cases

- Context discovery.
- Payload minimization.
- WAF/filter behavior testing.
- Blind XSS markers.

## Rule

Always identify the execution context before escalating payload complexity.
