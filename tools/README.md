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

**Recon**
[Recon](./recon.md) starts from domains, orgs, or CIDRs and produces candidate assets. Noise: passive to active.

**Content discovery**
[Content Discovery](./content-discovery.md) starts from base URLs or hosts and produces paths, endpoints, and vhosts. Noise: active.

**JavaScript analysis**
[JavaScript Analysis](./javascript-analysis.md) starts from JS URLs or app URLs and produces route, endpoint, and secret leads. Noise: passive/low.

**Proxy-assisted review**
[Burp Extensions](./burp-extensions.md) starts from proxy traffic and produces workflow-specific leads. Noise: low to active.

**Fuzzing**
[Fuzzing](./fuzzing.md) starts from URLs, parameters, and wordlists and produces anomalies. Noise: active/noisy.

**Out-of-band validation**
[Out Of Band](./out-of-band.md) starts from a callback domain and payload sink and produces callback evidence. Noise: controlled active.

**Cloud exposure**
[Cloud](./cloud.md) starts from cloud assets, buckets, and domains and produces exposure leads. Noise: passive to active.

**API / GraphQL**
[API / GraphQL](./api-graphql.md) starts from routes, schemas, and tokens and produces endpoint/schema findings. Noise: low to active.

**Automation**
[Automation](./automation.md) starts from approved workflow inputs and produces repeatable pipeline output. Noise: varies.

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
