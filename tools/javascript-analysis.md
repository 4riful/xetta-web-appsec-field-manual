---
title: "Javascript Analysis"
summary: "javascript-analysis tools and commands."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - tools
  - javascript-analysis
related: []
references: []
---
# Javascript Analysis

### https://github.com/bit4woo/domain_hunter

- Type: `burp_extension`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://github.com/bit4woo/domain_hunter

### https://github.com/ferreiraklet/airixss---

- Type: `burp_extension`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://github.com/ferreiraklet/airixss---

### [ffuf scripts and tricks [NahamCon 2021]](https://www.youtube.com/watch?v=uwcRBS

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: [ffuf scripts and tricks [NahamCon 2021]](https://www.youtube.com/watch?v=uwcRBSUl8e4)

### cat urls | gauplus -subs | grep “.js” |. httpx -content-type | grep ‘application

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: cat urls | gauplus -subs | grep “.js” |. httpx -content-type | grep ‘application/javascript’” | awk ‘{print $1}’ | nuclei. -t nuclei-templates/http/exposures/ -silent. > secrets.txt

### cat urls-his | gf xss | anew xss

- Type: `command`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: cat urls-his | gf xss | anew xss

### curl -s -H "Host: nonexistent.ffuf.io.fi" http://ffuf.io.fi | wc -c

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: curl -s -H "Host: nonexistent.ffuf.io.fi" http://ffuf.io.fi | wc -c

### echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -i dns

### ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs 612

### git clone https://github.com/s0md3v/XSStrike.git /opt/xsstrike || git -C /opt/xs

- Type: `command`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: git clone https://github.com/s0md3v/XSStrike.git /opt/xsstrike || git -C /opt/xsstrike pull

### httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “roo

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi;xss`
- Tier: `tier_2_useful`
- Value: httpx -l lfi -paths /root/LFI-files -threads 100 -random-agent. -mc 200 -mr “root:[x*]:0:0:”

### nmap --script http-vhosts -p 80,8080,443 target

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: nmap --script http-vhosts -p 80,8080,443 target

### sqlmap -m sql -batch — random-agent — level 5 — risk 3

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli;xss`
- Tier: `tier_2_useful`
- Value: sqlmap -m sql -batch — random-agent — level 5 — risk 3

### https://github.com/ShadowByte1/XSS

- Type: `github_repo`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://github.com/ShadowByte1/XSS

### random-robbie/ssrf-finder

- Type: `github_repo`
- Kind: `url`
- Bug class: `ssrf;xss`
- Tier: `tier_2_useful`
- Value: https://github.com/random-robbie/ssrf-finder

### Referer: xsshunter

- Type: `note`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: Referer: xsshunter

### Replace : Referer: xsshunter

- Type: `note`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: Replace : Referer: xsshunter

### Replace: User-Agent:xsshunter

- Type: `note`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: Replace: User-Agent:xsshunter

### User-Agent:xsshunter

- Type: `note`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: User-Agent:xsshunter

### emadshanab/Blind-XSS-burp-match-and-replace

- Type: `tool`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://github.com/emadshanab/Blind-XSS-burp-match-and-replace

### ffuf.io.fi

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: http://ffuf.io.fi

### https://github.com/blacklanternsecurity/bbot

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: https://github.com/blacklanternsecurity/bbot

### s0md3v/XSStrike.git

- Type: `tool`
- Kind: `url`
- Bug class: `xss`
- Tier: `tier_2_useful`
- Value: https://github.com/s0md3v/XSStrike.git

### Subdomain Enumeration Tool Face-off 2022

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: https://blog.blacklanternsecurity.com/p/subdomain-enumeration-tool-face-off

### vhost

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: http://ffuf.me/sub/vhost

### YouTube video or playlist

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: https://www.youtube.com/watch?v=uwcRBSUl8e4

### - `curl -s <https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-

- Type: `command`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_5_placeholder_payload`
- Value: - `curl -s <https://raw.githubusercontent.com/projectdiscovery/public-bugbounty-programs/main/chaos-bugbounty-list.json> | jq “.[][] | select(.bounty==true) | .domains[]” -r > targets.txt`

### - `curl -s “<https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main

- Type: `command`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_5_placeholder_payload`
- Value: - `curl -s “<https://raw.githubusercontent.com/arkadiyt/bounty-targets-data/main/data/domains.txt”> | anew targets.txt`

### 1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: 1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

### 2. ffuf -c -u http://bolt.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-t

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: 2. ffuf -c -u http://bolt.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.bolt.htb" -fl 505

### 3. gobuster vhost -u http://horizontall.htb/ -w /usr/share/seclists/Discovery/DN

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: 3. gobuster vhost -u http://horizontall.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 200

### Replace COLLABHERE with your OOB domain — sed ‘s/COLLABHERE/<oob-domain>/g

- Type: `payload`
- Kind: `snippet`
- Bug class: `xss`
- Tier: `tier_5_placeholder_payload`
- Value: Replace COLLABHERE with your OOB domain — sed ‘s/COLLABHERE/<oob-domain>/g

### bolt.htb

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: http://bolt.htb/

### target

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: https://target

### https://github.com/xerohackcom/webrecon

- Type: `burp_extension`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/xerohackcom/webrecon

### /opt/waymore/config.yml

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: /opt/waymore/config.yml

### [](https://blog.vedixera.com/master-in-ffuf/)

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: [](https://blog.vedixera.com/master-in-ffuf/)

### [FFUF - Everything You Need To Know - CyberSec Nerds](https://cybersecnerds.com/

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: [FFUF - Everything You Need To Know - CyberSec Nerds](https://cybersecnerds.com/ffuf-everything-you-need-to-know/)

### [ffuf advanced tricks - ACCEIS](https://www.acceis.fr/ffuf-advanced-tricks/)

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: [ffuf advanced tricks - ACCEIS](https://www.acceis.fr/ffuf-advanced-tricks/)

### cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i

- Type: `command`
- Kind: `snippet`
- Bug class: `access-control;sqli`
- Tier: `tier_2_useful`
- Value: cat hosts | xargs -I@ sh -c ‘python3 dirsearch.py -r 3 -t 500 -b -w path -u @ -i 200, 403, 401, 302 -e. conf,config,bak,backup,swp,old,db,sql,asp,aspx,aspx~,asp~,py,py~,rb,rb~,php,php~,bak,bkp,cache,cgi,conf,csv,html,inc,jar,js,json,jsp,jsp~,lock,log,rar,old,sql,sql.gz,sql.zip,sql.tar.gz,sql~,swp,swp~,tar,tar.bz2,tar.gz,txt,wadl,zip,log,xml,js,json’ -x 400,500,429

### cat url.txt | while read host do;do. waymore -i $host |anew /root/urls-his.txt ;

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: cat url.txt | while read host do;do. waymore -i $host |anew /root/urls-his.txt ;done

### cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json

- Type: `command`
- Kind: `snippet`
- Bug class: `sqli`
- Tier: `tier_2_useful`
- Value: cat urls | gauplus -subs | grep — -color -E. “.xls | \\. xml | \\.xlsx | \\.json | \\. pdf | \\.sql | \\. doc| \\.docx | \\. pptx| \\.txt| \\.zip| \\.tar.gz| \\.tgz| \\.bak| \\.7z| \\.rar”

### cat urls | gauplus -subs | grep “.js” | anew jsfiles.txt| cat jsfiles.txt | grep

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: cat urls | gauplus -subs | grep “.js” | anew jsfiles.txt| cat jsfiles.txt | grep -oh “\”\/[a-zA-Z0–9_/?=&]*\”” | sed -e ‘s/^”//’ -e ‘s/”$//’ | sort -u

### chmod +x /usr/local/bin/waymore

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: chmod +x /usr/local/bin/waymore

### git clone https://github.com/xnl-h4ck3r/waymore.git /opt/waymore || git -C /opt/

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: git clone https://github.com/xnl-h4ck3r/waymore.git /opt/waymore || git -C /opt/waymore pull

### If you have found somthing you can use dirsearch to fuzz for some juicy files yo

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: If you have found somthing you can use dirsearch to fuzz for some juicy files you can run it against multiple hosts

### Install waymore to get the history of your target

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: Install waymore to get the history of your target

### ln -s /opt/waymore//waymore.py /usr/local/bin/waymore

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: ln -s /opt/waymore//waymore.py /usr/local/bin/waymore

### pip3 install -r /opt/waymore/requirements.txt

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: pip3 install -r /opt/waymore/requirements.txt

### Run gospider and proxit it to burpsuite to collect more urls:-

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: Run gospider and proxit it to burpsuite to collect more urls:-

### Test for lfi via httpx or nuclei

- Type: `command`
- Kind: `snippet`
- Bug class: `lfi`
- Tier: `tier_2_useful`
- Value: Test for lfi via httpx or nuclei

### waymore -i http://google.com |anew /root/google-his.txt

- Type: `command`
- Kind: `snippet`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: waymore -i http://google.com |anew /root/google-his.txt

### assetnote/surf

- Type: `github_repo`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://github.com/assetnote/surf/

### GitHub - Th3l0newolf/AdvanceRecon-Dorks

- Type: `github_repo`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/Th3l0newolf/AdvanceRecon-Dorks

### https://github.com/edoardottt/awesome-hacker-search-engines

- Type: `github_repo`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/edoardottt/awesome-hacker-search-engines

### https://github.com/System00-Security/Recon-Reloaded

- Type: `github_repo`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/System00-Security/Recon-Reloaded

### https://github.com/TheBinitGhimire/GitHub-Recon

- Type: `github_repo`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/TheBinitGhimire/GitHub-Recon

### redhuntlabs/Awesome-Asset-Discovery

- Type: `github_repo`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://github.com/redhuntlabs/Awesome-Asset-Discovery

### xnl-h4ck3r/waymore.git

- Type: `github_repo`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://github.com/xnl-h4ck3r/waymore.git

### censys.io

- Type: `osint_service`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://censys.io

### dehashed.com

- Type: `osint_service`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://dehashed.com

### dnsdumpster.com

- Type: `osint_service`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://dnsdumpster.com

### haveibeenpwned.com

- Type: `osint_service`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://haveibeenpwned.com

### https://web-check.xyz/

- Type: `osint_service`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://web-check.xyz/

### intelx.io

- Type: `osint_service`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://intelx.io

### profile

- Type: `osint_service`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://urlscan.io/user/profile/

### shodan.io

- Type: `osint_service`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://shodan.io

### snusbase.com

- Type: `osint_service`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://snusbase.com

### 4iq.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://4iq.com

### breachchecker.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://breachchecker.com

### cve 2022 41040 unfurl payloads.txt|sed

- Type: `tool`
- Kind: `url`
- Bug class: `rce;recon`
- Tier: `tier_2_useful`
- Value: https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed

### FFUF - Everything You Need To Know - CyberSec Nerds

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://cybersecnerds.com/ffuf-everything-you-need-to-know/

### ffuf advanced tricks - ACCEIS

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://www.acceis.fr/ffuf-advanced-tricks/

### ghostproject.fr

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://ghostproject.fr

### hashes.org

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://hashes.org

### haveibeensold.app

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://haveibeensold.app

### https://redsiege.com/tools-techniques/2020/02/recon-methods-part-2-osint-host-discovery-continued/

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://redsiege.com/tools-techniques/2020/02/recon-methods-part-2-osint-host-discovery-continued/

### leak lookup.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leak-lookup.com

### leak.sx

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leak.sx

### leakcheck.io

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leakcheck.io

### leakcheck.net

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leakcheck.net

### leakcorp.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leakcorp.com

### leaked.site

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leaked.site

### leakedsource.ru

- Type: `tool`
- Kind: `url`
- Bug class: `rce;recon`
- Tier: `tier_2_useful`
- Value: https://leakedsource.ru

### leakengine

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://joe.black/leakengine.html

### leakpeek.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://leakpeek.com

### master in ffuf

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://blog.vedixera.com/master-in-ffuf/

### nuclearleaks.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://nuclearleaks.com

### private base.info

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://private-base.info

### rslookup.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://rslookup.com

### scatteredsecrets.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: http://scatteredsecrets.com

### scylla.sh

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: http://scylla.sh

### services.normshield.com

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://services.normshield.com

### vigilante.pw

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://vigilante.pw

### weleakinfo.to

- Type: `tool`
- Kind: `url`
- Bug class: `recon`
- Tier: `tier_2_useful`
- Value: https://weleakinfo.to

### gospider -S urls-his -a -w — sitemap -r -c 20 -d 8 -p http://127.0.0.1:8080

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_5_placeholder_payload`
- Value: gospider -S urls-his -a -w — sitemap -r -c 20 -d 8 -p http://127.0.0.1:8080

### for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8

- Type: `payload`
- Kind: `snippet`
- Bug class: `rce;recon`
- Tier: `tier_5_placeholder_payload`
- Value: for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed ‘s/COLLABHERE/<OOB-PAYLOAD>/g’); do cat targets.txt |unfurl format $url >> fuzz-ready.txt;done & ffuf -w fuzz-ready.txt -u FUZZ
