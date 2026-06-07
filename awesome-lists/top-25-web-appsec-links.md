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

This is the manual's core library: standards, labs, primary documentation, and current references a security person can trust.

It is intentionally not a payload dump. Topic-specific cheat sheets, writeups, and tools belong in resource pages unless they are broadly useful across assessments.

## Methodology And Requirements

1. [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) - primary public methodology for structured web application security testing.
2. [OWASP Application Security Verification Standard](https://owasp.org/www-project-application-security-verification-standard/) - turns AppSec expectations into testable requirements.
3. [OWASP Cheat Sheet Series](https://cheatsheetseries.owasp.org/) - defensive implementation guidance for auth, sessions, access control, XSS, CSRF, SSRF, uploads, secrets, and more.
4. [OWASP SAMM](https://owasp.org/www-project-samm/) - maturity model for improving secure software delivery, not just testing individual apps.
5. [CISA Secure by Design](https://www.cisa.gov/resources-tools/resources/secure-by-design) - product-security guidance for secure defaults, accountability, and reducing whole vulnerability classes.

## Labs And Practice

6. [PortSwigger Web Security Academy](https://portswigger.net/web-security) - one of the strongest free lab-safe web vulnerability training platforms.
7. [PortSwigger Learning Paths](https://portswigger.net/web-security/learning-paths) - sequenced paths for building skill instead of link hopping.
8. [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) - intentionally vulnerable app for safe local web AppSec practice.
9. [OWASP crAPI](https://github.com/OWASP/crAPI) - intentionally vulnerable API for BOLA, auth, rate-limit, and API inventory practice.
10. [PortSwigger Web LLM Attacks](https://portswigger.net/web-security/llm-attacks) - lab-safe LLM application testing content covering prompt injection, tools, APIs, and output handling.

## Browser, Protocol, And Auth Foundations

11. [MDN Web Security](https://developer.mozilla.org/en-US/docs/Web/Security) - practical browser security reference for CSP, CORS, cookies, SOP, and secure contexts.
12. [MDN Same-Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy) - foundational browser isolation model.
13. [RFC 9110 HTTP Semantics](https://www.rfc-editor.org/rfc/rfc9110.html) - protocol-level reference for methods, headers, status codes, and HTTP behavior.
14. [RFC 9700 OAuth 2.0 Security BCP](https://www.rfc-editor.org/rfc/rfc9700.html) - current OAuth security best current practice for modern implementations.
15. [W3C WebAuthn Level 3](https://www.w3.org/TR/webauthn-3/) - primary reference for passkeys, public-key credentials, origin binding, and relying-party behavior.

## API And Automation

16. [OWASP API Security Top 10](https://owasp.org/www-project-api-security/) - API-specific risk taxonomy for BOLA, auth, inventory, SSRF, and unsafe API consumption.
17. [OpenAPI Specification](https://spec.openapis.org/oas/latest.html) - API contract standard for inventory, test planning, and request/response modeling.
18. [GraphQL Specification](https://spec.graphql.org/) - primary reference for GraphQL schema, validation, execution, introspection, and type behavior.
19. [Burp Suite Documentation](https://portswigger.net/burp/documentation) - official manual proxy and testing workflow documentation.
20. [OWASP ZAP Documentation](https://www.zaproxy.org/docs/) - open-source proxy and DAST documentation.
21. [ProjectDiscovery Documentation](https://docs.projectdiscovery.io/) - official docs for nuclei, httpx, subfinder, katana, naabu, interactsh, and automation workflows.

## AI, Reporting, And Prioritization

22. [OWASP Top 10 for LLM Applications](https://genai.owasp.org/llm-top-10/) - baseline risk taxonomy for LLM-backed applications.
23. [OWASP AI Exchange](https://owasp.org/www-project-ai-security-and-privacy-guide/) - broad AI security and privacy control guidance beyond LLM-specific risks.
24. [CWE Top 25](https://cwe.mitre.org/top25/) - root-cause weakness reference for remediation-oriented reporting.
25. [FIRST CVSS v4.0](https://www.first.org/cvss/) - current severity scoring standard for consistent vulnerability communication.

## Honorable Mentions

- [OWASP GenAI Security Project Resources](https://genai.owasp.org/resources/) - living hub for LLM, agentic AI, governance, and GenAI security resources.
- [OWASP Agentic AI: Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) - useful for tool-using, memory-backed, and autonomous AI systems.
- [CISA Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) - exploited-in-the-wild prioritization signal.
- [FIRST EPSS](https://www.first.org/epss/) - exploit-likelihood signal that complements severity scoring.
- [Payloads All The Things](https://swisskyrepo.github.io/PayloadsAllTheThings/) - payload encyclopedia; use as reference, not as a blind testing script.
- [SecLists](https://github.com/danielmiessler/SecLists) - broad security wordlist library; use carefully and only inside authorized scope.
- [Assetnote Research](https://www.assetnote.io/resources/research) - high-signal real-world research and case studies.
- [HackerOne Hacktivity](https://hackerone.com/hacktivity) - public disclosed reports for pattern mining and report-quality study.

## Use Policy

Use these resources for education, defensive testing, secure development, and authorized assessment only.

Hands-on practice belongs in labs or explicitly authorized systems. Do not use this page as permission to scan, exploit, bypass controls, extract data, or test third-party systems.

Do not start with tools, payload repositories, or disclosed reports until you understand the relevant methodology and scope. Honorable mentions should stay short; if that section grows beyond 5-8 links, move items into topic-specific resource pages.
