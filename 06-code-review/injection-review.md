---
title: "Injection Review"
summary: "Code-review checklist for SQLi, XSS, command injection, XXE, and template injection."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - injection
  - code-review
references: []
---
# Injection Review

## Check Sinks

- Raw SQL construction.
- Shell execution.
- Template rendering with user input.
- HTML output contexts.
- XML parser configuration.
- URL fetchers.

## Control Questions

- Is parameterization used?
- Is shell avoided or argument-safe?
- Is output encoded by context?
- Are external entities disabled?
