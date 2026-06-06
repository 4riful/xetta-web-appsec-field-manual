---
title: "Start Here"
summary: "Route selector for using the Xetta Web AppSec Field Manual."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - orientation
  - navigation
related:
  - FIELD-MANUAL.md
references: []
---
# Start Here

## Pick Your Path

| Situation | Path |
|---|---|
| I have a bounty target and need a plan | `04-workflows/bug-bounty-workflow.md` |
| I need to collect assets | `01-reconnaissance/workflow.md` |
| I have subdomains but no priorities | `02-mapping-and-triage/attack-surface-scoring.md` |
| I found interesting endpoints | `02-mapping-and-triage/finding-testable-leads.md` |
| I want to test a bug class | `03-vulnerability-guides/README.md` |
| I need payloads/tools | `05-toolkit/README.md` |
| I need to write a report | `07-reporting/report-template.md` |

## Beginner Route

1. Read `00-orientation/legal-and-scope-discipline.md`.
2. Follow `01-reconnaissance/workflow.md`.
3. Build `targets.txt`, `subs-resolved.txt`, `hosts-http.txt`, and `urls-archive.txt`.
4. Read `02-mapping-and-triage/finding-testable-leads.md`.
5. Pick one vulnerability guide and test only where the signal makes sense.
6. Capture evidence using `07-reporting/evidence-standards.md`.

## Operator Route

1. Scope intake.
2. Passive recon.
3. Active enrichment.
4. Live service discovery.
5. URL/archive mining.
6. JavaScript endpoint extraction.
7. Mapping and triage.
8. Bug-class testing.
9. Report writing.

## Rule Of The Repo

Do not spray payloads at random. Build a model, identify a trust boundary, then test with a reason.
