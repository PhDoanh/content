---
name: blog-research
description: Collects ideas, keywords and references from personal-wiki (whole wiki/ primary, vault-first) via wiki-query, SERP via blog-cluster only for 3 cores. Use when user says "/blog-research", "research wiki for post", "collect ideas and references".
---

# blog-research — Vault-First Research

Runs inside `content` vault. Primary source is `personal-wiki` whole `wiki/`.

## References (verbatim reuse)

- `claude-obsidian` `wiki-query/SKILL.md: Select depth` Quick/Standard/Deep, `Retrieve` (check `python3 "$CORE" contracts --vault "$VAULT" --verify --capability wiki-retrieve` then `python3 "$RETRIEVE" --vault "$VAULT" "$QUERY" --top 5 --no-rerank --explain`, fallback to `wiki/index.md` + sub-indexes + text search), `Assess evidence` (read `wiki/meta/ledgers/claim-ledger.json` + `source-ledger.json`, `accepted` needs fresh non-synthetic source, high-risk needs two independent, `provisional/contested/unsupported` labeled)
- `claude-obsidian` `wiki-ingest/SKILL.md: Analyze before drafting` (SHA-256, `.raw/.manifest.json`), `wiki-retrieve/SKILL.md` (contextual/BM25/cosine)
- `claude-obsidian` `autoresearch/SKILL.md: Round 1-3` (decompose 3-5 angles, 2-3 WebSearch per angle, fetch top 2-3, gap fill max 5) — NOT used here except as budget reference; this skill stays wiki-only
- `claude-blog` `blog-cluster/SKILL.md: Step 1-3` SERP overlap ≥4/10 = same intent, intent classification, `hub-and-spoke` only for 3 cores (`blog-cluster plan <seed>`)
- `personal-wiki .vault-meta/blog-config.json` legacy thresholds `min_wikilinks 2, min_cluster_notes 3, min_cluster_words 800, transient_blocklist [news,changelog,wip,todo,draft]` — now in `content/blog-config.json:research`

## Workflow

1. Resolve vault: `VAULT="${WIKI_PATH:-/mnt/d/phdoanh/personal-wiki}"`.
2. Reuse deterministic filters: `python3 .agents/skills/blog-research/scripts/scan_candidates.py --vault "$VAULT"` → `python3 .agents/skills/blog-research/scripts/cluster_graph.py --config blog-config.json` (undirected `related:` graph, connected components, `min_cluster_notes/words` gate).
3. Deep evidence read: for top candidate cluster, run `wiki-query` Deep semantics (read `wiki/hot.md` → `wiki-retrieve` if verified else `wiki/index.md` → candidate pages + `claim-ledger.json` + depth-2 wikilinks).
4. If topic is within 3 cores (Fullstack/Automation/AI-Driven), optionally run `blog-cluster plan <seed>` as library to expand SERP keywords, but **do not** write cluster files; merge SERP overlap signal into report only.
5. Decide label `marketing-first (core name)` | `digital-garden` | `chưa chín`, with reason.
6. Write `reports/research-report-{YYYYMMDD-HHmmss}.json` (keep 3 then prune, oldest deleted) with fields `topic, timestamp, label, core, cluster_notes[ {path,title,word_count,tags,status} ], keywords[primary+secondary], references[ {claim, source, url, tier, ledger_status} ], research_report json`; also print human summary in session (no separate human file).
7. Garden branch: omit SERP keyword block.

## Output

- Artifact: `skills/blog-research/reports/research-report-{ts}.json` (machine). Human summary is session-only.
- Next: `blog-outline` consumes the `research-report-{ts}.json` path.

## Distilled Transport Update (v2)

- Preferred vault read: try `obsidian-cli` first (`obsidian vault="personal-wiki" search/query/read` per `../obsidian-cli/SKILL.md`), fallback to filesystem `Read/Grep` if Obsidian not running (per `personal-wiki/.vault-meta/transport.json: filesystem`).
- Preferred retrieval: try `python3 "$WIKI_PATH/scripts/retrieve.py" "$QUERY" --top 5` (wiki-retrieve synthetic, 619 chunks provisioned Aug 30) before legacy `hot.md→index.md`. If `retrieve.py` exits 10 or chunks missing, fallback.
- Preferred web cleaning: `defuddle parse <url> --md` via `../defuddle-kepano/SKILL.md` (or `../defuddle-obsidian/SKILL.md`) before `WebFetch` to strip ads/nav.

## Safety

Vault is read-only: never `Write` to `$VAULT`. All writes stay inside `content/.agents/skills/blog-research/reports/`. Prune `ls -t reports/research-report-*.json | tail -n +4 | xargs rm -f`.
