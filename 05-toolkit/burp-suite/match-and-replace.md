---
title: "Match and Replace"
summary: "Using Burp match-and-replace for OOB headers and controlled testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - burp
  - match-and-replace
related:
  - ../../03-vulnerability-guides/injection/xss.md
  - ../../03-vulnerability-guides/server-side/ssrf.md
references: []
---
# Match and Replace

## Use Cases

- Blind XSS header testing.
- OOB SSRF callback markers.
- Temporary header instrumentation.

## Source-Derived Blind XSS Headers

```text
Referer: https://xss.example
User-Agent: https://xss.example
```

Use a collector you control and only on authorized targets.
