---
title: "Api Graphql"
summary: "api-graphql tools and commands."
status: "needs_triage"
last_reviewed: "2026-06-06"
tags:
  - tools
  - api-graphql
related: []
references: []
---
# Api Graphql

### https://github.com/akabe1/OAUTHScan

- Type: `burp_extension`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://github.com/akabe1/OAUTHScan

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### ext:asp “powered by DUForum” inurl:(messages|details|login|default|register) -si

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: ext:asp “powered by DUForum” inurl:(messages|details|login|default|register) -site:duware.com

### intitle:”Control panel” “Control Panel Login” ArticleLive inurl:admin -demo

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: intitle:”Control panel” “Control Panel Login” ArticleLive inurl:admin -demo

### https://github.com/cyprosecurity/API-SecurityEmpire/

- Type: `github_repo`
- Kind: `url`
- Bug class: `api`
- Tier: `tier_2_useful`
- Value: https://github.com/cyprosecurity/API-SecurityEmpire/

### Traceableai/31-days-of-pentesting

- Type: `github_repo`
- Kind: `url`
- Bug class: `api`
- Tier: `tier_2_useful`
- Value: https://github.com/Traceableai/31-days-of-pentesting
