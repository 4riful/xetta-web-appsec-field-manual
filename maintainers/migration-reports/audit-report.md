---
title: "Audit Report"
summary: "Inventory and quality audit for the migrated Notion export."
tags:
  - report
  - migration
related_topics:
  - "Repository Migration"
references:
---
# Audit Report

## Executive Summary

- Source archive: `/mnt/d/xettaswebapppentestinghandbook.zip` -> nested Notion export ZIP.
- Markdown pages scanned: 66.
- Assets scanned: 3.
- External links found: 432.
- Empty or near-empty pages: 3 empty, 27 stubs.
- Exact duplicate documents by normalized hash: 0 groups.
- Near duplicates or fragmented concepts identified: 4 groups.

## Findings

- The original folder `Bugs` mixed vulnerability classes, index pages, stubs, and cloud/network topics.
- Several top-level pages were resource dumps rather than standalone documentation.
- Notion-export IDs polluted filenames and were removed in the canonical repository.
- `Subdomain eumeration` contained a typo and split overview/tool/vhost content across multiple pages.
- Multiple vulnerability notes were stubs that pointed to a single external reference; they were preserved but grouped into canonical topics.
- Three PNG assets were present and preserved both in the raw archive and normalized under `assets/images/`.

## Empty Pages

- `Private & Shared/XettaтАЩs Web AppSEC Notes/0days 2c824a24402344d1a18ccdc202bf4dea.md`
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Blogs 7ddd522c024441e59efcd8ba3c29558b.md`
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/CORS b3f20e3518bb4862accff1155d79365f.md`

## Stub Pages

- `Private & Shared/XettaтАЩs Web AppSEC Notes/Active Directory 265438fe29144462983eac15793ca5ff.md` (10 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Asset Discovery 1e94ffbbd6ae47898546d465d075bd81.md` (9 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bookmarks 03cc554e8e9d462aa15edc015b428e1a.md` (15 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/0 - DAY 368eb2d51f284424bd0d4b66e0b59cce.md` (15 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/403 Bypass 768ee1f5236d4af1aabf1e52fff3a1e9.md` (18 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Account takeover 767e1ea2b74e4230984065bd81352e74.md` (12 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Command Injection fe2f4f79498344daa4589fa0dcb75a8b.md` (9 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Dns 7eb82bf0f46e403783822e35be2af5bb.md` (9 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload e394e3cbdba340448f462fb5304803de.md` (18 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload f30fc3097e014c6494fcfe858e4c0e85.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/LFI 523bd5023fdd40bbb08c7116e0b21fe1.md` (20 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Password Reset 77a6cd8d5af842588866dfd4f7b65dee.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Port Scanning 6d3cbe0c749148aa9cbcf52647ae2123.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/RCE 444aaa7c978444d1adf51583799c1a35.md` (15 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/WAF BYPASS fc99a4561cf641c9b9364a316b5336db.md` (18 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/CODE Review 11516e1de3fd4f439b091aea6b9d5df6.md` (19 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Dorking techniques b49ac278a7f44070b6e595f3876e7db8.md` (22 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/MindMaps 97fe4e81e9c5487e968c498984760a00.md` (24 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Oscp Preparation 321052e948124165a3e4c03e0dbd28c1.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things/v1 recon 774f918d99da462d8ac54faeb14719c6.md` (7 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Red teaming 26997c46b93d8015bf30e252925608bf.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Source Code Analysis b0d2eddfc2e24f5c80df31ba34e25471.md` (18 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/TOOLS a902f3b512814f0eaf26e640226ef831.md` (12 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Toolkit & Hacks 7ccc3c4e9c184fb9b668d7243c5e2a80.md` (10 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Twitter tips a368211f6b2a4f7b91dfb2aa5f7fb230.md` (9 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/WAF Bypass 4a6ba2181f5d41acb899f1617448f144.md` (14 words)
- `Private & Shared/XettaтАЩs Web AppSEC Notes/Wordlist d779840dc9274225b070814f6b373cf0.md` (14 words)

## Near Duplicates And Fragments

- **File Upload**: Bugs/File Upload e394e3cbdba340448f462fb5304803de.md, Bugs/File Upload f30fc3097e014c6494fcfe858e4c0e85.md - Duplicate topic with one stub and one canonical resource pointer.
- **WAF Bypass**: WAF Bypass 4a6ba2181f5d41acb899f1617448f144.md, Bugs/WAF BYPASS fc99a4561cf641c9b9364a316b5336db.md - Same concept split between top-level resource and vulnerability page.
- **AWS Security**: Bugs/AwS3 d42978bf1a9a4260b021b793fe883288.md, Bugs/cloudSec AWS f107a022672340eaa05f87af4938ba3d.md - Cloud/AWS/S3 notes overlap and are better maintained together.
- **Zero-Day Research**: 0days 2c824a24402344d1a18ccdc202bf4dea.md, Bugs/0 - DAY 368eb2d51f284424bd0d4b66e0b59cce.md - Both are zero-day resource stubs.

## Asset Inventory

| Source | Normalized Destination | SHA-256 Prefix |
|---|---|---|
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/IDOR/Untitled 1.png` | `assets/images/image-01.png` | `1d0875267164` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/IDOR/Untitled.png` | `assets/images/image-02.png` | `074e60f77f65` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things/v1 recon/Untitled.png` | `assets/images/image-03.png` | `feb8a3a0c321` |

## Full Markdown Inventory

| Source File | Title | Words | Links | Canonical Destination |
|---|---:|---:|---:|---|
| `Private & Shared/XettaтАЩs Web AppSEC Notes/0days 2c824a24402344d1a18ccdc202bf4dea.md` | Zero-Day Research | 4 | 1 | `vulnerabilities/zero-day-and-miscellaneous.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/ALL IN ONE Cheat Sheets c263b653a9d344e9876cf60e7b759ffc.md` | All-in-One Cheat Sheets | 673 | 49 | `resources/cheat-sheets.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Active Directory 265438fe29144462983eac15793ca5ff.md` | Active Directory | 10 | 1 | `resources/videos-mindmaps-and-training.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Asset Discovery 1e94ffbbd6ae47898546d465d075bd81.md` | Asset Discovery | 9 | 1 | `methodology/recon-methodology.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Automation & Script Devs ee773c0f42234d43a0c4370dc87e7328.md` | Automation & Script Devs | 74 | 3 | `tooling/automation-and-fuzzing.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/AweSome BlogPost 465a8707c7e0436abb674ae52c18b490.md` | Awesome Blog Posts | 193 | 20 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/AweSome Live Gitbooks 3ed0973ef7bf40829ecb8ec0b9980861.md` | Awesome Live Gitbooks | 105 | 10 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Blogs 7ddd522c024441e59efcd8ba3c29558b.md` | Blogs | 5 | 1 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bookmarks 03cc554e8e9d462aa15edc015b428e1a.md` | Bookmarks | 15 | 2 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/0 - DAY 368eb2d51f284424bd0d4b66e0b59cce.md` | Zero-Day Research | 15 | 1 | `vulnerabilities/zero-day-and-miscellaneous.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/403 Bypass 768ee1f5236d4af1aabf1e52fff3a1e9.md` | 403 Bypass | 18 | 1 | `vulnerabilities/access-control-and-business-logic.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/API 3c82b2c98c5f457ba168b706b2a0bb86.md` | API | 60 | 6 | `vulnerabilities/api-and-graphql.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Account takeover 767e1ea2b74e4230984065bd81352e74.md` | Account takeover | 12 | 1 | `vulnerabilities/authentication-and-account-security.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Auth Bypass d97162a3fb2b437a9d55c5a068dfe8c5.md` | Auth Bypass | 67 | 4 | `vulnerabilities/authentication-and-account-security.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/AwS3 d42978bf1a9a4260b021b793fe883288.md` | AWS S3 Security | 29 | 3 | `vulnerabilities/cloud-and-aws-security.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/CORS b3f20e3518bb4862accff1155d79365f.md` | CORS | 1 | 0 | `vulnerabilities/cors.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Command Injection fe2f4f79498344daa4589fa0dcb75a8b.md` | Command Injection | 9 | 1 | `vulnerabilities/command-injection-and-rce.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Dns 7eb82bf0f46e403783822e35be2af5bb.md` | DNS Security | 9 | 1 | `vulnerabilities/dns-and-port-scanning.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload e394e3cbdba340448f462fb5304803de.md` | File Upload | 18 | 1 | `vulnerabilities/file-upload.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload f30fc3097e014c6494fcfe858e4c0e85.md` | File Upload | 14 | 1 | `vulnerabilities/file-upload.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/GraphQL fb36e66b207a481795ae86ad29c412f3.md` | GraphQL | 65 | 1 | `vulnerabilities/api-and-graphql.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/HTTP SMUGLING e9eb11c9d3864f93acd75aa1f016a4f3.md` | HTTP Request Smuggling | 111 | 5 | `vulnerabilities/http-request-smuggling.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/IDOR 5d3f49249f2740b4b5f70a70cd3afb87.md` | IDOR | 57 | 2 | `vulnerabilities/access-control-and-business-logic.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/LFI 523bd5023fdd40bbb08c7116e0b21fe1.md` | LFI | 20 | 1 | `vulnerabilities/xxe-and-lfi.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Logic Bypass 7e95162bb82c430c83718146bb4535f4.md` | Logic Bypass | 64 | 2 | `vulnerabilities/access-control-and-business-logic.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Misc 4f15937f20ec4069bc7d5f75299699e1.md` | Miscellaneous Vulnerabilities | 30 | 2 | `vulnerabilities/zero-day-and-miscellaneous.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Password Reset 77a6cd8d5af842588866dfd4f7b65dee.md` | Password Reset | 14 | 1 | `vulnerabilities/authentication-and-account-security.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Port Scanning 6d3cbe0c749148aa9cbcf52647ae2123.md` | Port Scanning | 14 | 1 | `vulnerabilities/dns-and-port-scanning.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/RCE 444aaa7c978444d1adf51583799c1a35.md` | RCE | 15 | 1 | `vulnerabilities/command-injection-and-rce.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/SQL injection 744552967cf74b78b19398b3e476316b.md` | SQL injection | 112 | 7 | `vulnerabilities/sql-injection.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/SSRF 5bb6cfbd823840f8bb3bd809ab5809f5.md` | SSRF | 207 | 12 | `vulnerabilities/ssrf.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/WAF BYPASS fc99a4561cf641c9b9364a316b5336db.md` | WAF BYPASS | 18 | 1 | `vulnerabilities/waf-bypass.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/XSS 9249e451b45840a089fed1ce1027a836.md` | XSS | 105 | 9 | `vulnerabilities/xss.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/XXE 907847798a544e60a65a87e580c87269.md` | XXE | 46 | 2 | `vulnerabilities/xxe-and-lfi.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/cloudSec AWS f107a022672340eaa05f87af4938ba3d.md` | Cloud Security and AWS | 26 | 2 | `vulnerabilities/cloud-and-aws-security.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs 5849fd829b084890baaf176cd27d6aba.md` | Bugs | 186 | 1 | `resources/uncategorized/bugs.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/CODE Review 11516e1de3fd4f439b091aea6b9d5df6.md` | Code Review | 19 | 2 | `code-review/source-code-analysis.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Dorking techniques b49ac278a7f44070b6e595f3876e7db8.md` | Dorking techniques | 22 | 3 | `recon/osint-and-dorking.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Fuzzing dcfac0a8d57441b4830ffca259b48319.md` | Fuzzing | 63 | 5 | `tooling/automation-and-fuzzing.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/JS IN BUG BOUNTY acc2704513a84087aed6d17ca5d44a15.md` | JavaScript Recon for Bug Bounty | 62 | 3 | `recon/javascript-recon.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/MISC 3c874076a97941ca9308c76ecfca542a.md` | Miscellaneous Resources | 95 | 6 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/MindMaps 97fe4e81e9c5487e968c498984760a00.md` | MindMaps | 24 | 1 | `resources/videos-mindmaps-and-training.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/OSINT WEB TOOLS 9c714449ecee4488ace9cd1885d52e09.md` | OSINT WEB TOOLS | 115 | 29 | `recon/osint-and-dorking.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Onliner 9e50211bacab4adfab82c068a28a5070.md` | One-Liners | 146 | 6 | `tooling/automation-and-fuzzing.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Oscp Preparation 321052e948124165a3e4c03e0dbd28c1.md` | OSCP Preparation | 14 | 1 | `resources/videos-mindmaps-and-training.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/PAYLOADS ba930704f4a14ef4a9fba4ff95af27a6.md` | Payloads | 48 | 4 | `tooling/payloads-and-wordlists.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things/v1 recon 774f918d99da462d8ac54faeb14719c6.md` | v1 recon | 7 | 0 | `resources/uncategorized/v1-recon.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things 08b9dadb798c4fc194be6627a7ef998b.md` | Recon All the things | 302 | 15 | `methodology/recon-methodology.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Red teaming 26997c46b93d8015bf30e252925608bf.md` | Red teaming | 14 | 1 | `resources/videos-mindmaps-and-training.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Source Code Analysis b0d2eddfc2e24f5c80df31ba34e25471.md` | Source Code Analysis | 18 | 1 | `code-review/source-code-analysis.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/TOOLS a902f3b512814f0eaf26e640226ef831.md` | Subdomain Enumeration Tools | 12 | 1 | `recon/subdomain-enumeration.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/V-Host Enumeration 2e17a3e4461d491ea3a067d9926208bc.md` | Virtual Host Enumeration | 188 | 8 | `recon/subdomain-enumeration.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration 084630216b8f46e891dd2a7896eb31e6.md` | Subdomain Enumeration | 163 | 7 | `recon/subdomain-enumeration.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/TIPS 03af46c2c9954890be1ae8910e9ba344.md` | General Tips | 93 | 5 | `methodology/bug-bounty-workflow.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md` | Tips From EMAD Shanab | 2815 | 114 | `methodology/bug-bounty-workflow.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Burp Extensions 9e2504a523d748f0b96ac8ec259bacb9.md` | Burp Suite Extensions | 150 | 13 | `tooling/burp-suite-and-toolkit.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Toolkit & Hacks 7ccc3c4e9c184fb9b668d7243c5e2a80.md` | Toolkit and Hacks | 10 | 1 | `tooling/burp-suite-and-toolkit.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions 5ce540fb07664fe09f3c25ccb8e39443.md` | Toolkit and Burp Suite Extensions | 202 | 14 | `tooling/burp-suite-and-toolkit.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Twitter tips a368211f6b2a4f7b91dfb2aa5f7fb230.md` | Twitter tips | 9 | 1 | `resources/uncategorized/twitter-tips.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/WAF Bypass 4a6ba2181f5d41acb899f1617448f144.md` | WAF Bypass | 14 | 1 | `vulnerabilities/waf-bypass.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Wordlist d779840dc9274225b070814f6b373cf0.md` | Wordlist | 14 | 1 | `tooling/payloads-and-wordlists.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Workflow Cheatsheet 99bf8927e2b94472933fa8877ac55f80.md` | Workflow | Cheatsheet | 163 | 11 | `methodology/bug-bounty-workflow.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/YouTube bd5c2d34b12140d08f73cf45d2427844.md` | YouTube | 114 | 7 | `resources/videos-mindmaps-and-training.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/checklist fc6500d29706427bb09b30824ea5a2ec.md` | Checklist | 88 | 6 | `methodology/bug-bounty-workflow.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/writeups Collection 0dc41ed16ef14f238671c260b22e8c83.md` | Writeups Collection | 185 | 7 | `resources/blogs-writeups-and-gitbooks.md` |
| `Private & Shared/XettaтАЩs Web AppSEC Notes b6950bcb2a864c36809946e4c1324ea5.md` | Xetta Web AppSec Handbook | 452 | 0 | `resources/uncategorized/xetta-web-appsec-handbook.md` |
