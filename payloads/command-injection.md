---
title: "Command Injection"
summary: "Command-injection payload references, blind execution notes, and safe validation guidance."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - payloads
  - command-injection
related: []
references: []
---
# Command Injection

Command-injection payloads only make sense when user-controlled input reaches an operating-system command, script wrapper, shell expansion, archive handler, conversion utility, network diagnostic feature, or backend automation task.

Use harmless proof first. Prefer timing, controlled callbacks, or reading non-sensitive command output only when scope allows it.

## Source Resource

### blind command injection

- Type: `article`
- Kind: `url`
- Bug class: `general`
- Tier: `tier_2_useful`
- Value: https://bergee.it/blog/blind-command-injection/

## Testing Notes

- Look for features that execute diagnostics, image tools, PDF tools, archive tools, import/export jobs, or webhook processors.
- Track whether input is inserted into a shell command or passed as a safer argument array.
- Blind cases need timing or out-of-band evidence; do not assume no response means no execution.
- Document the exact parameter, request, timing difference, callback, or command output used as proof.

## Related

- [Injection Bug Classes](../bug-classes/injection/README.md)
- [RCE / CVE Resources](../resources/rce-cves-and-0days.md)
- [Out-Of-Band Tools](../tools/out-of-band.md)
