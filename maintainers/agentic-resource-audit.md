---
title: "Agentic Resource Audit"
summary: "Independent multi-agent verification of raw ZIP resources, public indexes, and deep source samples."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - qa
  - agentic-audit
related:
  - ../RESOURCE-MAP.md
  - resource-completeness-check.md
  - source-resource-links.md
  - exhaustive-source-catalog.md
references: []
---
# Agentic Resource Audit

## Result

Coverage is complete, but the earlier public presentation was too noisy.

Three independent agents checked the raw archive, public resource indexes, and deep source samples. No missing public resource coverage was found. The usability issue was navigation: the exhaustive raw list was too prominent and mixed placeholders, payload strings, writeups, tools, and normal resource links together.

## Agents

| Agent | Scope | Result |
|---|---|---|
| Agent A: Raw Source Auditor | Checked every raw Markdown file under `source-archive/notion-export/` against maintainer coverage artifacts and resource indexes. | PASS: 66 raw Markdown files represented; 0 missing normalized HTTP/HTTPS resources. |
| Agent B: Resource Index Auditor | Checked `RESOURCES.md`, `08-reference-library/all-source-resources.md`, all category indexes, and `maintainers/source-resource-links.md` for count/category/link consistency. | PASS for category reachability and internal links. Found exact-string punctuation normalization differences in 8 source-preserved URLs. |
| Agent C: Deep Sample Auditor | Sampled 13 source files across major folders, including the largest and highest-value files. | PASS: 53 sampled URLs found in public resource indexes. |

## Verified Scope

- Raw Markdown files: `66`
- Raw image assets: `3`
- Normalized HTTP/HTTPS URL occurrences checked by independent extraction: `533`
- Unique normalized HTTP/HTTPS URLs checked by independent extraction: `406`
- Missing normalized HTTP/HTTPS URLs: `0`
- Public category index files: `15`
- Category indexes linked from `README.md`: `15`
- Category indexes linked from `RESOURCES.md`: `15`
- Category indexes linked from `08-reference-library/README.md`: `15`

## Deep Samples Checked

Agent C checked URLs from these source files:

- `Tips From EMAD Shanab`
- `ALL IN ONE Cheat Sheets`
- `Bugs/SSRF`
- `Bugs/XSS`
- `Bugs/API`
- `Bugs/IDOR`
- `Subdomain eumeration/V-Host Enumeration`
- `Toolkit and Burpsuite Extensions/Burp Extensions`
- `Toolkit and Burpsuite Extensions`
- `Recon All the things`
- `OSINT WEB TOOLS`
- `YouTube`
- `Subdomain eumeration/TOOLS`

All sampled URLs were present in public resource indexes.

## Exact-String Normalization Notes

Agent B found 8 exact-string differences between source-preserved audit files and public category indexes. These are not missing resources. They are punctuation-boundary differences where the public category index stripped trailing punctuation from malformed source snippets.

Affected source strings include AEM placeholder URLs ending in `.` and one GitHub URL ending in `,`.

The source-preserved audit files keep the original punctuation. Public resource indexes keep the normalized URL because it is more usable for readers.

## Usability Fix

Added [Resource Map](../RESOURCE-MAP.md) as the clean front door.

The new intended order is:

1. `RESOURCE-MAP.md` for clean navigation.
2. `08-reference-library/resource-indexes/*.md` for topic lists.
3. `RESOURCES.md` only for exhaustive category dump.
4. `maintainers/source-resource-links.md` only for exact source audit.

## Conclusion

The resources from the ZIP are available. The messy part was presentation, not missing coverage. The repository now separates clean navigation from exhaustive audit data.
