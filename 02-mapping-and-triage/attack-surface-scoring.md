---
title: "Attack Surface Scoring"
summary: "Rank assets and features by impact, reachability, confidence, and testing cost."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - triage
  - prioritization
related:
  - finding-testable-leads.md
references: []
---
# Attack Surface Scoring

## Score Dimensions

| Dimension | High score means |
|---|---|
| Impact | bug could expose data, money, admin control, code execution, or cross-tenant access |
| Reachability | feature is accessible with your account and scope |
| Confidence | recon signal maps clearly to a bug class |
| Novelty | endpoint or feature is less likely to be heavily tested |
| Cost | manual validation is practical and safe |

## High-Value Surfaces

- Admin portals.
- Upload/import/export.
- Billing, invoices, orders, coupons.
- Teams, tenants, invites, roles.
- Webhooks and integrations.
- GraphQL and undocumented APIs.
- Cloud storage and metadata pivots.
