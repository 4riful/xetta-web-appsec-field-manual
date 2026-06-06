---
title: "Remediation Language"
summary: "Reusable remediation patterns by vulnerability class."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - remediation
  - reporting
references: []
---
# Remediation Language

## Access Control

Enforce server-side authorization for every object read and state-changing action. Authorization should be based on the authenticated user's role, tenant, and object ownership, not on UI visibility or client-provided fields.

## SSRF

Restrict server-side fetchers to allowlisted destinations, block private/internal IP ranges, disable unnecessary redirects, normalize URL parsing, and isolate fetch infrastructure from sensitive networks.

## XSS

Apply context-aware output encoding, sanitize rich HTML with an allowlist sanitizer, avoid dangerous DOM sinks, and use CSP as a defense-in-depth control.

## SQL Injection

Use parameterized queries or safe ORM bindings, validate query builders, and avoid string concatenation with user-controlled input.

## File Upload

Validate content server-side, store files outside web roots, randomize filenames, strip active content, enforce authorization on file access, and process files in isolated environments.
