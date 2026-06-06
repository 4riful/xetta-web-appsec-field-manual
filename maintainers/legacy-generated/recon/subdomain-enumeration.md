---
title: "Subdomain Enumeration"
summary: "Canonical subdomain enumeration note migrated from 3 Notion source page(s), preserving commands, links, and resource references."
tags:
  - recon
  - subdomains
  - vhosts
  - dns
related_topics:
  - "Bug Bounty Workflow"
  - "OSINT and Dorking"
  - "Subdomain Enumeration"
references:
  - "https://github.com/blacklanternsecurity/bbot"
  - "https://docs.google.com/presentation/d/1k8A_sjJpMUsVdLY5cmtHxkbikn-WvOzD/edit#slide=id.p1"
  - "https://www.youtube.com/watch?v=uwcRBSUl8e4"
  - "https://target"
  - "http://bolt.htb/"
  - "http://horizontall.htb/"
  - "http://ffuf.me/sub/vhost"
  - "http://ffuf.io.fi"
  - "https://pentester.land/blog/subdomains-enumeration-cheatsheet/"
  - "https://m0chan.github.io/2019/12/17/Bug-Bounty-Cheetsheet.html"
  - "https://0xffsec.com/handbook/information-gathering/subdomain-enumeration/#fn:8"
  - "https://apexvicky.medium.com/subdomain-enumeration-the-right-way-prerequisites-7449ac0f2498"
  - "https://trickest.medium.com/recon-experience-with-trickest-subdomain-recon-tale-in-a-workflow-1-a522717d1471"
  - "https://trickest.medium.com/recon-experience-with-trickest-subdomain-recon-tale-in-a-workflow-2-brute-forcing-and-158b9be9e924"
  - "https://blog.blacklanternsecurity.com/p/subdomain-enumeration-tool-face-off"
---

# Subdomain Enumeration

## Summary

Canonical subdomain enumeration note migrated from 3 Notion source page(s), preserving commands, links, and resource references.

## Source Provenance

- `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/TOOLS a902f3b512814f0eaf26e640226ef831.md` (12 words, 1 external links)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/V-Host Enumeration 2e17a3e4461d491ea3a067d9926208bc.md` (188 words, 8 external links)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration 084630216b8f46e891dd2a7896eb31e6.md` (163 words, 7 external links)

## Refactored Notes

### Subdomain Enumeration Tools

> Tools

[https://github.com/blacklanternsecurity/bbot](https://github.com/blacklanternsecurity/bbot)

### Virtual Host Enumeration

> Thapa Recon

[https://docs.google.com/presentation/d/1k8A_sjJpMUsVdLY5cmtHxkbikn-WvOzD/edit#slide=id.p1](https://docs.google.com/presentation/d/1k8A_sjJpMUsVdLY5cmtHxkbikn-WvOzD/edit#slide=id.p1)

> Youtube

[ffuf scripts and tricks [NahamCon 2021]](https://www.youtube.com/watch?v=uwcRBSUl8e4)

> Oneliner

```rust
1. ffuf -c -u https://target .com -H “Host: FUZZ” -w vhost_wordlist.txt

2. ffuf -c -u http://bolt.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt -H "Host: FUZZ.bolt.htb" -fl 505

3. gobuster vhost -u http://horizontall.htb/ -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt -t 200

http://ffuf.me/sub/vhost
```

> With Nmap

```jsx
nmap --script http-vhosts -p 80,8080,443 target
```

> With FFUF

```jsx
#figure out response length of false positive

curl -s -H "Host: nonexistent.ffuf.io.fi" http://ffuf.io.fi | wc -c

# result is 612

# then filter out responses of len 612

ffuf -c -w /path/to/wordlist -u http://ffuf.io.fi -H "host: FUZZ.ffuf.io.fi" -fs 612

:)
```

> Vhosts in ssl certificate

```
echo | openssl s_client ––connect host:port | openssl x509 -noout -text | grep -i dns
```

### Subdomain Enumeration

---

[V-Host Enumeration](../source-archive/notion-export/Private%20%26%20Shared/Xetta%D1%82%D0%90%D0%A9s%20Web%20AppSEC%20Notes/Subdomain%20eumeration/V-Host%20Enumeration%202e17a3e4461d491ea3a067d9926208bc.md)

[TOOLS](../source-archive/notion-export/Private%20%26%20Shared/Xetta%D1%82%D0%90%D0%A9s%20Web%20AppSEC%20Notes/Subdomain%20eumeration/TOOLS%20a902f3b512814f0eaf26e640226ef831.md)


[Subdomains Enumeration Cheat Sheet](https://pentester.land/blog/subdomains-enumeration-cheatsheet/)


[https://m0chan.github.io/2019/12/17/Bug-Bounty-Cheetsheet.html](https://m0chan.github.io/2019/12/17/Bug-Bounty-Cheetsheet.html)


[Subdomain Enumeration: The Ultimate Guide](https://0xffsec.com/handbook/information-gathering/subdomain-enumeration/#fn:8)


[Subdomain Enumeration - The Right way (Prerequisites)](https://apexvicky.medium.com/subdomain-enumeration-the-right-way-prerequisites-7449ac0f2498)

- Subb brute By trickest

[Recon Experience with Trickest - Subdomain Recon Tale in a Workflow #1](https://trickest.medium.com/recon-experience-with-trickest-subdomain-recon-tale-in-a-workflow-1-a522717d1471)

[Recon Experience with Trickest - Subdomain Recon Tale in a Workflow #2 Brute - Forcing and...](https://trickest.medium.com/recon-experience-with-trickest-subdomain-recon-tale-in-a-workflow-2-brute-forcing-and-158b9be9e924)


[Subdomain Enumeration Tool Face-off 2022](https://blog.blacklanternsecurity.com/p/subdomain-enumeration-tool-face-off)
