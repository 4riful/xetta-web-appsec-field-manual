---
title: "XXE, LFI, and File Read"
summary: "XXE, LFI, and File Read resources sorted from the raw ZIP at link and text-snippet level."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - xxe-lfi-and-file-read
related: []
references: []
---

# XXE, LFI, and File Read

Entries: `13`

### Comprehensive Guide on Local File Inclusion (LFI) - Hacking Articles

- Type: `article`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://www.hackingarticles.in/comprehensive-guide-to-local-file-inclusion/

### exploiting out of band xxe in the wild 16fc6dad9ee2

- Type: `article`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://0xmahmoudjo0.medium.com/exploiting-out-of-band-xxe-in-the-wild-16fc6dad9ee2

### Full Local File Read via Error Based XXE using XLIFF File | pwn.vg

- Type: `article`
- Kind: `url`
- Bug class: `lfi;xxe`
- Tier: `tier_2_useful`
- Value: https://web.archive.org/web/20210618175428/https://pwn.vg/articles/2021-06/local-file-read-via-error-based-xxe

### eJPT-Cheatsheet/eJPT CheatSheet.md at main · Hellfire0x01/eJPT-Cheatsheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://github.com/hellfire0x01/eJPT-Cheatsheet/blob/main/eJPT%20CheatSheet.md

### lprTDCXRYgb

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://link.medium.com/lprTDCXRYgb

### cat urls-his | gf lfi |anew lfi

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: cat urls-his | gf lfi |anew lfi

### httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “roo

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi;xss`
- Tier: `tier_2_useful`
- Value: httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “root:[x*]:0:0:”

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### nuclei -l urls-his -c 200 -tags lfi

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: nuclei -l urls-his -c 200 -tags lfi

### Test for lfi via httpx or nuclei

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: Test for lfi via httpx or nuclei

### vijay922/XXE-FUZZ

- Type: `github_repo`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://github.com/vijay922/XXE-FUZZ

### hussein98d/LFI-files

- Type: `payload_collection`
- Kind: `url`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: https://github.com/hussein98d/LFI-files

### <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file

- Type: `payload`
- Kind: `snippet`
- Bug class: `file_upload;xxe`
- Tier: `tier_5_placeholder_payload`
- Value: <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file:///etc/hostname” > ]><svg width=”128px” height=”128px” xmlns=”http://www.w3.org/2000/svg” xmlns:xlink=”http://www.w3.org/1999/xlink” version=”1.1"><text font-size=”16" x=”0" y=”16">&xxe;</text></svg>
