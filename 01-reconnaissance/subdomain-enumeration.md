---
title: "Subdomain Enumeration"
summary: "Passive and active subdomain enumeration workflow with filtering and handoff guidance."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - subdomains
related:
  - asset-inventory.md
  - http-service-discovery.md
  - virtual-host-discovery.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration 084630216b8f46e891dd2a7896eb31e6.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/TOOLS a902f3b512814f0eaf26e640226ef831.md"
references:
  - "https://github.com/blacklanternsecurity/bbot"
  - "https://pentester.land/blog/subdomains-enumeration-cheatsheet/"
  - "https://0xffsec.com/handbook/information-gathering/subdomain-enumeration/"
  - "https://blog.blacklanternsecurity.com/p/subdomain-enumeration-tool-face-off"
---
# Subdomain Enumeration

## Mental Model

Subdomain enumeration is the process of expanding authorized root or wildcard domains into concrete hostnames worth resolving and probing.

## Workflow

1. Start with clean scope from `asset-inventory.md`.
2. Collect passive subdomains from certificate transparency, public datasets, search engines, and tools like `bbot`.
3. Run active brute force only where the program allows it.
4. Resolve candidates.
5. Filter wildcard DNS.
6. Deduplicate.
7. Send resolved hosts to HTTP service discovery.

## Output Files

- `subs-passive.txt`
- `subs-active.txt`
- `subs-resolved.txt`
- `subs-wildcard-filtered.txt`

## Quality Checks

- Remove hosts outside authorized domains.
- Check wildcard responses before trusting brute-force results.
- Keep source labels if possible so high-confidence hosts are easier to prioritize.

## Handoff

Use `http-service-discovery.md` to determine which resolved hosts expose web services.
