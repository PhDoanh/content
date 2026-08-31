---
name: blog-research
description: Collects ideas, keywords and references from personal-wiki (whole wiki/ primary, vault-first) via filesystem scan + wiki-retrieve. Use when user says "/blog-research", "research wiki for post", "collect ideas and references".
version: 2.1.0
author: PhDoanh
license: MIT
allowed-tools: Read, Grep, Glob, Bash, Task
---

# blog-research — Vault-First Research

Runs inside `content` vault. Primary source is `personal-wiki` whole `wiki/` (read-only). Vault read via filesystem directly.

## When to Use

- First stage of pipeline or standalone research for a topic
- Needs deterministic cluster + keyword + reference output for `blog-outline`

## References

- **Filesystem scan** — `Bash: python3 .agents/skills/blog-research/scripts/scan_candidates.py --vault "$WIKI_PATH"` (reads `blog-config.json:research`, scans `wiki/` via `Glob`, parses frontmatter, filters `transient_tag_blocklist` + `maturity_levels_eligible` + `min_wikilinks`, extracts `blog_refs` markers).
- **Cluster graph** — `Bash: python3 .agents/skills/blog-research/scripts/cluster_graph.py --config blog-config.json` (undirected `related:` graph, connected components, `min_cluster_notes/words` gate, taxonomy majority vote, note with LLM decision prompt).
- **Retrieval (preferred)** — call subagent with `wiki-retrieve` if `python3 "$WIKI_PATH/scripts/retrieve.py" --top 5` succeeds — uses `defuddle` cleaning + BM25 before fallback to `wiki/hot.md → wiki/index.md + text search`. If `retrieve.py` exits 10, fallback to legacy hot→index→drill.
- **Evidence assessment** — `Read: wiki/meta/ledgers/claim-ledger.json + source-ledger.json` if present (`accepted` needs fresh non-synthetic source, high-risk needs two independent, label `provisional/contested/unsupported`). Source: `../blog-shared/references/synthesis-contract.md: 6 LAWs` + `research-quality.md`.
- **SERP (cores only, optional)** — call subagent with `../blog-cluster/SKILL.md: Step 1-3` (SERP overlap ≥4/10 = same intent, intent classification, hub-and-spoke) + `../blog-shared/references/flow-alignment.md` — only for 3 cores (Fullstack/Automation/AI-Driven), merge signal into report without writing cluster files. Garden skips SERP.
- **Web cleaning** — `../defuddle/SKILL.md: Usage --md` (`defuddle parse <url> --md`) before any `WebFetch` to strip ads/nav, save 40-60% tokens.
- **Thresholds** — `blog-config.json:research` (`min_wikilinks 2, min_cluster_notes 3, min_cluster_words 800, transient_blocklist [news,changelog,wip,todo,draft]`).

## Workflow

1. Resolve vault: `VAULT="${WIKI_PATH:-/mnt/d/phdoanh/personal-wiki}"`.
2. Deterministic filters — call subagent via Bash: `python3 .agents/skills/blog-research/scripts/scan_candidates.py --vault "$VAULT"` → pipe to `python3 .agents/skills/blog-research/scripts/cluster_graph.py --config blog-config.json` (undirected `related:` graph, connected components, `min_cluster_notes/words` gate).
3. Deep evidence read — for top candidate cluster, prefer `wiki-retrieve` (`python3 "$WIKI_PATH/scripts/retrieve.py" "$QUERY" --top 5 --no-rerank --explain` if verified) else `Read: wiki/hot.md → wiki/index.md` → candidate pages + `claim-ledger.json` + depth-2 wikilinks via filesystem `Grep`.
4. If topic is within 3 cores (Fullstack/Automation/AI-Driven), optionally call subagent with `blog-cluster plan <seed>` as library to expand SERP keywords (do not write cluster files; merge SERP overlap signal into report only).
5. Decide label `marketing-first (core name)` | `digital-garden` | `chưa chín`, with reason (gate failures, ledger status, SERP overlap).
6. Write `reports/research-report-{YYYYMMDD-HHmmss}.json` via `Bash: python3 .agents/skills/blog-research/scripts/write_report.py --config blog-config.json` (keep 3 then prune oldest) with fields `topic, timestamp, label, core, cluster_notes[{path,title,word_count,tags,status}], keywords[primary+secondary], references[{claim, source, url, tier, ledger_status}]`. Print human summary in session (no separate human file).
7. Garden branch: omit SERP keyword block.

## Output

- **Artifact:** `reports/research-report-{ts}.json` (machine, keep 3). Human summary is session-only.
- **Next:** `blog-outline` consumes the `research-report-{ts}.json` path.

## Safety

- Vault is read-only: never `Write` to `$VAULT`. All writes stay inside `content/.agents/skills/blog-research/reports/`. Prune `ls -t reports/research-report-*.json | tail -n +4 | xargs rm -f`.
- Vault read: filesystem via `Read/Grep/Glob` directly on `$WIKI_PATH/wiki/**/*.md`.
