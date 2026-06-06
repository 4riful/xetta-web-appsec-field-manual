---
title: "Command Injection Payloads"
summary: "Command injection payload handling and safety notes."
status: "needs-expansion"
last_reviewed: "2026-06-06"
tags:
  - command-injection
  - payloads
related:
  - ../../03-vulnerability-guides/injection/command-injection.md
references: []
---
# Command Injection Payloads

## Safety

Use harmless commands and OOB proof where possible. Never run destructive commands.

## Proof Styles

- Timing.
- DNS/HTTP OOB callback.
- Harmless output such as username or hostname where allowed.
