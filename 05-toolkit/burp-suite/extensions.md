---
title: "Burp Extensions"
summary: "Curated Burp extension and adjacent tool matrix from the source corpus."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - burp
  - extensions
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Burp Extensions 9e2504a523d748f0b96ac8ec259bacb9.md"
references:
  - "https://github.com/xnl-h4ck3r/burp-extensions/blob/main/GAP%20Help.md"
---
# Burp Extensions

## Shortlist

| Tool | Use case | Related guide |
|---|---|---|
| GAP | Endpoint and parameter discovery | `../../01-reconnaissance/javascript-recon.md` |
| OAUTHScan | OAuth testing | `../../03-vulnerability-guides/authentication/oauth-and-sso.md` |
| Agartha | Payload manipulation | injection guides |
| Auto Repeater | Repeated OOB/header tests | XSS, SSRF, Log4j-style checks |
| JS Miner | JavaScript endpoint discovery | JavaScript recon |

## Adjacent Tools From Source Notes

These are useful but not Burp extensions:

| Tool | Use case |
|---|---|
| `gitleaks` | secret scanning |
| `x8` | parameter discovery |
| `jaeles` | automated testing templates |
| `autossrf` | SSRF automation |
| `Blisqy` | blind SQLi |

Keep non-Burp tools in their relevant toolkit or vulnerability guide when expanding.
