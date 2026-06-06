---
title: "Playbooks"
summary: "Compact workflows for turning resources into an actual testing process."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - playbooks
related: []
references: []
---
# Playbooks

These are short workflows that connect the vault sections.

## Recon To First Bug

1. Build a target list from scope and public asset sources.
2. Expand assets with [resources/recon-and-osint.md](../resources/recon-and-osint.md).
3. Probe live hosts with tools from [tools/recon.md](../tools/recon.md).
4. Collect URLs, JavaScript, endpoints, and parameters.
5. Triage by signal: auth boundary, user-controlled input, file parsing, URL fetchers, admin surfaces, and old endpoints.
6. Pick one bug class from [bug-classes/](../bug-classes/README.md).
7. Use payloads from [payloads/](../payloads/README.md) only after there is a reason to test.

## Black-Box Web Assessment

Focus on the application model first.

- Identify roles, objects, tenants, and sensitive workflows.
- Map login, password reset, upload, export, import, webhook, and API features.
- Test access control before chasing exotic payloads.
- Keep requests, responses, screenshots, and timestamps for reporting.

## API Assessment

- Start with [resources/api-auth-oauth-and-graphql.md](../resources/api-auth-oauth-and-graphql.md).
- Collect endpoints from JavaScript, traffic, docs, mobile apps, and crawlers.
- Test auth, object access, mass assignment, rate limits, GraphQL introspection, and excessive data exposure.
- Use [tools/api-graphql.md](../tools/api-graphql.md) for API-specific tooling.

## Cloud Exposure Review

- Start with [resources/cloud-and-infrastructure.md](../resources/cloud-and-infrastructure.md).
- Look for public buckets, metadata exposure, leaked keys, cloud-hosted admin panels, and storage misconfigurations.
- Connect cloud findings back to real business impact before reporting.

## Report Writing

- Use [reports/](../reports/README.md) when a finding is reproducible.
- Include summary, affected asset, steps, evidence, impact, and remediation.
- Do not overclaim scanner output. Prove the behavior.
