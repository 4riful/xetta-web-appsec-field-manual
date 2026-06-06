---
title: "SQLi Payloads"
summary: "SQL injection payload references by validation style."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - sqli
  - payloads
related:
  - ../../03-vulnerability-guides/injection/sql-injection.md
references:
  - "https://portswigger.net/web-security/sql-injection/cheat-sheet"
  - "https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet"
---
# SQLi Payloads

## Families

- Error-based.
- Boolean-based.
- Time-based.
- UNION-based.
- JSON/body-specific cases.

## Rule

Prefer minimal proof and avoid data extraction beyond what authorization allows.
