---
title: "ffuf"
summary: "Field notes for vhost, directory, and parameter fuzzing with ffuf."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - ffuf
  - fuzzing
related:
  - ../../01-reconnaissance/virtual-host-discovery.md
references:
  - "https://www.acceis.fr/ffuf-advanced-tricks/"
---
# ffuf

## Vhost Example

```bash
ffuf -c -u http://example.com -H "Host: FUZZ.example.com" -w /path/to/wordlist -fs <baseline_size>
```

## Output That Matters

- unique status/size/word count,
- redirects to named apps,
- auth prompts,
- non-default titles.

## Risk

Fuzzing can be noisy. Start with targeted wordlists and low concurrency.
