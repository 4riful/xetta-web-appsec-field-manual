---
title: "Virtual Host Discovery"
summary: "Finding hidden vhosts behind known IPs or shared web servers."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - vhost
  - ffuf
related:
  - subdomain-enumeration.md
  - http-service-discovery.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/V-Host Enumeration 2e17a3e4461d491ea3a067d9926208bc.md"
references: []
---
# Virtual Host Discovery

## When To Use

Use vhost enumeration when multiple hostnames may be served by the same IP or when DNS does not reveal all application names.

## Baseline First

Measure the default response before fuzzing.

```bash
curl -s -H "Host: nonexistent.example.com" http://example.com | wc -c
```

Use the size as a filter when false positives return the same default page.

## FFUF

```bash
ffuf -c -u http://example.com -H "Host: FUZZ.example.com" -w /path/to/wordlist -fs <baseline_size>
```

## Gobuster

```bash
gobuster vhost -u http://example.com/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 50
```

## Nmap

```bash
nmap --script http-vhosts -p 80,8080,443 example.com
```

## TLS SAN Discovery

```bash
echo | openssl s_client -connect example.com:443 2>/dev/null \
  | openssl x509 -noout -text \
  | grep -i DNS
```

## Pitfalls

- CDN edges can produce noisy default responses.
- Wildcard vhosts can make every candidate look valid.
- Lab examples from old notes must be replaced with authorized targets.
