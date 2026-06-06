---
title: "Legal and Scope Discipline"
summary: "Scope, safety, and authorization rules for using the manual."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - scope
  - safety
  - bug-bounty
related:
  - ../04-workflows/bug-bounty-workflow.md
references: []
---
# Legal and Scope Discipline

## Non-Negotiable Rules

- Test only assets where you have authorization.
- Read program rules before running tools.
- Treat wildcard scope as permission to investigate, not permission to overload infrastructure.
- Never commit API tokens, bounty platform tokens, cookies, session IDs, or customer data.
- Do not use leaked credentials or credential-stuffing workflows.
- Avoid destructive tests unless explicitly allowed.

## Before Running Commands

Confirm:

- target is in scope,
- rate limits are understood,
- command input is deduplicated,
- output path will not leak secrets,
- scan intensity matches authorization.

## Safe Defaults

- Start with passive sources.
- Probe live services gently.
- Use low concurrency first.
- Validate one asset manually before scaling.
- Stop when you can prove impact clearly.
