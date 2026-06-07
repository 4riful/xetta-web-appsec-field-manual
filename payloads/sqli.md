---
title: "SQLi Payload Context"
summary: "Safe SQL injection payload context notes for authorized testing after a query hypothesis exists."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - payloads
  - sqli
related:
  - ../bug-classes/injection/sqli.md
  - ../reports/README.md
references:
  - https://portswigger.net/web-security/sql-injection/cheat-sheet
  - https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
---

# SQLi Payload Context

Use this page only after you have a SQL injection hypothesis for an in-scope feature.

Payloads should prove query influence with the least possible impact. They should not dump data, alter data, execute OS commands, or stress the database unless the engagement explicitly authorizes that testing.

## Use When

- A parameter, JSON field, cookie, header, sort field, or filter appears to influence a database query.
- You have a baseline request and expected behavior.
- You can test with a controlled account and minimal data access.

## Safe First Checks

- Syntax boundary checks that do not reveal data.
- Boolean-style comparisons that only change response shape.
- Small timing checks within agreed limits.
- Error observation without forcing large query work.

## Stop Conditions

Stop when:

- unauthorized data appears
- the database or app slows unexpectedly
- a tool attempts enumeration or extraction
- the test would require destructive operations
- scope does not explicitly allow deeper database testing

## Evidence

Keep the original request, modified request, responses, timing/context notes, and the reason the behavior indicates query influence. Report the control failure, not the payload string.

## Related Bug Class

- [SQL Injection](../bug-classes/injection/sqli.md)
