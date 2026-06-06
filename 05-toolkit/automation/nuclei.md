---
title: "nuclei"
summary: "Using nuclei for lead generation with scope and severity controls."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - nuclei
  - automation
related:
  - ../../04-workflows/bug-bounty-workflow.md
references:
  - "https://github.com/projectdiscovery/nuclei-templates"
---
# nuclei

## Safe Lead Generation

```bash
nuclei -l urls-archive.txt -c 50 -t fuzzing-templates -s critical,high
```

## CVE/High-Severity Sweep

```bash
nuclei -c 50 -l urls.txt -t nuclei-templates/ -severity critical,high -tags cve,rce,log4j,lfi,ssrf,sql,xxe,exposure,panel,default-login
```

## Rules

- Scanner output is not a finding.
- Validate manually.
- Do not run high-concurrency scans without authorization.
- Avoid destructive templates.
