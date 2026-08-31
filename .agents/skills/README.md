# Distilled Skills — Provenance Index (v2.1)

Pipeline remains **vault-first, content submodule**: `personal-wiki` (read-only source) → `content` (Quartz publish). Distilled adapters are **reference-only** in `content/.agents/skills/`; `personal-wiki` remains the only vault with `.vault-meta/` and `scripts/`. Vault read: **filesystem only** via `Read/Grep/Glob` on `$WIKI_PATH/wiki/**/*.md` (no `obsidian-cli`).

## Kepano (obsidian-skills) — 2 skills

| Adapter | Source | Verbatim? | Role |
|---|---|---|---|
| `obsidian-markdown/` | `kepano/obsidian-skills` `skills/obsidian-markdown/SKILL.md` (196l) + `references/CALLOUTS,EMBEDS,PROPERTIES.md` | Yes | Canonical `[[wikilink]]`/`![[embed]]`/`> [!type]`/YAML properties for `blog-outline`/`blog-write`. |
| `defuddle/` | `kepano/.../defuddle/SKILL.md` (41l) | Yes | `defuddle parse <url> --md` — strip ads/nav, -40-60% tokens. Use before `WebFetch` in `blog-write`/`blog-verify`. |

**Install**: `npm install -g defuddle` (merged package; `defuddle-cli@0.7.0` deprecated). Verified `defuddle 0.1.0`. `obsidian-cli` removed — filesystem is the only transport.

## Claude-blog — 12 adapters + 1 shared (upstream merged)

| Adapter | Source | Lines | Role in dual-goal pipeline |
|---|---|---|---|
| `blog-shared/` | `claude-blog` `skills/blog/references/*` (16) + `templates/*` (12) | — | Shared contracts: `quality-scoring`, `blog-delivery-contract`, `synthesis-contract`, `content-templates`, `visual-media`, `eeat-signals`, `flow-alignment`, etc. Consumed via `../blog-shared/references/`. |
| `blog-analyze/` | `skills/blog-analyze/SKILL.md` | 339 | 5-category 100pt scoring (Content30/SEO25/E-E-A-T15/Technical15/AI15). Replaces `verify.py` heuristic. |
| `blog-seo-check/` | `skills/blog-seo-check/SKILL.md` | 236 | 11-step SEO validation. |
| `blog-factcheck/` | `skills/blog-factcheck/SKILL.md` | 191 | Tier T1-T5 + echo-cluster, scores 1.0/0.7/0.3/0.0. |
| `blog-geo/` | `skills/blog-geo/SKILL.md` | 311 | AI citation readiness (ChatGPT/Perplexity/Gemini...). |
| `blog-brief/` | `skills/blog-brief/SKILL.md` | 281 | Content brief with statistics/EE-A-T/internal architecture. |
| `blog-audit/` | `skills/blog-audit/SKILL.md` | 254 | Site-wide orphan/cannibalization/stale for `content/system-foundations/**/*.md`. Monthly, not per-post. |
| `blog-style/` | `skills/blog-style/SKILL.md` | 88 | `learn <paths>` 5-10 posts → `VOICE.md` for `humanizer` calibration. |
| `blog-strategy/` | `skills/blog-strategy/SKILL.md` | 378 | Quarterly hub-and-spoke strategy for 3 cores. |
| `blog-cluster/` | `skills/blog-cluster/SKILL.md` + `references/{semantic-clustering,cluster-architecture,execution-workflow}.md` | 339 | SERP overlap ≥4/10 semantic clustering, hub-and-spoke execution (3 cores only, garden skips). |
| `blog-schema/` | `skills/blog-schema/SKILL.md` | 307 | JSON-LD Article/Person/Org/BreadcrumbList/ImageObject. |
| `blog-repurpose/` | `skills/blog-repurpose/SKILL.md` | 295 | Repurpose to X/LinkedIn/Reddit/YouTube/newsletter — post-publish marketing. |
| `blog-rewrite/` | `skills/blog-rewrite/SKILL.md` | 364 | Optimize existing posts for May 2026 Core Update + AI citation. |

`blog-outline` and `blog-write` upstream verbatim merged into custom skills (`blog-outline/SKILL.md` now includes SERP Step 1-5 detail; `blog-write/SKILL.md` now includes Phase 0-7). Upstream folders `blog-outline-upstream`/`blog-write-upstream` removed. Originals preserved at `/tmp/opencode/...` for reference.

## Personal-wiki provisioning (Aug 30)

- `wiki-retrieve`: `bash bin/setup-retrieve.sh --no-llm` → 619 chunks (434 pages), `synthetic` tier, `bm25/index.json` vocab 13959, avg_dl 804. `retrieve.py "query" --top 5` returns valid JSON (bm25+rerank noop). Auto-detected by `wiki-query`/`autoresearch`.
- `defuddle`: `npm i -g defuddle` (0.1.0) — `defuddle parse <url> --md` verified.

## Pipeline integration (v2.1 deltas)

- **Defuddle:** `defuddle-kepano` renamed to `defuddle`; `defuddle-obsidian` and `obsidian-cli` removed. Vault read is filesystem-only.
- **Custom skills rewritten to Anthropic standard:** `blog`, `blog-research`, `blog-outline` (merged 148l upstream), `blog-write` (merged 497l upstream Phases 0-7), `blog-verify`, `blog-publish` — each now has `version/author/license/allowed-tools` frontmatter + `When to Use` + abstract deterministic invocation spec (call subagent, compat any executor).
- **Artifacts:** `scan_candidates.py` (FRONTMATTER_RE hardened `\s*`), `cluster_graph.py` (wiki-retrieve fallback note), `write_report.py` (prune by `mtime`), `finalize_outline.py` (threshold annotation); `blog-verify/scripts/verify.py` removed (replaced by `blog-analyze/seo-check/factcheck/geo` subagents).
- **Config:** `blog-config.json:write.lang_char_ratio_warn_threshold: 0.3` added.

No `.vault-meta/` was created in `content`; no files were added to `personal-wiki` beyond `chunks/` + `bm25/` (idempotent).
