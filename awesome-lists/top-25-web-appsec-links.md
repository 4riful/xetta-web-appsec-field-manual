---
title: "Top 25 Web AppSec Links"
summary: "A curated starting set of reputable Web AppSec references, not a generated link dump."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - awesome
  - curated
  - appsec
related:
  - ../QUICKSTART.md
  - ../playbooks/README.md
  - ../resources/README.md
references:
  - https://owasp.org/www-project-web-security-testing-guide/
  - https://portswigger.net/web-security
---

# Top 25 Web AppSec Links

This page is the fastest high-signal starting point in the manual.

It favors official standards, original research, reputable labs, and documentation that a security person can trust. Raw dumps, duplicate links, vague titles, private notes, and one-off commands do not belong here.

## Core Methodology

1. [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) - the primary public methodology for structured web application security testing.
2. [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) - turns security ideas into verifiable requirements and review criteria.
3. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - defensive implementation guidance for auth, sessions, access control, XSS, CSRF, SSRF, uploads, secrets, and more.
4. [OWASP Top 10](https://owasp.org/www-project-top-ten/) - useful risk taxonomy for communication, not a complete test plan.
5. [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) - API-specific risk map for BOLA, auth, excessive data exposure, SSRF, and inventory issues.

## Practical Learning

6. [PortSwigger Web Security Academy](https://portswigger.net/web-security) - the best free lab-safe web vulnerability training platform.
7. [PortSwigger Learning Paths](https://portswigger.net/web-security/learning-paths) - sequenced paths for building skill instead of link hopping.
8. [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - intentionally vulnerable app for safe local practice.
9. [OWASP crAPI](https://github.com/OWASP/crAPI) - intentionally vulnerable API for practicing API security issues.
10. [Bugcrowd University](https://www.bugcrowd.com/hackers/bugcrowd-university/) - practical researcher training and platform workflow guidance.

## Browser, Platform, And Protocol Foundations

11. [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security) - authoritative browser security reference for CSP, CORS, cookies, SOP, and secure contexts.
12. [MDN Same-Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) - foundational browser isolation model.
13. [MDN CORS](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS) - practical explanation of cross-origin API behavior.
14. [Web.dev Security](https://web.dev/secure/) - modern developer-focused web security guidance.
15. [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) - protocol-level reference for HTTP behavior.

## Bug-Class References

16. [PortSwigger XSS](https://portswigger.net/web-security/cross-site-scripting) - practical XSS explanations and labs.
17. [PortSwigger SQL Injection](https://portswigger.net/web-security/sql-injection) - SQLi methodology and labs.
18. [PortSwigger SSRF](https://portswigger.net/web-security/ssrf) - SSRF labs and filter-bypass concepts.
19. [PortSwigger Request Smuggling](https://portswigger.net/web-security/request-smuggling) - HTTP desync learning path.
20. [PortSwigger OAuth](https://portswigger.net/web-security/oauth) - common OAuth implementation mistakes and labs.

## Tools And Automation References

21. [Burp Suite Documentation](https://portswigger.net/burp/documentation) - official manual testing and proxy workflow documentation.
22. [OWASP ZAP Documentation](https://www.zaproxy.org/docs/) - open-source proxy and DAST documentation.
23. [ProjectDiscovery Documentation](https://docs.projectdiscovery.io/) - official docs for nuclei, httpx, subfinder, katana, naabu, interactsh, and automation workflows.
24. [Nuclei Templates Documentation](https://docs.projectdiscovery.io/templates/introduction) - template structure, matchers, extractors, and safe detector creation.
25. [SecLists](https://github.com/danielmiessler/SecLists) - broad security wordlist library; use carefully and only inside authorized scope.

## Honorable Mentions

- [Payloads All The Things](https://swisskyrepo.github.io/PayloadsAllTheThings/) - payload encyclopedia; use as reference, not as a blind testing script.
- [Assetnote Research](https://www.assetnote.io/resources/research) - high-signal real-world research and case studies.
- [Detectify Labs](https://labs.detectify.com/) - applied AppSec and attack surface research.
- [Intigriti Researcher Blog](https://www.intigriti.com/researchers/blog) - writeups, Bug Bytes, and challenge content.
- [HackerOne Hacktivity](https://hackerone.com/hacktivity) - public disclosed reports for pattern mining and report-quality study.

## Use Policy

Use these resources for education, defensive testing, secure development, and authorized assessment only.

Hands-on practice belongs in labs or explicitly authorized systems. Do not use this page as permission to scan, exploit, bypass controls, extract data, or test third-party systems.
