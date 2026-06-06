---
title: "Provenance"
summary: "Internal source archive, generated coverage records, and audit material for maintainers."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - provenance
related: []
references: []
---
# Provenance

This section is for maintainers, audits, recovery, and source verification. Normal learners should start from `resources/`, `awesome-lists/`, `payloads/`, `tools/`, `bug-classes/`, or `maps/` instead.

The original export is preserved under `raw-archive/notion-export/` after the vault reset. The public vault is generated from sorted resource records, while this folder keeps the traceability layer available when something needs to be checked or rebuilt.

## Files

- [Source Catalog](source-catalog.md)
- [Source Resource Links](source-resource-links.md)
- [Source Coverage Matrix](source-coverage-matrix.md)

## How To Use This Section

- Use `source-catalog.md` to confirm which source Markdown files and image assets exist.
- Use `source-resource-links.md` to trace URL resources back to source files.
- Use `source-coverage-matrix.md` to confirm source files have been represented in the generated vault.
- Use `../data/resource-occurrences.csv` when exact occurrence-level provenance matters.

## Rule

Do not make this folder the learner-facing entry point. It exists so the curated vault can stay clean while still preserving the raw material for audit and regeneration.
