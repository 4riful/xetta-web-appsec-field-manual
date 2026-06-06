---
title: "Cloud"
summary: "cloud tools and commands."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - tools
  - cloud
related: []
references: []
---
# Cloud

### echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -i dns

### GitHub - 4ndersonLin/awesome-cloud-security: 🛡️ Awesome Cloud Security Resources ⚔️

- Type: `github_repo`
- Kind: `url`
- Bug class: `cloud;rce`
- Tier: `tier_2_useful`
- Value: https://github.com/4ndersonLin/awesome-cloud-security#aws-1

### mxm0z/awesome-sec-s3

- Type: `github_repo`
- Kind: `url`
- Bug class: `cloud`
- Tier: `tier_2_useful`
- Value: https://github.com/mxm0z/awesome-sec-s3

### dnsdumpster.com

- Type: `osint_service`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://dnsdumpster.com

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

### bolt.htb

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: http://bolt.htb/
