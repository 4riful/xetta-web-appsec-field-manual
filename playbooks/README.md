---
title: "Playbooks"
summary: "Operational workflows for turning resources into safe, repeatable AppSec work."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - playbooks
  - methodology
related:
  - ../QUICKSTART.md
  - ../bug-classes/README.md
  - ../tools/README.md
  - ../reports/README.md
references:
  - https://owasp.org/www-project-web-security-testing-guide/
  - https://owasp.org/www-project-api-security/
  - https://portswigger.net/web-security
---

# Playbooks

Playbooks connect resources, tools, bug classes, payload context, and reporting into one workflow.

Every workflow follows the same rule:

```text
authorized scope -> low-noise discovery -> hypothesis -> safe validation -> evidence -> report
```

## Playbook Index

- [Recon To First Bug](#recon-to-first-bug)
- [Black-Box Web Assessment](#black-box-web-assessment)
- [API Assessment](#api-assessment)
- [OSINT And Dorking Review](#osint-and-dorking-review)
- [Cloud Exposure Review](#cloud-exposure-review)
- [Source-Assisted Review](#source-assisted-review)
- [AI/LLM Application Review](#aillm-application-review)
- [Reporting And Evidence](#reporting-and-evidence)

## Recon To First Bug

### Goal

Move from a written scope to one meaningful, testable security hypothesis.

### Inputs

- Scope document or bug bounty brief.
- Allowed domains, IP ranges, apps, APIs, mobile apps, repositories, and cloud accounts.
- Test accounts and role matrix if available.
- Rate limits and prohibited activity list.

### Workflow

1. Normalize scope into domains, subdomains, IPs, app URLs, APIs, repositories, and exclusions.
2. Use passive discovery first: certificate names, archived URLs, GitHub search, search operators, and public asset search engines.
3. Probe only approved assets for liveness and basic metadata.
4. Collect URLs, JavaScript files, API routes, forms, upload points, redirects, webhooks, admin surfaces, and auth boundaries.
5. Triage by feature risk: auth, access control, user-controlled input, file parsing, URL fetchers, exports, imports, callbacks, and tenant boundaries.
6. Pick one bug class from [bug-classes/](../bug-classes/README.md).
7. Validate manually before running payload-heavy automation.
8. Save evidence as request, response, timestamp, account role, affected object, and impact.

### Stop Conditions

- Scope is unclear.
- The program forbids the test category.
- The test may affect other users or production availability.
- Sensitive data appears and minimal evidence is already enough.

### Output

- One validated finding, or a documented test hypothesis with why it was rejected.

## Black-Box Web Assessment

### Goal

Understand the application model before chasing payloads.

### Workflow

1. Map user roles, objects, tenants, sensitive actions, and trust boundaries.
2. Walk through login, registration, password reset, invite flows, upload/export/import, payment or billing, admin panels, API calls, and webhooks.
3. Build a small feature matrix:
   - role
   - object type
   - allowed action
   - expected denial
   - observed behavior
4. Prioritize access control early for multi-role or multi-tenant apps before spending time on lower-signal exotic classes.
5. Review session behavior: cookie attributes, logout, password reset, MFA, remember-me, and token rotation.
6. Test high-signal input surfaces after you understand the feature.
7. Document all proof with reproducible requests and account context.

### High-Value Bug Classes

- Broken object-level authorization.
- Broken function-level authorization.
- Authentication logic flaws.
- Password reset abuse.
- Stored XSS in trusted workflows.
- File upload parser abuse.
- SSRF in URL fetchers, webhooks, importers, and previewers.

## API Assessment

### Goal

Find authorization, authentication, schema, data exposure, and abuse-case issues in APIs.

### Workflow

1. Collect API routes from browser traffic, OpenAPI specs, JavaScript, mobile clients, docs, and crawlers.
2. Identify auth model: session cookie, bearer token, API key, OAuth, OIDC, JWT, mTLS, or mixed.
3. Build object and role matrices.
4. Test BOLA/IDOR with test accounts only.
5. Test property-level authorization and mass assignment.
6. Check excessive data exposure in list/detail/search endpoints.
7. Check rate limits, pagination, batching, GraphQL depth/complexity, and resource consumption safely.
8. Report impact using exact endpoint, method, role, object, and data boundary crossed.

### Primary References

- [OWASP API Security Top 10](https://owasp.org/www-project-api-security/)
- [OWASP REST Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html)
- [OWASP GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)

## OSINT And Dorking Review

### Goal

Find defensive exposure signals without creating unauthorized traffic or targeting random third parties.

Detailed guide: [OSINT And Dorking Playbook](osint-and-dorking.md)

### Safe Inputs

- `example.com` style approved domains.
- Authorized GitHub orgs/repos.
- Approved CIDR ranges.
- Approved cloud accounts and owned assets.

### Rules

- Keep placeholders generic in documentation.
- Replace placeholders only with authorized assets.
- Record minimal evidence.
- Do not download bulk documents.
- Do not use discovered secrets.
- Convert findings into remediation: remove exposure, restrict access, rotate secrets, deindex, and monitor recurrence.

Keep query patterns in the detailed [OSINT And Dorking Playbook](osint-and-dorking.md) so examples stay reviewed in one place.

## Cloud Exposure Review

### Goal

Identify cloud-facing exposure and connect it to business impact.

### Workflow

1. Confirm cloud scope and provider rules of engagement.
2. Inventory domains, certificates, buckets, CDN origins, public APIs, admin panels, and exposed metadata paths.
3. Search for leaked keys in authorized repositories.
4. Review public storage, CORS, security headers, TLS posture, and exposed debug/admin surfaces.
5. Validate ownership before reporting.
6. Sanitize evidence because cloud findings often reveal internal architecture.

### Primary References

- [AWS penetration testing policy](https://aws.amazon.com/security/penetration-testing/)
- [Microsoft security testing rules of engagement](https://www.microsoft.com/en-us/msrc/pentest-rules-of-engagement)
- [Google Cloud penetration testing FAQ](https://support.google.com/cloud/answer/6262505)

## Source-Assisted Review

### Goal

Use source code to find high-confidence issues faster than black-box guessing.

### Workflow

1. Identify routes, controllers, middleware, auth checks, object ownership checks, sinks, parsers, and external integrations.
2. Trace user-controlled input into sensitive sinks.
3. Trace auth context into object access.
4. Search for secrets and unsafe defaults.
5. Compare code paths with live behavior.
6. Report both root cause and exploitability.

### Useful Tools

- CodeQL
- Semgrep
- Gitleaks
- TruffleHog
- Dependency scanners

## AI/LLM Application Review

### Goal

Assess AI-enabled application features for prompt injection, indirect prompt injection, data leakage, unsafe tool use, RAG authorization failure, and insecure output handling.

Detailed guide: [AI/LLM Application Review Playbook](ai-llm-application-review.md)

### Inputs

- Written authorization covering AI features.
- Test accounts and roles.
- List of AI features, tools, plugins, retrieval sources, and external actions.
- Data handling rules for prompts, responses, logs, retrieved documents, and generated files.

### Workflow

1. Map AI entry points: chat, summarization, search, support bots, code assistants, agents, plugins, and API endpoints.
2. Identify model permissions: read-only, retrieval, tool calling, write actions, external requests, tickets, email, file access, or code execution.
3. Test direct prompt injection with harmless canaries.
4. Test indirect prompt injection through in-scope documents, web pages, tickets, emails, or retrieved content.
5. Check whether the model exposes hidden instructions, other users' data, secrets, internal documents, or tool schemas.
6. Check whether tool calls enforce server-side authorization independent of model output.
7. Capture minimal evidence without extracting sensitive data.
8. Report root cause as a control failure, not just a clever prompt.

### Stop Conditions

- Scope does not explicitly include AI features.
- The test may access another user's data.
- The model is about to invoke a destructive or external action.
- Sensitive information appears and minimal proof is enough.

### Output

- A validated AI feature finding, or a documented model/tool/data-flow risk assessment.

## Reporting And Evidence

### Goal

Make findings reproducible, scoped, and useful to fix.

### Minimum Report

- Summary.
- Scope and affected asset.
- Impact.
- Preconditions.
- Reproduction steps.
- Request/response evidence.
- Affected role/object/tenant.
- Expected behavior.
- Actual behavior.
- Remediation.
- References.

### Do Not

- Overclaim scanner output.
- Include raw secrets in reports unless the reporting channel explicitly supports secure secret handling.
- Dump user data.
- Use destructive proof when safer proof is enough.

Use [reports/](../reports/README.md) when a finding is reproducible.
