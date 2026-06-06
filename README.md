<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&height=220&color=0:0f172a,45:7c3aed,100:06b6d4&text=Xetta's%20Web%20Application%20Hacking%20Vault&fontColor=ffffff&fontSize=34&fontAlignY=38&desc=Resources%20first.%20Payloads,%20tools,%20writeups,%20labs,%20bug%20classes,%20and%20source-traceable%20data.&descAlignY=58&descSize=14" alt="Xetta's Web Application Hacking Vault" />
</p>

<p align="center">
  <a href="resources/README.md"><img alt="Resources" src="https://img.shields.io/badge/resources-topic%20sorted-7c3aed?style=for-the-badge"></a>
  <a href="payloads/README.md"><img alt="Payloads" src="https://img.shields.io/badge/payloads-ready%20to%20browse-06b6d4?style=for-the-badge"></a>
  <a href="tools/README.md"><img alt="Tools" src="https://img.shields.io/badge/tools-recon%20burp%20fuzzing-22c55e?style=for-the-badge"></a>
  <a href="data/resources.csv"><img alt="Resource database" src="https://img.shields.io/badge/database-540%20records-f97316?style=for-the-badge"></a>
</p>

<p align="center">
  <img alt="Source URLs" src="https://img.shields.io/badge/source%20URLs-407-111827?style=flat-square">
  <img alt="Extracted snippets" src="https://img.shields.io/badge/extracted%20snippets-128-111827?style=flat-square">
  <img alt="Source notes" src="https://img.shields.io/badge/source%20notes-66-111827?style=flat-square">
  <img alt="Preserved assets" src="https://img.shields.io/badge/preserved%20assets-3-111827?style=flat-square">
</p>

<br>

## What This Is

**Xetta's Web Application Hacking Vault** is a resource-first Web AppSec library rebuilt from the original ZIP source.

It is designed for fast browsing, not slow reading. Open a section, grab the resource category you need, and move.

The vault contains links, tools, payload references, dorks, command snippets, Burp workflows, writeups, GitBooks, labs, bug-class indexes, report helpers, and a source-traceable CSV/JSON database.

## Start Here

<div align="center">

<a href="resources/README.md"><img width="31%" src="https://dummyimage.com/520x170/111827/ffffff&text=Browse+Resources" alt="Browse Resources"></a>
<a href="awesome-lists/top-25-web-appsec-links.md"><img width="31%" src="https://dummyimage.com/520x170/312e81/ffffff&text=Top+25+Links" alt="Top 25 Links"></a>
<a href="payloads/README.md"><img width="31%" src="https://dummyimage.com/520x170/155e75/ffffff&text=Payloads+%26+Wordlists" alt="Payloads and Wordlists"></a>

<br><br>

<a href="tools/README.md"><img width="31%" src="https://dummyimage.com/520x170/166534/ffffff&text=Tools+%26+Automation" alt="Tools and Automation"></a>
<a href="bug-classes/README.md"><img width="31%" src="https://dummyimage.com/520x170/7f1d1d/ffffff&text=Bug+Classes" alt="Bug Classes"></a>
<a href="maps/README.md"><img width="31%" src="https://dummyimage.com/520x170/4c1d95/ffffff&text=Learning+Maps" alt="Learning Maps"></a>

</div>

## The Vault Layout

### Resources

The main library lives in [resources/](resources/README.md).

- [Recon and OSINT](resources/recon-and-osint.md)
- [Payloads, Cheat Sheets, and Wordlists](resources/payloads-cheat-sheets-and-wordlists.md)
- [Bug Bounty Writeups, Blogs, and GitBooks](resources/bug-bounty-writeups-blogs-and-gitbooks.md)
- [Burp Suite and Tooling](resources/burp-suite-and-tooling.md)
- [API, Auth, OAuth, and GraphQL](resources/api-auth-oauth-and-graphql.md)
- [XSS and Client-Side](resources/xss-and-client-side.md)
- [SQL Injection](resources/sql-injection.md)
- [SSRF](resources/ssrf.md)
- [XXE, LFI, and File Read](resources/xxe-lfi-and-file-read.md)
- [File Upload and Parser Abuse](resources/file-upload-and-parser-abuse.md)
- [Cloud and Infrastructure](resources/cloud-and-infrastructure.md)
- [WAF, CORS, CSRF, and Smuggling](resources/waf-cors-csrf-smuggling.md)
- [RCE, CVEs, and 0days](resources/rce-cves-and-0days.md)
- [Training, Labs, Videos, OSCP, AD, and Red Team](resources/training-labs-videos-oscp-ad-and-red-team.md)

### Curated Best-Of

Use [awesome-lists/](awesome-lists/README.md) when you do not want the full dump.

- [Top 25 Web AppSec Links](awesome-lists/top-25-web-appsec-links.md)
- [Best Recon Resources](awesome-lists/best-recon-resources.md)
- [Best Bug Bounty Writeups](awesome-lists/best-bug-bounty-writeups.md)
- [Best Cheat Sheets](awesome-lists/best-cheat-sheets.md)
- [Best Burp Extensions](awesome-lists/best-burp-extensions.md)
- [Best Payload Repositories](awesome-lists/best-payload-repositories.md)
- [Hidden Gems](awesome-lists/hidden-gems.md)

### Practical Sections

- [payloads/](payloads/README.md) for XSS, SQLi, SSRF, LFI, upload bypass, WAF bypass, request smuggling, and wordlists.
- [tools/](tools/README.md) for recon, content discovery, JavaScript analysis, Burp extensions, fuzzing, OOB, cloud, API/GraphQL, and automation.
- [bug-classes/](bug-classes/README.md) for access control, auth, API, client-side, cloud, parser bugs, injection, and server-side classes.
- [playbooks/](playbooks/README.md) for recon-to-first-bug, black-box assessment, API assessment, cloud exposure review, source-assisted review, and reporting.
- [labs/](labs/README.md) for videos, OSCP, Active Directory, practice platforms, and mindmaps.
- [reports/](reports/README.md) for evidence, severity, remediation language, and report templates.

## Database Backbone

The pretty pages are not the source of truth. The data is.

- [data/resources.csv](data/resources.csv) contains every deduplicated resource and snippet.
- [data/resource_occurrences.csv](data/resource_occurrences.csv) tracks exact source occurrences.
- [data/source_documents.csv](data/source_documents.csv) maps all raw Markdown files.
- [data/resources.json](data/resources.json) provides a machine-readable export.
- [data/link-status.csv](data/link-status.csv) keeps generated link records inspectable.

This means the vault can be searched, filtered, regenerated, or re-themed without losing provenance.

## Add A Resource

Good resources are welcome.

Open a resource request here:

[New resource request](https://github.com/4riful/xetta-web-appsec-field-manual/issues/new?template=resource-request.yml)

Or submit a pull request using the repository template:

[Open a pull request](https://github.com/4riful/xetta-web-appsec-field-manual/compare)

Useful additions include tools, payload lists, writeups, GitBooks, labs, checklists, cheat sheets, bug-class references, and command snippets.

## Star History

<p align="center">
  <a href="https://star-history.com/#4riful/xetta-web-appsec-field-manual&Date">
    <img src="https://api.star-history.com/svg?repos=4riful/xetta-web-appsec-field-manual&type=Date" alt="Star History Chart">
  </a>
</p>

## Source Traceability

The original ZIP/Notion export is preserved for audit and recovery under `provenance/raw-archive/notion-export/`.

Most users should not browse the raw archive. Use the vault sections above first. Use [provenance/](provenance/README.md) only when you want to verify where a resource came from.
