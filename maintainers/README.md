---
title: "Maintainers"
summary: "Maintainer-only rules for the resource vault, database generation, and quality checks."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - maintainers
related:
  - ../data/README.md
  - ../provenance/README.md
references: []
---
# Maintainers

## Purpose

This folder keeps maintenance rules out of the main resource browsing path.

## Contents

- [Content Quality Checklist](content-quality-checklist.md)
- [Link Checking](link-checking.md)

## Source Of Truth

- Resource database: [data/resources.csv](../data/resources.csv)
- Resource occurrences: [data/resource_occurrences.csv](../data/resource_occurrences.csv)
- Source documents: [data/source_documents.csv](../data/source_documents.csv)
- Provenance: [provenance/](../provenance/README.md)
- Raw archive: `../provenance/raw-archive/notion-export/`

## Rule

User-facing material belongs in `resources/`, `awesome-lists/`, `payloads/`, `tools/`, `bug-classes/`, `playbooks/`, `maps/`, `labs/`, and `reports/`. Source audit and raw export material belongs in `provenance/`.
