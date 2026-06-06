---
title: "JavaScript Recon"
summary: "Collecting JavaScript files, extracting endpoints, and turning client-side clues into testable leads."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - javascript
  - endpoints
related:
  - url-and-archive-recon.md
  - ../03-vulnerability-guides/api-security/rest-api-testing.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/JS IN BUG BOUNTY acc2704513a84087aed6d17ca5d44a15.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
references:
  - "https://github.com/xnl-h4ck3r/GAP-Burp-Extension"
---
# JavaScript Recon

## Goals

- Discover hidden endpoints.
- Find API base URLs.
- Identify feature flags and internal route names.
- Detect accidental secrets or tokens.
- Build parameter and endpoint wordlists.

## Collect JS Files

```bash
cat urls-archive.txt \
  | gauplus -subs \
  | grep -E '\.js($|\?)' \
  | anew jsfiles.txt
```

## Extract Endpoints

```bash
cat jsfiles.txt \
  | grep -oh '"/[a-zA-Z0-9_/?=&.-]*"' \
  | sed -e 's/^"//' -e 's/"$//' \
  | sort -u \
  > js-endpoints.txt
```

## Burp-Assisted Review

Send selected JS through Burp when you want JS Miner, GAP, or passive extensions to parse it.

```bash
cat jsfiles.txt | parallel -j 10 'curl --proxy http://127.0.0.1:8080 -sk {} > /dev/null'
```

Start with low concurrency. Burp can become the bottleneck, and excessive requests can violate program rules.

## Triage Signals

- `/admin`, `/internal`, `/graphql`, `/api/v2`.
- Object IDs, tenant IDs, user IDs.
- Export/import/upload routes.
- Webhook and callback URLs.
- Environment names like staging, dev, qa, beta.
