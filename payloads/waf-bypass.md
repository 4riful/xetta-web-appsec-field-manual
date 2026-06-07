---
title: "WAF Bypass Payload Context"
summary: "Safe context notes for filter and WAF bypass testing after an underlying bug class is identified."
status: "reviewed"
last_reviewed: "2026-06-08"
tags:
  - payloads
  - waf-bypass
related:
  - ../bug-classes/defensive-bypass/waf-bypass.md
  - ../payloads/README.md
references:
  - https://owasp.org/www-project-web-application-firewall-evaluation-criteria/
---

# WAF Bypass Payload Context

WAF bypass payloads are not findings by themselves. They are test inputs used to show that a defensive layer and the application disagree about equivalent input.

## Use When

- A real underlying bug class is already suspected or confirmed.
- You know which parser, filter, proxy, or application layer is being compared.
- The test can be done with a small number of controlled requests.

## Safe First Checks

- Compare one encoded/normalized representation at a time.
- Keep requests low-volume.
- Avoid broad mutation lists unless explicitly authorized.
- Record both blocked and accepted behavior.

## Stop Conditions

Stop when:

- the parser/filter mismatch is clear
- the next step would require noisy mutation
- the payload would affect other users or application state
- there is no underlying application impact

## Reporting Note

Report the underlying control failure. A better remediation is usually server-side authorization, context-safe encoding, parameterization, canonicalization, or allowlisting, not merely adding another WAF rule.

## Related Bug Class

- [WAF And Filter Bypass](../bug-classes/defensive-bypass/waf-bypass.md)
