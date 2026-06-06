---
title: "URL and Archive Recon"
summary: "Mining historical URLs and classifying parameters into vulnerability leads."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - archives
  - waymore
  - gf
related:
  - javascript-recon.md
  - ../02-mapping-and-triage/finding-testable-leads.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
references:
  - "https://github.com/xnl-h4ck3r/waymore"
  - "https://github.com/tomnomnom/gf"
  - "https://github.com/emadshanab/Gf-Patterns-Collection"
---
# URL and Archive Recon

## Why Archives Matter

Historical URLs reveal old endpoints, parameters, admin paths, file handlers, and APIs that may still exist or leave useful clues.

## Waymore Setup

```bash
git clone https://github.com/xnl-h4ck3r/waymore.git ~/tools/waymore || git -C ~/tools/waymore pull
pip3 install -r ~/tools/waymore/requirements.txt
```

## Collect URLs

```bash
while read -r host; do
  waymore -i "$host" | anew urls-archive.txt
done < hosts-http.txt
```

## Classify Leads With GF

```bash
gf sql urls-archive.txt | anew leads-sqli.txt
gf xss urls-archive.txt | anew leads-xss.txt
gf ssrf urls-archive.txt | anew leads-ssrf.txt
gf lfi urls-archive.txt | anew leads-lfi.txt
```

## What Output Matters

- URLs with parameters.
- API paths.
- File download/export routes.
- Redirect and callback parameters.
- Legacy extensions like `.php`, `.asp`, `.aspx`, `.jsp`.

## False Positives

Archive URLs can be dead. Validate with HTTP probing before testing aggressively.
