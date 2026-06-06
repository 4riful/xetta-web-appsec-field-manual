---
title: "CORS And CSRF"
summary: "Browser trust-boundary resources for CORS misconfiguration, CSRF, credentialed requests, and origin handling."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - bug-class
  - cors-csrf
related: []
references: []
---
# CORS And CSRF

CORS and CSRF are browser trust-boundary bugs. They are not proven by a header alone. Confirm whether credentials are included, whether sensitive actions are possible, and whether the victim browser can be made to send the relevant request.

## Core Resources

### cors misconfiguration

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `cors-csrf`
- Tier: `tier_2_useful`
- Value: https://0xn3va.gitbook.io/cheat-sheets/web-application/cors-misconfiguration

### csrf cross site request forgery

- Type: `cheat_sheet`
- Kind: `url`
- Bug class: `cors-csrf`
- Tier: `tier_1_core`
- Value: https://book.hacktricks.xyz/pertesting-web/csrf-cross-site-request-forgery

## Testing Notes

- For CORS, check `Access-Control-Allow-Origin`, `Access-Control-Allow-Credentials`, origin reflection, `null` origin, wildcard behavior, and regex/subdomain mistakes.
- For CSRF, check whether the action relies only on browser cookies and whether the request can be triggered cross-site without an unpredictable token.
- A CORS issue becomes stronger when it exposes sensitive authenticated data to an attacker-controlled origin.
- A CSRF issue becomes stronger when it changes email, password, payout settings, API keys, roles, or other security-sensitive state.

## Related

- [Client-Side Bug Classes](./README.md)
- [XSS And Client-Side Resources](../../resources/xss-and-client-side.md)
- [WAF / CORS / CSRF / Smuggling Resources](../../resources/waf-cors-csrf-smuggling.md)
