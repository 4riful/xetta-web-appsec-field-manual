---
title: "Reporting"
summary: "Evidence, severity, remediation, and report-writing guidance."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - reports
related: []
references: []
---
# Reporting

Use this section after you have a reproducible finding.

## Report Skeleton

```markdown
# Summary

# Affected Asset

# Preconditions

# Steps To Reproduce

# Evidence

# Impact

# Remediation

# Retest Notes
```

## Evidence Standards

- Save the raw request and response.
- Capture the affected account, role, tenant, object ID, or workflow.
- Include timestamps and environment details.
- Add screenshots only when they clarify the finding.
- Avoid destructive proof. Show impact safely.

## Severity Thinking

- Low: limited information disclosure or weak signal.
- Medium: meaningful data exposure, workflow bypass, or scoped unauthorized action.
- High: account-level compromise, cross-tenant data access, significant privilege escalation, or sensitive data exposure.
- Critical: reliable remote code execution, mass compromise, or systemic compromise path.

## Remediation Language

- Explain the root cause, not only the payload.
- Recommend validation on the server side.
- Mention authorization checks, input validation, output encoding, parser hardening, secure defaults, or cloud policy changes where relevant.
- Include retest steps that confirm the fix.
