---
title: "Burp Proxy Setup"
summary: "Baseline Burp proxy setup for browser and CLI-assisted testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - burp
  - proxy
related:
  - repeater-workflows.md
references: []
---
# Burp Proxy Setup

## Browser

- Use a dedicated browser profile.
- Install Burp CA certificate.
- Keep test accounts separate from personal accounts.

## CLI Through Burp

```bash
curl --proxy http://127.0.0.1:8080 -sk https://example.com/
```

Use CLI proxying for selected requests, not high-volume scans by default.
