---
title: "Access Control"
summary: "access-control resources from the vault."
status: "needs_triage"
last_reviewed: "2026-06-06"
tags:
  - bug-class
  - access-control
related: []
references: []
---
# Access Control

### IDOR Attack vectors exploitation bypasses and chains 0b73eb18e9b640ce8c337af831397a6b

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `access-control;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://notion.so/IDOR-Attack-vectors-exploitation-bypasses-and-chains-0b73eb18e9b640ce8c337af831397a6b

### MX5hzfESYgb

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `access-control;cloud`
- Tier: `tier_2_useful`
- Value: https://link.medium.com/MX5hzfESYgb

### bugbounty/403-bypass at main · aufzayed/bugbounty

- Type: `writeup`
- Kind: `url`
- Bug class: `access-control;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://github.com/aufzayed/bugbounty/tree/main/403-bypass

### guide to dns takeovers

- Type: `article`
- Kind: `url`
- Bug class: `access-control`
- Tier: `tier_2_useful`
- Value: https://blog.projectdiscovery.io/guide-to-dns-takeovers/

### What I learnt from reading 220* IDOR bug reports.

- Type: `article`
- Kind: `url`
- Bug class: `access-control`
- Tier: `tier_2_useful`
- Value: https://medium.com/@Sm9l/what-i-learnt-from-reading-220-idor-bug-reports-6efbea44db7

### A 7500$ Google sites IDOR

- Type: `article`
- Kind: `url`
- Bug class: `access-control`
- Tier: `tier_2_useful`
- Value: https://r0ckinxj3.wordpress.com/2021/10/24/a-7500-google-sites-idor/

### cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i

- Type: `command`
- Kind: `snippet`
- Bug class: `access-control;sqli`
- Tier: `tier_2_useful`
- Value: cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i 200, 403, 401, 302 -e. conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,log,xml,js,json’ -x 400,500,429
