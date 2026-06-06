---
title: "Learning Maps"
summary: "Methodical paths through the vault for beginners, recon, payloads, tools, and bug classes."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - maps
related: []
references: []
---
# Learning Maps

Use this page when you do not know where to start.

## Beginner Flow

1. Read [resources/recon-and-osint.md](../resources/recon-and-osint.md) to understand how targets are discovered.
2. Read [awesome-lists/best-bug-bounty-writeups.md](../awesome-lists/best-bug-bounty-writeups.md) to see real bugs explained.
3. Pick one topic from [bug-classes/](../bug-classes/README.md), not ten at once.
4. Use [payloads/](../payloads/README.md) only after you understand the bug class.
5. Practice with [labs/](../labs/README.md).
6. Learn to document evidence with [reports/](../reports/README.md).

## Bounty Hunter Flow

Start with recon, then move to high-signal bug classes.

1. [Recon and OSINT](../resources/recon-and-osint.md)
2. [Tools and Automation](../tools/README.md)
3. [XSS and Client-Side](../resources/xss-and-client-side.md)
4. [SSRF](../resources/ssrf.md)
5. [SQL Injection](../resources/sql-injection.md)
6. [File Upload and Parser Abuse](../resources/file-upload-and-parser-abuse.md)
7. [Bug Classes](../bug-classes/README.md)

## Payload Flow

Use payloads as testing aids, not magic strings.

1. Pick the vulnerability family in [bug-classes/](../bug-classes/README.md).
2. Open the matching page in [payloads/](../payloads/README.md).
3. Read at least one writeup from [awesome-lists/](../awesome-lists/README.md).
4. Validate behavior manually before reporting.

## Tool Flow

1. Recon tools: [tools/recon.md](../tools/recon.md)
2. Content discovery: [tools/content-discovery.md](../tools/content-discovery.md)
3. Burp extensions: [tools/burp-extensions.md](../tools/burp-extensions.md)
4. Fuzzing: [tools/fuzzing.md](../tools/fuzzing.md)
5. Automation: [tools/automation.md](../tools/automation.md)
