---
title: "Bug Bounty Workflow"
summary: "A safe recon-to-validation loop for bug bounty hunting."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-bounty
  - workflow
related:
  - ../01-reconnaissance/workflow.md
  - ../07-reporting/report-template.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Workflow Cheatsheet 99bf8927e2b94472933fa8877ac55f80.md"
references: []
---
# Bug Bounty Workflow

## Goal

Move from authorized program scope to validated findings without drowning in recon output.

## Loop

1. Read scope and exclusions.
2. Build target inventory.
3. Run passive recon.
4. Validate live services.
5. Mine URLs and JavaScript.
6. Map roles, objects, and APIs.
7. Pick high-confidence vulnerability guides.
8. Validate manually.
9. Capture evidence.
10. Write report.

## When To Stop Recon

Stop when you have high-quality leads with clear impact potential. More subdomains do not matter if you already found an upload parser, admin API, or cross-tenant object boundary.

## Noise Control

- Keep one target/program per workspace.
- Deduplicate early.
- Use low concurrency first.
- Do not run CVE templates blindly across scope.
- Prefer manual validation for reportable issues.
