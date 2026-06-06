---
title: "Injection"
summary: "Injection resources for XSS, SQL injection, XXE, and command execution topics."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
related: []
references: []
---
# Injection

Start here when user-controlled input reaches an interpreter, parser, query, shell, browser sink, or backend processor.

Injection bugs are context bugs. The same payload can be useless or dangerous depending on whether the sink is HTML, JavaScript, SQL, XML, shell, template engine, file parser, or API backend.

## Pages

- [XSS](./xss.md)
- [SQL Injection](./sqli.md)
- [XXE](./xxe.md)
- [Command Injection Payloads](../../payloads/command-injection.md)

## Method

1. Identify the sink before choosing payloads.
2. Confirm reflection, parsing, execution, query behavior, or error behavior.
3. Use low-impact payloads first.
4. Save exact requests and responses for reporting.
5. Cross-check against one writeup or cheat sheet before claiming impact.

## Related Resource Pages

- [resources/xss-and-client-side.md](../../resources/xss-and-client-side.md)
- [resources/sql-injection.md](../../resources/sql-injection.md)
- [resources/xxe-lfi-and-file-read.md](../../resources/xxe-lfi-and-file-read.md)
