---
title: "SQL Injection"
summary: "Methodology for testing database-backed input safely during authorized assessments."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - bug-class
  - injection
  - sqli
related:
  - ../../payloads/sqli.md
  - ../../reports/README.md
  - ../../tools/README.md
references:
  - https://portswigger.net/web-security/sql-injection
  - https://portswigger.net/web-security/sql-injection/cheat-sheet
  - https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html
  - https://bobby-tables.com/
---

# SQL Injection

SQL injection happens when user-controlled input changes how an application builds or executes a database query.

Use this page to decide whether a database-backed feature has a real query-control failure. Do not start with automated dumping or destructive payloads.

## What Fails

- Query parameters, filters, sort fields, JSON bodies, headers, or cookies are concatenated into SQL.
- Backend code trusts client-supplied field names, operators, or object identifiers.
- Error handling exposes query structure or database details.
- Different database contexts are mixed without parameterization or allowlists.

## Where It Appears

- Search and filter forms.
- Reporting/export endpoints.
- Login and account lookup flows.
- Admin panels and analytics dashboards.
- API endpoints accepting JSON filters or query builders.
- Legacy applications with hand-built SQL strings.

## Signals

- Input changes the number, order, or content of returned rows unexpectedly.
- Syntax-like characters cause database-flavored errors.
- Boolean-style changes produce different responses.
- Time-like probes create controlled response differences.
- A filter accepts operators, column names, sort fields, or raw fragments.

## Preconditions

- The asset and endpoint are in scope.
- You have a test account or authorized unauthenticated flow.
- You understand expected behavior for the feature.
- You can test without dumping data, changing data, or stressing the database.

## Safe Test Path

1. Capture a normal request and response.
2. Identify the smallest input that may reach a query.
3. Change one variable at a time.
4. Look for controlled differences in status, content, row count, errors, or timing.
5. Stop when query influence is proven.
6. Do not enumerate tables, dump records, write files, execute OS commands, or extract secrets unless explicitly authorized.

## Tool-Assisted Checks

Tools can help confirm patterns, but tool output alone is not a finding.

- Use manual replay first.
- If automation is authorized, use low risk settings and strict scope.
- Save the exact request used as input to the tool.
- Validate any tool result manually before reporting.

## Payload Context

Use [SQLi payload context](../../payloads/sqli.md) only after you know the parameter and expected behavior. Prefer syntax/boolean/timing checks that do not reveal or modify data.

## Evidence Checklist

- In-scope asset and endpoint.
- Original request and response.
- Modified request and response.
- Expected behavior and actual behavior.
- Role/account used.
- Minimal proof of query influence.
- Redaction notes if any sensitive data appeared.
- Remediation and retest guidance.

## Common False Positives

- Generic application errors unrelated to database parsing.
- Search behavior that naturally changes with punctuation.
- Cache or rate-limit timing differences.
- Tool signatures that do not reproduce manually.
- Expected admin-only query features in authorized admin contexts.

## Impact And Severity

Severity increases when the issue allows unauthorized data access, authentication bypass, cross-tenant data exposure, data modification, or reliable extraction at scale.

Severity decreases when the behavior is limited to harmless error disclosure, requires high privilege, or cannot affect protected data.

## Remediation

- Use parameterized queries or safe ORM query builders.
- Avoid string concatenation for query values.
- Allowlist sortable/filterable column names and operators.
- Validate JSON query builders server-side.
- Return generic errors to users while logging details securely.
- Add regression tests for the affected parameter and similar query paths.

## References

- [PortSwigger SQL injection](https://portswigger.net/web-security/sql-injection)
- [PortSwigger SQL injection cheat sheet](https://portswigger.net/web-security/sql-injection/cheat-sheet)
- [OWASP SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [Bobby Tables](https://bobby-tables.com/)
