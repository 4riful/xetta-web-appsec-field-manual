---
title: "Start Here"
summary: "Route selector for using the Xetta Web AppSec Field Manual."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - orientation
  - navigation
related:
  - RESOURCE-MAP.md
  - RESOURCES.md
  - RESOURCE-FIRST.md
  - FIELD-MANUAL.md
references: []
---
# Start Here

## Pick Your Path

| Situation | Path |
|---|---|
| I want clean resources first | `RESOURCE-MAP.md` |
| I want the exhaustive raw resource dump | `RESOURCES.md` |
| I want to understand the resource-first layout | `RESOURCE-FIRST.md` |
| I have a bounty target and need a plan | `04-workflows/bug-bounty-workflow.md` |
| I need to collect assets | `01-reconnaissance/workflow.md` |
| I have subdomains but no priorities | `02-mapping-and-triage/attack-surface-scoring.md` |
| I found interesting endpoints | `02-mapping-and-triage/finding-testable-leads.md` |
| I want to test a bug class | `03-vulnerability-guides/README.md` |
| I need payloads/tools | `05-toolkit/README.md` |
| I need to write a report | `07-reporting/report-template.md` |

## Beginner Route

1. Open `RESOURCE-MAP.md` and choose a category.
2. Use `RESOURCES.md` only when you need the exhaustive raw resource dump.
3. Use `RESOURCE-FIRST.md` to understand how the resource library is organized.
4. Read `00-orientation/legal-and-scope-discipline.md` before active testing.
5. Follow `01-reconnaissance/workflow.md` when you move from reading to testing.
6. Build `targets.txt`, `subs-resolved.txt`, `hosts-http.txt`, and `urls-archive.txt`.
7. Read `02-mapping-and-triage/finding-testable-leads.md`.
8. Pick one vulnerability guide and test only where the signal makes sense.
9. Capture evidence using `07-reporting/evidence-standards.md`.

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
