---
title: "Sample Finding: SSRF"
summary: "Sample structure for an SSRF report."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - ssrf
  - sample-finding
related:
  - ../../03-vulnerability-guides/server-side/ssrf.md
references: []
---
# Sample Finding: SSRF

## Summary

The application fetches attacker-controlled URLs from the server side.

## Impact

Depending on network reachability, this can expose internal services or cloud metadata.

## Evidence To Include

- Vulnerable request with URL parameter.
- OOB callback log.
- Source IP and timestamp.
- Safe impact proof.
