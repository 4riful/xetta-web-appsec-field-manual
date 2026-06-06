---
title: "Sample Finding: IDOR"
summary: "Sample structure for an IDOR report."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - idor
  - sample-finding
related:
  - ../../03-vulnerability-guides/access-control/idor.md
references: []
---
# Sample Finding: IDOR

## Summary

The API allows a user to access another user's object by changing the object ID in the request.

## Impact

An attacker with a normal account can read or modify another user's data.

## Evidence To Include

- User A object creation.
- User B unauthorized request.
- Response showing unauthorized access.
- Object ownership proof.
