---
title: "Auth"
summary: "auth resources from the vault."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
  - auth
related: []
references: []
---
# Auth

### HolyBugx/HolyTips

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://github.com/HolyBugx/HolyTips/blob/main/Checklist/Authentication.pdf

### oauth2 threat model

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://binarybrotherhood.io/oauth2_threat_model.html

### view

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://drive.google.com/file/d/11Fizx/Vw4GIZ60s5v3I1S5p8kXZHEXFT/view

### e11/014

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://github.com/e11/014/derson/SAML-SSO

### firing 8 account takeover methods 77e892099050

- Type: `article`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://0xmaruf.medium.com/firing-8-account-takeover-methods-77e892099050

### 10 Most Common Security Issues Found In Login Functionalities - RedHunt Labs

- Type: `article`
- Kind: `url`
- Bug class: `auth;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://redhuntlabs.com/blog/10-most-common-security-issues-found-in-login-functionalities.html

### Bypassing 2FA using OpenID Misconfiguration

- Type: `article`
- Kind: `url`
- Bug class: `auth;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://youst.in/posts/bypassing-2fa-using-openid-misconfiguration/

### login testing

- Type: `article`
- Kind: `url`
- Bug class: `auth;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://blog.vedixera.com/login-testing/

### Password Reset Testing Cheat Sheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth;waf-bypass`
- Tier: `tier_2_useful`
- Value: https://highon.coffee/blog/password-reset-security-testing-cheat-sheet/

### imran-parray/Web-Sec-CheatSheet

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://github.com/imran-parray/Web-Sec-CheatSheet/blob/master/password_reset.md

### GitHub Digging 0xAwali 65e04d033e894aaba7e9dd89d5332fae

- Type: `article`
- Kind: `url`
- Bug class: `auth;recon`
- Tier: `tier_2_useful`
- Value: https://sl4x0.notion.site/GitHub-Digging-0xAwali-65e04d033e894aaba7e9dd89d5332fae

### From Recon via Censys and DNSdumpster, to Getting P1 by Login Using Weak Password - "password"

- Type: `writeup`
- Kind: `url`
- Bug class: `auth;recon`
- Tier: `tier_2_useful`
- Value: https://infosecwriteups.com/from-recon-via-censys-and-dnsdumpster-to-getting-p1-by-login-using-weak-password-password-504e617956ce

### nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,

- Type: `command`
- Kind: `snippet`
- Bug class: `auth;lfi;rce;sqli;ssrf;xxe`
- Tier: `tier_2_useful`
- Value: nuclei -c 500 -l urls.txt -t nuclei-templates/ -severity critical,high -ept ssl,tcp -tags cve,rce,log4j,grafana,tomcat,solar,apache,lfi,ssrf,sql,xxe,symfony,exposure,traversal,panel,default-login,confluence,vmware,vcenter -o url_results.txt

### intitle:”Control panel” “Control Panel Login” ArticleLive inurl:admin -demo

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: intitle:”Control panel” “Control Panel Login” ArticleLive inurl:admin -demo

### filetype:mdb “standard jet” (password | username | user | pass)

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: filetype:mdb “standard jet” (password | username | user | pass)

### ext:asp “powered by DUForum” inurl:(messages|details|login|default|register) -si

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: ext:asp “powered by DUForum” inurl:(messages|details|login|default|register) -site:duware.com

### intitle:mywebftp “Please enter your password”

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: intitle:mywebftp “Please enter your password”

### inurl:changepassword.cgi -cvs

- Type: `dork`
- Kind: `snippet`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: inurl:changepassword.cgi -cvs

### target&customer key=zzzz&customer secret zzzz&redirect uri=xxxx&code=e

- Type: `article`
- Kind: `url`
- Bug class: `auth;cloud;rce`
- Tier: `tier_5_placeholder_payload`
- Value: http://target&customer_key=zzzz&customer_secret-zzzz&redirect_uri=xxxx&code=e

### https://github.com/akabe1/OAUTHScan

- Type: `burp_extension`
- Kind: `url`
- Bug class: `auth`
- Tier: `tier_2_useful`
- Value: https://github.com/akabe1/OAUTHScan
