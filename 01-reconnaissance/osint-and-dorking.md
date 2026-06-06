---
title: "OSINT and Dorking"
summary: "Using public search, dorks, and intelligence sources to find testable AppSec leads."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - osint
  - dorking
  - recon
related:
  - asset-inventory.md
  - ../08-reference-library/curated-cheat-sheets.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Dorking techniques b49ac278a7f44070b6e595f3876e7db8.md"
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/OSINT WEB TOOLS 9c714449ecee4488ace9cd1885d52e09.md"
references:
  - "https://dorksearch.com/"
  - "https://dorkking.blindf.com/"
  - "https://taksec.github.io/google-dorks-bug-bounty/"
---
# OSINT and Dorking

## Goals

- Discover exposed files and panels.
- Find legacy apps and forgotten endpoints.
- Identify technology and organization context.
- Build leads without touching the target heavily.

## Useful Dork Categories

### Upload Surfaces

```text
"Index of" "upload_image.php"
inurl:updown.php | intext:"Powered by PHP Uploader Downloader"
"Powered By: Simplicity oF Upload" inurl:download.php | inurl:upload.php
```

### Config And Backup Files

```text
"index of" "Production.json"
intitle:"index of" "nrpe.cfg"
filetype:cnf my.cnf -cvs -example
filetype:mdb "standard jet" (password | username | user | pass)
```

### API And Service Definitions

```text
filetype:wsdl wsdl
allinurl:forcedownload.php?file=
```

## Ethics

OSINT can surface leaks and credentials. Do not use exposed credentials. Report sensitive exposure according to program rules and avoid accessing systems with leaked secrets.
