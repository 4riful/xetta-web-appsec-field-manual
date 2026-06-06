---
title: "Application Mapping"
summary: "Map features, routes, state changes, and trust boundaries before testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - application-mapping
  - triage
related:
  - finding-testable-leads.md
references: []
---
# Application Mapping

## What To Map

- Entry points: web, API, mobile backend, admin, integrations.
- Roles: anonymous, user, manager, admin, tenant owner, support.
- Objects: users, teams, organizations, projects, invoices, files, API tokens.
- State changes: create, update, delete, approve, export, import, invite, transfer.
- Trust boundaries: user-to-user, tenant-to-tenant, client-to-server, server-to-cloud.

## Workflow

1. Browse manually with Burp running.
2. Capture requests for every important feature.
3. Group endpoints by feature, not by URL alone.
4. Mark parameters that identify users, tenants, files, or permissions.
5. Link each feature to likely vulnerability guides.

## Output Format

| Feature | Endpoint | Method | Auth required | Object IDs | Notes |
|---|---|---|---|---|---|
| Team invite | `/api/teams/{id}/invites` | POST | yes | team ID | test authorization and email change flows |
