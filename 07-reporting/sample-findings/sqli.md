---
title: "Sample Finding: SQL Injection"
summary: "Sample structure for a SQL injection report."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - sqli
  - sample-finding
related:
  - ../../03-vulnerability-guides/injection/sql-injection.md
references: []
---
# Sample Finding: SQL Injection

## Summary

The endpoint uses user-controlled input in a database query without safe parameterization.

## Evidence To Include

- Vulnerable parameter.
- Baseline request and response.
- Proof of SQL behavior, such as error, boolean difference, or safe metadata proof.
- Impact and remediation.
