---
title: "Reporting"
summary: "Evidence, severity, remediation, and report-writing guidance for reproducible AppSec findings."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - reports
related: []
references: []
---
# Reporting

Use this section after you have reproducible behavior that crosses a security boundary or demonstrates a meaningful control failure.

A finding is not ready because a scanner flagged it. A finding is ready when the behavior, boundary, impact, and remediation are clear.

## Report-Ready Checklist

- [ ] Asset is in scope.
- [ ] Affected feature is identified.
- [ ] Affected role, account, object, tenant, or data boundary is clear.
- [ ] Expected behavior is stated.
- [ ] Actual behavior is reproducible.
- [ ] Evidence is minimal and safe.
- [ ] Impact is realistic and not overclaimed.
- [ ] Root cause is described.
- [ ] Remediation is actionable.
- [ ] Retest steps are included.

## Report Skeleton

```markdown
# Summary

# Affected Asset

# Affected Feature Or Endpoint

# Preconditions

# Steps To Reproduce

# Evidence

# Impact

# Remediation

# Retest Notes

# References
```

## Summary

Use one or two sentences:

> A [role/user/system] can [unauthorized action] against [asset/object/data] because [control failure]. This can result in [impact].

## Affected Asset

Include:

- domain, app, API, repository, or cloud asset
- environment
- endpoint or feature
- role/account type
- tenant, object, or data boundary

## Preconditions

Include:

- required account role
- required object state
- required feature flag/subscription
- required API token/session
- required test data

## Steps To Reproduce

Good steps are:

- numbered
- minimal
- deterministic
- scoped to test accounts
- free of unnecessary data access
- paired with exact requests/responses where useful

## Evidence Standards

- Save the raw request and response.
- Capture the affected account, role, tenant, object ID, or workflow.
- Include timestamps and environment details.
- Add screenshots only when they clarify the finding.
- Avoid destructive proof. Show impact safely.
- Redact secrets, tokens, PII, prompts, customer data, and internal URLs unless the detail is required and authorized.

## Impact

Describe what the vulnerability allows in realistic terms.

Avoid:

- “full account takeover” unless proven
- “critical” based only on theoretical chaining
- inflated data exposure claims
- assumptions about internal architecture

## Severity Thinking

- Low: limited exposure, hard-to-abuse behavior, weak but real control gap.
- Medium: meaningful unauthorized action or data exposure under constraints.
- High: account-level compromise, cross-tenant data access, significant privilege escalation, or sensitive data exposure.
- Critical: reliable remote code execution, mass compromise, systemic auth bypass, destructive unauthenticated impact, or broad data compromise.

Severity factors:

- authentication required
- privileges required
- user interaction
- exploit reliability
- data sensitivity
- scope breadth
- tenant/user isolation impact
- availability impact
- compensating controls

## Remediation Language

Good remediation explains the root cause and control.

Examples:

- enforce object authorization server-side
- validate ownership on every request
- bind password reset tokens to user/session/action/expiry
- validate and encode output by context
- restrict server-side URL fetch destinations
- enforce parser allowlists
- apply API schema validation
- enforce RAG/document ACLs before retrieval
- reduce tool permissions for AI agents
- add audit logging and regression tests

## Retest Notes

Include:

- exact request or workflow to replay
- expected fixed behavior
- negative and positive test cases
- regression test recommendation

## Common Reporting Mistakes

- reporting scanner output without validation
- omitting role/object context
- overclaiming impact
- including too much sensitive data
- failing to explain root cause
- recommending only generic input validation
- missing retest criteria

## Evidence Handling

Treat secrets, tokens, prompts, PII, customer data, internal URLs, retrieved documents, and AI context as sensitive evidence.
