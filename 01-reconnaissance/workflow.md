---
title: "Reconnaissance Workflow"
summary: "A controlled recon sequence from scope intake to testable leads."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - workflow
related:
  - asset-inventory.md
  - ../02-mapping-and-triage/finding-testable-leads.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things 08b9dadb798c4fc194be6627a7ef998b.md"
references: []
---
# Reconnaissance Workflow

## Workflow Overview

```text
scope -> targets -> subdomains -> resolved hosts -> live services -> URLs -> JS endpoints -> content discovery -> triage
```

## 1. Target Intake

Create stable input files:

- `targets.txt`: root domains and explicit domains.
- `target-wildcards.txt`: wildcard scope only.
- `program-notes.md`: scope rules, exclusions, rate limits, and credentials provided by the program.

## 2. Passive Asset Discovery

Use public datasets, certificate transparency, internet search engines, and bounty scope lists before active brute force. Passive recon is safer and gives broad coverage.

## 3. Subdomain Enrichment

Combine passive enumeration, active brute force, permutations, and resolution. Filter wildcard DNS before trusting output.

## 4. Live Service Discovery

Probe resolved hosts for HTTP/S services. Capture status code, title, server, technology, redirect, and content length. Only live services should feed deeper crawling or archive replay.

## 5. Archive And URL Mining

Use archive sources to recover old endpoints, parameters, file paths, and API routes. Deduplicate aggressively before classification.

## 6. JavaScript Recon

Extract JavaScript files from live hosts and archives. Look for endpoints, feature flags, secrets, internal route names, and API base URLs.

## 7. Content Discovery

Run content discovery only after you know the host is in scope and alive. Start with targeted wordlists and low concurrency.

## 8. Lead Generation

Classify URLs and parameters into bug-class leads:

- SQL-like inputs.
- Redirect or URL-fetching parameters.
- File paths and download endpoints.
- Object IDs and tenant/user identifiers.
- Upload, export, import, webhook, and integration features.

## 9. Handoff

Move to `02-mapping-and-triage/` before testing. Recon output is not a finding; it is raw material for hypotheses.
