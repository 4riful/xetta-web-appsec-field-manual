---
title: "Repeater Workflows"
summary: "Manual validation workflows using Burp Repeater."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - burp
  - repeater
related:
  - ../../03-vulnerability-guides/access-control/idor.md
references: []
---
# Repeater Workflows

## Access Control

1. Send User A request to Repeater.
2. Replace object ID with User B object ID.
3. Keep User A session.
4. Compare response and state changes.

## Injection

1. Confirm reflection or sink.
2. Add minimal payload.
3. Observe context and encoding.
4. Escalate only if needed.
