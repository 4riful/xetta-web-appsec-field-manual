---
title: "SSRF Payload Context"
summary: "Safe SSRF canary and URL-context guidance for authorized outbound request testing."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - payloads
  - ssrf
related:
  - ../bug-classes/server-side/ssrf.md
  - ../tools/out-of-band.md
  - ../reports/README.md
references:
  - https://portswigger.net/web-security/ssrf
  - https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html
---

# SSRF Payload Context

Use this page only after an in-scope feature is confirmed to make or attempt server-side outbound requests.

The safest SSRF proof is a controlled callback/canary that demonstrates server-side reachability without probing internal systems.

## Use When

- A feature accepts a URL, webhook, import source, preview target, or external resource reference.
- External callback testing is authorized.
- You control the callback destination and can preserve logs securely.

## Safe First Checks

- Use a controlled callback domain or approved OOB service.
- Include a unique canary path or token in the URL.
- Record DNS/HTTP callback time, source metadata, path, and headers if available.
- Test redirects only to approved destinations.

## Stop Conditions

Stop when:

- the callback proves server-side fetch behavior
- the next step would enumerate internal hosts
- the next step would request metadata or privileged services
- callback logs include sensitive data
- the program forbids external callbacks

## Evidence

Keep the triggering request, callback log, timestamp, source metadata, and explanation of why the destination should or should not be allowed.

## Related Bug Class

- [Server-Side Request Forgery](../bug-classes/server-side/ssrf.md)
