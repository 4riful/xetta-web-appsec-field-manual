---
title: "Tools"
summary: "Tool selection guide organized by job, noise level, input, and validation requirement."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - tools
related: []
references: []
---
# Tools

Tools support a hypothesis. They do not replace one.

Use this section after you know:

- the authorized scope
- the job you need the tool to perform
- the expected input
- the expected output
- how you will manually validate results

## Tool Selection Rules

1. Pick the job before picking the tool.
2. Prefer passive or low-noise collection first.
3. Use active scanning only when scope and rate limits allow it.
4. Treat tool output as leads, not findings.
5. Record command inputs, timestamps, and scope.
6. Validate manually before reporting.

## Tool Buckets

| Job | Page | Typical input | Output | Noise |
|---|---|---|---|---|
| Recon | [Recon](./recon.md) | domains, orgs, CIDRs | candidate assets | passive to active |
| Content discovery | [Content Discovery](./content-discovery.md) | base URLs, hosts | paths, endpoints, vhosts | active |
| JavaScript analysis | [JavaScript Analysis](./javascript-analysis.md) | JS URLs, app URLs | routes, endpoint leads, secret leads | passive/low |
| Proxy-assisted review | [Burp Extensions](./burp-extensions.md) | proxy traffic | workflow-specific leads | low to active |
| Fuzzing | [Fuzzing](./fuzzing.md) | URLs, params, wordlists | anomalies | active/noisy |
| Out-of-band validation | [Out Of Band](./out-of-band.md) | callback domain, payload sink | callback evidence | controlled active |
| Cloud exposure | [Cloud](./cloud.md) | cloud assets, buckets, domains | exposure leads | passive to active |
| API / GraphQL | [API / GraphQL](./api-graphql.md) | routes, schemas, tokens | endpoint/schema findings | low to active |
| Automation | [Automation](./automation.md) | approved workflow inputs | repeatable pipeline output | varies |

## Passive, Low-Noise, Active, Noisy

- Passive: no direct target interaction or only third-party/public data.
- Low-noise: normal browsing or small controlled request sets.
- Active: sends crafted requests to in-scope systems.
- Noisy: high-volume fuzzing, scanning, brute-force-like behavior, or templates that may alter application state.

## Before Running A Tool

Document:

- scope item
- reason for running
- input file or source
- expected output
- rate limit
- stop condition
- evidence location

## After Running A Tool

Ask:

- Is the asset in scope?
- Is the result reproducible?
- Is this a vulnerability or only exposure?
- What bug class does it support?
- What manual request/response proves it?
- Could this be a false positive?

## Tool Page Standard

Every tool/topic page should include:

- job solved
- passive/active behavior
- inputs
- safe example
- output interpretation
- false positives
- when not to run it
- related playbooks
- related bug classes
- official documentation

## When Not To Use Tools

Do not run tools when:

- scope is unclear
- rate limits are unknown
- the output cannot be interpreted
- production availability may be affected
- the program forbids automation
- manual validation would be safer and enough

If you cannot explain what tool output means, do not report it yet. Pair tool output with a bug-class page, payload context, and evidence from [Reports](../reports/README.md).
