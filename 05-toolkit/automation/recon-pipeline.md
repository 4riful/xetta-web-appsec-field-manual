---
title: "Recon Pipeline"
summary: "Consistent file flow for recon automation."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - automation
references:
  - "https://labs.detectify.com/2021/11/30/hakluke-creating-the-perfect-bug-bounty-automation/"
---
# Recon Pipeline

## File Flow

```text
targets.txt
target-wildcards.txt
subs-passive.txt
subs-active.txt
subs-resolved.txt
hosts-http.txt
urls-archive.txt
urls-interesting.txt
jsfiles.txt
js-endpoints.txt
content-hits.txt
nuclei-findings.txt
manual-validation.md
```

## Principle

Every stage should have a clear input and output. If you cannot explain what a command consumes and produces, do not add it to the pipeline.
