---
title: "Lfi Path Traversal"
summary: "lfi-path-traversal payload and snippet resources."
status: "needs_triage"
last_reviewed: "2026-06-06"
tags:
  - payloads
  - lfi-path-traversal
related: []
references: []
---
# Lfi Path Traversal

### eJPT-Cheatsheet/eJPT CheatSheet.md at main · Hellfire0x01/eJPT-Cheatsheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://github.com/hellfire0x01/eJPT-Cheatsheet/blob/main/eJPT%20CheatSheet.md

### Comprehensive Guide on Local File Inclusion (LFI) - Hacking Articles

- Type: `article`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://www.hackingarticles.in/comprehensive-guide-to-local-file-inclusion/

### Full Local File Read via Error Based XXE using XLIFF File | pwn.vg

- Type: `article`
- Kind: `url`
- Bug class: `lfi;xxe`
- Tier: `tier_2_useful`
- Value: https://web.archive.org/web/20210618175428/https://pwn.vg/articles/2021-06/local-file-read-via-error-based-xxe

### cat urls-his | gf lfi |anew lfi

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: cat urls-his | gf lfi |anew lfi

### Test for lfi via httpx or nuclei

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: Test for lfi via httpx or nuclei

### httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “roo

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi;xss`
- Tier: `tier_2_useful`
- Value: httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “root:[x*]:0:0:”

### nuclei -l urls-his -c 200 -tags lfi

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: nuclei -l urls-his -c 200 -tags lfi

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### hussein98d/LFI-files

- Type: `payload_collection`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://github.com/hussein98d/LFI-files
