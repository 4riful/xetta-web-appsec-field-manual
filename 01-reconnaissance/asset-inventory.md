---
title: "Asset Inventory"
summary: "How to normalize bounty scope and asset discovery output into useful target files."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - scope
  - asset-discovery
related:
  - workflow.md
  - subdomain-enumeration.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
references:
  - "https://github.com/projectdiscovery/public-bugbounty-programs"
  - "https://github.com/arkadiyt/bounty-targets-data"
  - "https://github.com/sw33tLie/bbscope"
---
# Asset Inventory

## Goal

Build clean target files before running recon. The goal is not to collect the biggest list; it is to collect assets you are allowed to test and can reason about.

## Public Scope Sources

```bash
curl -s https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/main/chaos-bugbounty-list.json \
  | jq -r '.[][] | select(.bounty==true) | .domains[]' \
  > targets.txt

curl -s https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt \
  | anew targets.txt

curl -s https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/wildcards.txt \
  | anew target-wildcards.txt
```

## Bounty Platform Scope

`bbscope` can pull program scope from major platforms when you provide valid tokens.

```bash
bbscope h1 -a -u <username> -t <token> -b > bbscope-h1.txt
bbscope bc -t <token> -b > bbscope-bc.txt
bbscope it -t <token> -b > bbscope-it.txt
```

## Safety Notes

- Treat platform tokens as secrets.
- Never commit raw tokenized commands.
- Manually remove out-of-scope assets before scanning.
- Keep per-program folders if you hunt multiple programs.

## Output

Recommended files:

- `targets.txt`
- `target-wildcards.txt`
- `out-of-scope.txt`
- `program-rules.md`
- `notes/acquisitions.md`
