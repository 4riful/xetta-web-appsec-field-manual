---
title: "File Upload and Parser Abuse"
summary: "File upload and parser abuse resources for testing and learning."
status: "needs_triage"
last_reviewed: "2026-06-06"
tags:
  - resources
  - file-upload-and-parser-abuse
related: []
references: []
---

# File Upload and Parser Abuse

Entries: `19`

### A Tale of Two Formats: Exploiting Insecure XML and ZIP File Parsers to Create a Web Shell

- Type: `article`
- Kind: `url`
- Bug class: `waf-bypass`
- Tier: `tier_2_useful`
- Value: https://spaceraccoon.dev/a-tale-of-two-formats-exploiting-insecure-xml-and-zip-file-parsers-to-create-a/

### File Upload Attack | Exploit Notes

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: https://exploit-notes.hdks.org/exploit/file-upload-attack/

### http://www.securityidiots.com/

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: http://www.securityidiots.com/Web-Pentest/hacking-website-by-shell-uploading.html

### https://swarm.ptsecurity.com/

- Type: `article`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://swarm.ptsecurity.com/fuzzing-for-xss-via-nested-parsers-condition/

### hunting for bugs in file upload feature c3b364fb01ba

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: https://sm4rty.medium.com/hunting-for-bugs-in-file-upload-feature-c3b364fb01ba

### securityidiots.com

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: http://www.securityidiots.com/

### svg”

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: http://www.w3.org/2000/svg”

### swarm.ptsecurity.com

- Type: `article`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://swarm.ptsecurity.com/

### Testing File Upload Mechanism

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: https://redmethod.hashnode.dev/testing-file-upload-mechanism

### xlink”

- Type: `article`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: http://www.w3.org/1999/xlink”

### Breaking Down SSRF on PDF Generation: A Pentesting Guide

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `ssrf`
- Tier: `tier_2_useful`
- Value: https://xcheater.medium.com/breaking-down-ssrf-on-pdf-generation-a-pentesting-guide-66f8a309bf3c

### HolyBugx/HolyTips

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: https://github.com/HolyBugx/HolyTips/blob/main/Checklist/Fille%20Upload.pdf

### cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i

- Type: `command`
- Kind: `snippet`
- Bug class: `access-control;sqli`
- Tier: `tier_2_useful`
- Value: cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i 200, 403, 401, 302 -e. conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,log,xml,js,json’ -x 400,500,429

### cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json | \\. pdf | \\.sql | \\. doc| \\.docx | \\. pptx| \\.txt| \\.zip| \\.tar.gz| \\.tgz| \\.bak| \\.7z| \\.rar”

### inurl:updown.php | intext:”Powered by PHP Uploader Downloader”

- Type: `dork`
- Kind: `snippet`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: inurl:updown.php | intext:”Powered by PHP Uploader Downloader”

### “Powered By: Simplicity oF Upload” inurl:download.php | inurl:upload.php

- Type: `dork`
- Kind: `snippet`
- Bug class: `file-upload`
- Tier: `tier_2_useful`
- Value: “Powered By: Simplicity oF Upload” inurl:download.php | inurl:upload.php

### svg ssrfs and saga of bypasses 777e035a17a7

- Type: `writeup`
- Kind: `url`
- Bug class: `file-upload;ssrf;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://infosecwriteups.com/svg-ssrfs-and-saga-of-bypasses-777e035a17a7

### <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file

- Type: `payload`
- Kind: `snippet`
- Bug class: `file-upload;xxe`
- Tier: `tier_5_placeholder_payload`
- Value: <?xml version=”1.0" standalone=”yes”?><!DOCTYPE test [ <!ENTITY xxe SYSTEM “file:///etc/hostname” > ]><svg width=”128px” height=”128px” xmlns=”http://www.w3.org/2000/svg” xmlns:xlink=”http://www.w3.org/1999/xlink” version=”1.1"><text font-size=”16" x=”0" y=”16">&xxe;</text></svg>

### <svg xmlns:svg=”http://www.w3.org/2000/svg” xmlns=”http://www.w3.org/2000/svg” x

- Type: `payload`
- Kind: `snippet`
- Bug class: `file-upload`
- Tier: `tier_5_placeholder_payload`
- Value: <svg xmlns:svg=”http://www.w3.org/2000/svg” xmlns=”http://www.w3.org/2000/svg” xmlns:xlink=”http://www.w3.org/1999/xlink” width=”200" height=”200">
