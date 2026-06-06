---
title: "Review Methodology"
summary: "How to approach source-assisted security review."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - code-review
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/CODE Review 11516e1de3fd4f439b091aea6b9d5df6.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Source Code Analysis b0d2eddfc2e24f5c80df31ba34e25471.md"
references:
  - "https://securecode.wiki/docs/lang/introduction/"
  - "https://joern.io/"
  - "https://blog.riotsecurityteam.com/0day-chains"
---
# Review Methodology

## Goal

Find exploit-relevant flows by tracing untrusted input to sensitive sinks and checking the controls in between.

## Procedure

1. Map routes and controllers.
2. Identify sources: HTTP input, files, cookies, headers, queues, webhooks.
3. Identify sinks: database, command execution, file paths, templates, URL fetches, deserialization.
4. Check authorization before object access and state change.
5. Validate candidate bugs dynamically when possible.

## Tools

- Secure Code Wiki for language guidance.
- Joern for code property graph exploration.
- Manual source-to-sink tracing for exploitability.
