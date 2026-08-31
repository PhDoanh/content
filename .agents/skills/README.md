# Distilled Skills — Provenance Index (v2)

Pipeline remains **vault-first, content submodule**: `personal-wiki` (read-only source) → `content` (Quartz publish). Distilled adapters are **reference-only** in `content/.agents/skills/`; `personal-wiki` remains the only vault with `.vault-meta/` and `scripts/`.

## Kepano (obsidian-skills) — 3 skills + 1 fallback

| Adapter | Source | Verbatim? | Role |
|---|---|---|---|
| `obsidian-cli/` | `kepano/obsidian-skills` `skills/obsidian-cli/SKILL.md` (106l) | Yes | Primary transport: `obsidian read/search/create/append/property:set`. Fallback filesystem `Read/Grep` when Obsidian not running (per `personal-wiki/.vault-meta/transport.json: filesystem`). |
| `obsidian-markdown/` | `kepano/.../obsidian-markdown/SKILL.md` (196l) + `references/CALLOUTS,EMBEDS,PROPERTIES.md` | Yes | Canonical `[[wikilink]]`/`![[embed]]`/`> [!type]`/YAML properties for `blog-outline`/`blog-write`. Prefer kepano over `claude-obsidian` fallback. |
| `defuddle-kepano/` | `kepano/.../defuddle/SKILL.md` (41l) | Yes | `defuddle parse <url> --md` — strip ads/nav, -40-60% tokens. Use before `WebFetch` in `blog-write`/`blog-verify`. |
| `defuddle-obsidian/` | `claude-obsidian` `skills/defuddle/SKILL.md` | Yes | Vault-ingest variant; same CLI, kept for provenance. |

**Install**: `npm install -g defuddle` (merged package; `defuddle-cli@0.7.0` deprecated). Verified `defuddle 0.1.0`.

## Claude-blog — 14 adapters + 1 shared

| Adapter | Source | Lines | Role in dual-goal pipeline |
|---|---|---|---|
| `blog-shared/` | `claude-blog` `skills/blog/references/*` (16) + `templates/*` (12) | — | Shared contracts: `quality-scoring`, `blog-delivery-contract`, `synthesis-contract`, `content-templates`, `visual-media`, `eeat-signals`, `flow-alignment`, etc. Consumed by multiple adapters via `../blog-shared/references/`. |
| `blog-analyze/` | `skills/blog-analyze/SKILL.md` | 339 | 5-category 100pt scoring (Content30/SEO25/E-E-A-T15/Technical15/AI15). Replaces `verify.py` heuristic. |
| `blog-seo-check/` | `skills/blog-seo-check/SKILL.md` | 236 | 11-step SEO validation. |
| `blog-factcheck/` | `skills/blog-factcheck/SKILL.md` | 191 | Tier T1-T5 + echo-cluster, scores 1.0/0.7/0.3/0.0. |
| `blog-geo/` | `skills/blog-geo/SKILL.md` | 311 | AI citation readiness (ChatGPT/Perplexity/Gemini...) — archive signal. |
| `blog-brief/` | `skills/blog-brief/SKILL.md` | 281 | Content brief with statistics/EE-A-T/internal architecture. Upgrades `blog-outline` from skeleton to brief-first. |
| `blog-audit/` | `skills/blog-audit/SKILL.md` | 254 | Site-wide orphan/cannibalization/stale for `content/system-foundations/**/*.md`. Monthly, not per-post. |
| `blog-style/` | `skills/blog-style/SKILL.md` | 88 | `learn <paths>` 5-10 posts → `VOICE.md` for `humanizer` calibration. |
| `blog-strategy/` | `skills/blog-strategy/SKILL.md` | 378 | Quarterly hub-and-spoke strategy for 3 cores. |
| `blog-cluster/` | `skills/blog-cluster/SKILL.md` + `references/{semantic-clustering,cluster-architecture,execution-workflow}.md` | 339 | SERP overlap ≥4/10 semantic clustering, hub-and-spoke execution (3 cores only, garden skips). |
| `blog-write-upstream/` | `skills/blog-write/SKILL.md` | 497 | Upstream verbatim (497l, 7 phases) for comparison; pipeline's `blog-write/SKILL.md` remains execution authority. |
| `blog-outline-upstream/` | `skills/blog-outline/SKILL.md` | 148 | Upstream verbatim (Steps 1-5 SERP) for comparison. |
| `blog-schema/` | `skills/blog-schema/SKILL.md` | 307 | JSON-LD Article/Person/Org/BreadcrumbList/ImageObject. |
| `blog-repurpose/` | `skills/blog-repurpose/SKILL.md` | 295 | Repurpose to X/LinkedIn/Reddit/YouTube/newsletter — post-publish marketing. |
| `blog-rewrite/` | `skills/blog-rewrite/SKILL.md` | 364 | Optimize existing posts for May 2026 Core Update + AI citation. |

Upstream preserved at `/tmp/opencode/claude-blog-main/skills/*` and `/tmp/opencode/obsidian-skills-main/skills/*` for full context.

## Personal-wiki provisioning (Aug 30)

- `wiki-retrieve`: `bash bin/setup-retrieve.sh --no-llm` → 619 chunks (434 pages), `synthetic` tier, `bm25/index.json` vocab 13959, avg_dl 804. Fallback `noop-embed-error` until `ollama nomic-embed-text` available. `retrieve.py "query" --top 5` now returns valid JSON (bm25+rerank noop). Other skills (`wiki-query`, `autoresearch`) auto-detect.
- `defuddle`: `npm i -g defuddle` (0.1.0) — `defuddle parse <url> --md` verified.

## Pipeline integration (v2 deltas)

- `blog/SKILL.md` — added `Distilled Adapters (v2)` section listing all 18 adapters.
- `blog-research/SKILL.md` — added `Distilled Transport Update` (obsidian-cli first, retrieve synthetic, defuddle before WebFetch).
- `blog-outline/SKILL.md` — added `Distilled Adapters (v2)` (templates + obsidian-markdown + defuddle).
- `blog-write/SKILL.md` — added `Distilled Adapters (v2)` (shared contracts + strategy/cluster/schema/repurpose/rewrite/style).
- `blog-verify/SKILL.md` — added `Distilled Adapters (v2)` replacing heuristic with 4 parallel claude-blog adapters.

No `.vault-meta/` was created in `content`; no files were added to `personal-wiki` beyond `chunks/` + `bm25/` (idempotent).
