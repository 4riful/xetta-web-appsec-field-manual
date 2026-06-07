---
title: "Documentation Status And Trust Model"
summary: "How to interpret reviewed, generated, triage, and archival content in this repository."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - documentation
  - trust
  - quality
related:
  - ../README.md
  - ../maintainers/content-quality-checklist.md
  - ../provenance/source-catalog.md
  - ../data/resources.csv
references: []
---

# Documentation Status And Trust Model

This repository is being rebuilt from a mix of curated guidance, imported notes, generated indexes, resource databases, and manual rewrites.

Use this page to decide how much confidence to place in a page.

## Status Labels

**`reviewed`**
Curated and checked against the content quality checklist. Suitable for field guidance.

**`needs_triage`**
Useful material exists, but the page is not field-ready. Use it as source material only.

**`generated`**
Produced from extraction or categorization. Useful for search/index value only.

**`archival`**
Preserved for provenance or historical context. Do not treat it as current guidance.

## Reviewed Content Standard

A reviewed page should have:

- clear purpose
- audience or intended use
- when to use it
- when not to use it
- safety/legal framing
- related docs
- references or an explicit empty references list
- no unexplained raw commands
- no placeholder payloads
- no private/lab-only hostnames unless clearly marked
- no duplicate generated blocks
- evidence and remediation guidance where relevant

## High-Confidence Entry Points

Use these first:

- [README](../README.md)
- [Quickstart](../QUICKSTART.md)
- [Playbooks](../playbooks/README.md)
- [Bug Classes](../bug-classes/README.md)
- [Reports](../reports/README.md)
- [Top 25 Web AppSec Links](../awesome-lists/top-25-web-appsec-links.md)
- [Content Quality Checklist](../maintainers/content-quality-checklist.md)

## Triage Material

Treat a page as triage material if it contains:

- placeholder payloads
- raw command lists without purpose/input/output
- generated extraction blocks
- duplicate links
- lab-only hostnames
- private Notion or login-only links
- outdated exploit notes with no defensive context
- payload lists with no sink/context guidance

## How To Use Triage Material Safely

1. Use it to find possible source links.
2. Verify the canonical source.
3. Check freshness and relevance.
4. Prefer official docs or original research.
5. Convert useful material into a reviewed page shape.
6. Do not run commands or payloads blindly.

## Source And Provenance

Raw/imported data is preserved for transparency:

- [data/resources.csv](../data/resources.csv)
- [data/resources.json](../data/resources.json)
- [provenance/source-catalog.md](../provenance/source-catalog.md)

These are useful for search, deduplication, and future curation. They are not automatically recommendations.

## Reader Guidance

If you are doing active work:

1. Start with reviewed workflows.
2. Use resource pages to deepen a specific topic.
3. Use raw data only to locate sources.
4. Follow the Reports page before opening a finding.

## Maintainer Guidance

Before marking a page reviewed, apply:

- [Content Quality Checklist](../maintainers/content-quality-checklist.md)
- [Resource Page Template](../templates/resource-page.md)
- [Tool Note Template](../templates/tool-note.md)
- [Bug-Class Template](../templates/bug-class.md)
- [Workflow Template](../templates/workflow.md)

## Trust Principle

If a security person opened this page during real authorized work, it should help them decide what to do next safely. If it does not, it should not be marked reviewed.
