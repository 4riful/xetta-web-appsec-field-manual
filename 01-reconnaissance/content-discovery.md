---
title: "Content Discovery"
summary: "Low-noise directory and file discovery after live host validation."
status: "reviewed"
last_reviewed: "2026-06-06"
tags:
  - recon
  - content-discovery
  - dirsearch
related:
  - http-service-discovery.md
  - recon-triage.md
source_provenance:
  - "source-archive/notion-export/Private & Shared/XettaтАЩs Web AppSEC Notes/Tips From EMAD Shanab df876bcc54004ddebf09e7543a538d60.md"
references: []
---
# Content Discovery

## When To Use

Run content discovery after you have verified a host is in scope and alive. Use it to discover admin panels, config files, backups, API docs, upload handlers, and hidden routes.

## Safer Dirsearch Pattern

```bash
while read -r host; do
  dirsearch -u "$host" \
    -w /path/to/wordlist \
    -e conf,config,bak,backup,old,db,sql,js,json,xml,zip,txt \
    -i 200,301,302,401,403 \
    -x 400,404,429,500 \
    -t 25
done < hosts-http.txt
```

## Crawling Through Burp

```bash
gospider -S urls-archive.txt -a -w --sitemap -r -c 10 -d 3 -p http://127.0.0.1:8080
```

## Review Checklist

- Admin panels.
- Swagger/OpenAPI docs.
- Upload endpoints.
- Backup files.
- Source maps.
- Logs and debug output.
- Old API versions.

## Safety

Avoid high thread counts by default. The raw source had aggressive examples; this manual uses safer defaults and expects you to increase only with permission.
