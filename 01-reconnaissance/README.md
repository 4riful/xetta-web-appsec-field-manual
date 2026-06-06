---
title: "Reconnaissance"
summary: "Operator workflows for asset discovery, URL mining, JavaScript recon, content discovery, and lead generation."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - asset-discovery
related:
  - ../02-mapping-and-triage/README.md
references: []
---
# Reconnaissance

## Goal

Turn authorized scope into a clean set of live assets, endpoints, files, parameters, technologies, and candidate leads.

## Recommended Order

1. [Workflow](workflow.md)
2. [Asset Inventory](asset-inventory.md)
3. [Subdomain Enumeration](subdomain-enumeration.md)
4. [HTTP Service Discovery](http-service-discovery.md)
5. [Virtual Host Discovery](virtual-host-discovery.md)
6. [URL and Archive Recon](url-and-archive-recon.md)
7. [JavaScript Recon](javascript-recon.md)
8. [Content Discovery](content-discovery.md)
9. [Recon Triage](recon-triage.md)

## Output Contract

Recon should produce files that other phases can consume: `hosts-http.txt`, `urls-archive.txt`, `jsfiles.txt`, `js-endpoints.txt`, and `content-hits.txt`.
