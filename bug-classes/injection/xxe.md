---
title: "Xxe"
summary: "xxe resources from the vault."
status: "needs_triage"
last_reviewed: "2026-06-06"
tags:
  - bug-class
  - xxe
related: []
references: []
---
# Xxe

### lprTDCXRYgb

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://link.medium.com/lprTDCXRYgb

### Full Local File Read via Error Based XXE using XLIFF File | pwn.vg

- Type: `article`
- Kind: `url`
- Bug class: `lfi;xxe`
- Tier: `tier_2_useful`
- Value: https://web.archive.org/web/20210618175428/https://pwn.vg/articles/2021-06/local-file-read-via-error-based-xxe

### exploiting out of band xxe in the wild 16fc6dad9ee2

- Type: `article`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://0xmahmoudjo0.medium.com/exploiting-out-of-band-xxe-in-the-wild-16fc6dad9ee2

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### vijay922/XXE-FUZZ

- Type: `github_repo`
- Kind: `url`
- Bug class: `xxe`
- Tier: `tier_2_useful`
- Value: https://github.com/vijay922/XXE-FUZZ

### <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file

- Type: `payload`
- Kind: `snippet`
- Bug class: `file-upload;xxe`
- Tier: `tier_5_placeholder_payload`
- Value: <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file:///etc/hostname” > ]><svg width=”128px” height=”128px” xmlns=”http://www.w3.org/2000/svg” xmlns:xlink=”http://www.w3.org/1999/xlink” version=”1.1"><text font-size=”16" x=”0" y=”16">&xxe;</text></svg>
