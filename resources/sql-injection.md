---
title: "SQL Injection"
summary: "SQL Injection resources sorted from the raw ZIP at link and text-snippet level."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - sql-injection
related: []
references: []
---

# SQL Injection

Entries: `17`

### cheat sheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_1_core`
- Value: https://portswigger.net/web-security/sql-injection/cheat-sheet

### error based sql injection with waf bypass manual exploit 100 bab36b769005

- Type: `article`
- Kind: `url`
- Bug class: `sqli;waf_bypass`
- Tier: `tier_2_useful`
- Value: https://c0nqr0r.medium.com/error-based-sql-injection-with-waf-bypass-manual-exploit-100-bab36b769005

### MSSQL Injection In JSON Request

- Type: `article`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://kailashbohara.com.np/blog/2021/05/16/MSSQL-Injection-in-JSON-request/

### sql injection comprehensive guide

- Type: `article`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://www.akto.io/blog/sql-injection-comprehensive-guide

### GitHub - kleiton0x00/Advanced-SQL-Injection-Cheatsheet: A cheat sheet that contains advanced queries for SQL Injection of all types.

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://github.com/kleiton0x00/Advanced-SQL-Injection-Cheatsheet/tree/main

### sql injection cheat sheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://www.invicti.com/blog/web-security/sql-injection-cheat-sheet/

### cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i

- Type: `command`
- Kind: `snippet`
- Bug class: `access_control;sqli`
- Tier: `tier_2_useful`
- Value: cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i 200, 403, 401, 302 -e. conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,log,xml,js,json’ -x 400,500,429

### cat sql | while read host do;do ghauri -u $host — batch — level=3. -b — current-

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: cat sql | while read host do;do ghauri -u $host — batch — level=3. -b — current-user — current-db — hostname — dbs ;done

### cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json | \\. pdf | \\.sql | \\. doc| \\.docx | \\. pptx| \\.txt| \\.zip| \\.tar.gz| \\.tgz| \\.bak| \\.7z| \\.rar”

### cat urls-his | gf sql | anew sql

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: cat urls-his | gf sql | anew sql

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### Run ghauri to test for sql injection:-

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: Run ghauri to test for sql injection:-

### Run sqlmap to test for sql injection:-

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: Run sqlmap to test for sql injection:-

### sqlmap -m sql -batch — random-agent — level 5 — risk 3

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli;xss`
- Tier: `tier_2_useful`
- Value: sqlmap -m sql -batch — random-agent — level 5 — risk 3

### SQL Injection Payload List

- Type: `payload_collection`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://ismailtasdelen.medium.com/sql-injection-payload-list-b97656cfd66b

### Y000o/Payloads_xss_sql_bypass

- Type: `payload_collection`
- Kind: `url`
- Bug class: `sqli;waf_bypass;xss`
- Tier: `tier_2_useful`
- Value: https://github.com/Y000o/Payloads_xss_sql_bypass/blob/master/Payloads_xss_sql_bypass.md#Sql-inyection-case-y-sounds-like

### r0oth3x49/ghauri

- Type: `tool`
- Kind: `url`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: https://github.com/r0oth3x49/ghauri
