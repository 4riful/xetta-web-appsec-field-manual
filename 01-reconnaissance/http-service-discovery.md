---
title: "HTTP Service Discovery"
summary: "Probing resolved hosts and deciding what deserves deeper testing."
status: "needs-expansion"
last_reviewed: "2026-06-06"
tags:
  - recon
  - httpx
  - live-hosts
related:
  - subdomain-enumeration.md
  - recon-triage.md
references: []
---
# HTTP Service Discovery

## Goal

Convert resolved hosts into a useful live-service inventory.

## Capture

For each live host, record:

- URL,
- status code,
- title,
- redirect chain,
- technology hints,
- content length,
- interesting ports,
- authentication requirement.

## Output

- `hosts-http.txt`
- `hosts-interesting.txt`
- `technologies.txt`

## What To Prioritize

- Admin or staff portals.
- Staging/dev/qa hosts.
- Old frameworks or legacy extensions.
- Unusual ports.
- Swagger/OpenAPI docs.
- Login, upload, export, billing, team, and integration surfaces.

## Gap Note

The source corpus did not contain a clean live-host probing workflow. This page defines the expected bridge between subdomain enumeration and deeper recon.
