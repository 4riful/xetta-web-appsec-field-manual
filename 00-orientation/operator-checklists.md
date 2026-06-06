---
title: "Operator Checklists"
summary: "Short preflight and evidence checklists for AppSec testing."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - checklist
  - workflow
related:
  - ../07-reporting/evidence-standards.md
references: []
---
# Operator Checklists

## Scope Preflight

- [ ] Program or engagement authorization confirmed.
- [ ] In-scope domains and exclusions saved.
- [ ] Test accounts created or provided.
- [ ] Rate limits and automation rules reviewed.
- [ ] Secrets and tokens stored outside Git.

## Recon Output Files

- [ ] `targets.txt`
- [ ] `target-wildcards.txt`
- [ ] `subs-passive.txt`
- [ ] `subs-resolved.txt`
- [ ] `hosts-http.txt`
- [ ] `urls-archive.txt`
- [ ] `jsfiles.txt`
- [ ] `js-endpoints.txt`
- [ ] `content-hits.txt`

## Finding Evidence

- [ ] Vulnerable request and response captured.
- [ ] Account/role context documented.
- [ ] Impact demonstrated safely.
- [ ] False positives considered.
- [ ] Remediation is specific.
