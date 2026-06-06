---
title: "Resource Completeness Check"
summary: "Verification that every HTTP/HTTPS resource extracted from every raw Markdown file is present in the published resource indexes."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - resources
  - qa
  - source-coverage
related:
  - ../RESOURCES.md
  - source-resource-links.md
  - exhaustive-source-catalog.md
references: []
---
# Resource Completeness Check

## Result

PASS. Every normalized HTTP/HTTPS URL extracted from every raw Markdown file is present in the published resource indexes.

## Scope

- Raw Markdown files checked: `66`
- Raw Markdown files with zero HTTP/HTTPS URLs: `3`
- HTTP/HTTPS URL occurrences checked: `533`
- Unique normalized HTTP/HTTPS URLs checked: `406`
- Published index files checked: `18`
- Missing unique HTTP/HTTPS URLs: `0`
- Markdown link targets observed, including local Notion links and images: `273`
- Unique Markdown link targets observed: `260`

## What Was Compared

Source side: every `*.md` file under `source-archive/notion-export/`.

Published resource side:

- `RESOURCES.md`
- `08-reference-library/all-source-resources.md`
- every file under `08-reference-library/resource-indexes/`
- `maintainers/source-resource-links.md`

## Notes

- This check verifies HTTP/HTTPS resource availability in the public resource indexes.
- The source catalog and `RESOURCES.md` preserve the original extraction counts. This check uses normalized URL boundaries for comparison, so the comparison count can differ by one from the raw extraction count when a malformed source snippet includes punctuation or markup at the URL boundary.
- Local Notion page links, image links, and relative archive references are preserved by `source-archive/notion-export/` and inventoried in `maintainers/exhaustive-source-catalog.md`.
- Some source URLs are placeholders or payload strings such as localhost, target placeholders, OOB examples, and malformed source snippets. They are still preserved because they existed in the original ZIP export.

## Per-File Coverage

| Source Markdown file | URL occurrences | Unique URLs | Markdown targets | Missing URLs |
|---|---:|---:|---:|---:|
| `Private & Shared/XettaтАЩs Web AppSEC Notes/0days 2c824a24402344d1a18ccdc202bf4dea.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/ALL IN ONE Cheat Sheets c263b653a9d344e9876cf60e7b759ffc.md` | 57 | 49 | 23 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Active Directory 265438fe29144462983eac15793ca5ff.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Asset Discovery 1e94ffbbd6ae47898546d465d075bd81.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Automation & Script Devs ee773c0f42234d43a0c4370dc87e7328.md` | 4 | 3 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/AweSome BlogPost 465a8707c7e0436abb674ae52c18b490.md` | 38 | 24 | 19 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/AweSome Live Gitbooks 3ed0973ef7bf40829ecb8ec0b9980861.md` | 20 | 10 | 10 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Blogs 7ddd522c024441e59efcd8ba3c29558b.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bookmarks 03cc554e8e9d462aa15edc015b428e1a.md` | 2 | 2 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/0 - DAY 368eb2d51f284424bd0d4b66e0b59cce.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/403 Bypass 768ee1f5236d4af1aabf1e52fff3a1e9.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/API 3c82b2c98c5f457ba168b706b2a0bb86.md` | 7 | 6 | 3 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Account takeover 767e1ea2b74e4230984065bd81352e74.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Auth Bypass d97162a3fb2b437a9d55c5a068dfe8c5.md` | 4 | 4 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/AwS3 d42978bf1a9a4260b021b793fe883288.md` | 3 | 3 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/CORS b3f20e3518bb4862accff1155d79365f.md` | 0 | 0 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Command Injection fe2f4f79498344daa4589fa0dcb75a8b.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Dns 7eb82bf0f46e403783822e35be2af5bb.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload e394e3cbdba340448f462fb5304803de.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/File Upload f30fc3097e014c6494fcfe858e4c0e85.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/GraphQL fb36e66b207a481795ae86ad29c412f3.md` | 2 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/HTTP SMUGLING e9eb11c9d3864f93acd75aa1f016a4f3.md` | 6 | 5 | 5 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/IDOR 5d3f49249f2740b4b5f70a70cd3afb87.md` | 2 | 2 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/LFI 523bd5023fdd40bbb08c7116e0b21fe1.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Logic Bypass 7e95162bb82c430c83718146bb4535f4.md` | 2 | 2 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Misc 4f15937f20ec4069bc7d5f75299699e1.md` | 2 | 2 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Password Reset 77a6cd8d5af842588866dfd4f7b65dee.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/Port Scanning 6d3cbe0c749148aa9cbcf52647ae2123.md` | 2 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/RCE 444aaa7c978444d1adf51583799c1a35.md` | 2 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/SQL injection 744552967cf74b78b19398b3e476316b.md` | 7 | 7 | 3 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/SSRF 5bb6cfbd823840f8bb3bd809ab5809f5.md` | 14 | 12 | 9 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/WAF BYPASS fc99a4561cf641c9b9364a316b5336db.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/XSS 9249e451b45840a089fed1ce1027a836.md` | 12 | 9 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/XXE 907847798a544e60a65a87e580c87269.md` | 2 | 2 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs/cloudSec AWS f107a022672340eaa05f87af4938ba3d.md` | 2 | 2 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Bugs 5849fd829b084890baaf176cd27d6aba.md` | 2 | 1 | 27 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/CODE Review 11516e1de3fd4f439b091aea6b9d5df6.md` | 2 | 2 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Dorking techniques b49ac278a7f44070b6e595f3876e7db8.md` | 3 | 3 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Fuzzing dcfac0a8d57441b4830ffca259b48319.md` | 5 | 5 | 5 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/JS IN BUG BOUNTY acc2704513a84087aed6d17ca5d44a15.md` | 3 | 3 | 3 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/MISC 3c874076a97941ca9308c76ecfca542a.md` | 7 | 6 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/MindMaps 97fe4e81e9c5487e968c498984760a00.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/OSINT WEB TOOLS 9c714449ecee4488ace9cd1885d52e09.md` | 30 | 28 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Onliner 9e50211bacab4adfab82c068a28a5070.md` | 7 | 6 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Oscp Preparation 321052e948124165a3e4c03e0dbd28c1.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/PAYLOADS ba930704f4a14ef4a9fba4ff95af27a6.md` | 4 | 4 | 2 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things/v1 recon 774f918d99da462d8ac54faeb14719c6.md` | 0 | 0 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Recon All the things 08b9dadb798c4fc194be6627a7ef998b.md` | 20 | 15 | 13 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Red teaming 26997c46b93d8015bf30e252925608bf.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Source Code Analysis b0d2eddfc2e24f5c80df31ba34e25471.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/TOOLS a902f3b512814f0eaf26e640226ef831.md` | 2 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration/V-Host Enumeration 2e17a3e4461d491ea3a067d9926208bc.md` | 9 | 7 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Subdomain eumeration 084630216b8f46e891dd2a7896eb31e6.md` | 8 | 7 | 9 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/TIPS 03af46c2c9954890be1ae8910e9ba344.md` | 7 | 5 | 5 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md` | 113 | 104 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Burp Extensions 9e2504a523d748f0b96ac8ec259bacb9.md` | 26 | 13 | 13 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions/Toolkit & Hacks 7ccc3c4e9c184fb9b668d7243c5e2a80.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Toolkit and Burpsuite Extensions 5ce540fb07664fe09f3c25ccb8e39443.md` | 28 | 14 | 16 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Twitter tips a368211f6b2a4f7b91dfb2aa5f7fb230.md` | 1 | 1 | 0 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/WAF Bypass 4a6ba2181f5d41acb899f1617448f144.md` | 1 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Wordlist d779840dc9274225b070814f6b373cf0.md` | 2 | 1 | 1 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/Workflow Cheatsheet 99bf8927e2b94472933fa8877ac55f80.md` | 15 | 12 | 8 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/YouTube bd5c2d34b12140d08f73cf45d2427844.md` | 13 | 7 | 6 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/checklist fc6500d29706427bb09b30824ea5a2ec.md` | 7 | 6 | 4 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes/writeups Collection 0dc41ed16ef14f238671c260b22e8c83.md` | 9 | 9 | 6 | 0 |
| `Private & Shared/XettaтАЩs Web AppSEC Notes b6950bcb2a864c36809946e4c1324ea5.md` | 0 | 0 | 34 | 0 |
