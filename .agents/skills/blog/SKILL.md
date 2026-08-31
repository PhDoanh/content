---
name: blog
description: Orchestrates the full blog pipeline research → outline → write (+humanizer) → verify, pausing before publish. Use when user says "/blog", "run full blog pipeline", "produce post end-to-end".
---

# blog — Full Pipeline Orchestrator

Runs inside `content` vault (`cwd = content`). All stages are read-only vs `personal-wiki` except `blog-outline`/`blog-write` which write the in-place post.

## References (verbatim reuse)

- `claude-obsidian` `wiki-query/SKILL.md: Retrieve` (`wiki/hot.md` → `wiki-retrieve` BM25 contextual if `python3 "$RETRIEVE" --vault "$VAULT" --verify` verified, else `wiki/index.md` + text search) + `Assess evidence` (claim-ledger `accepted/provisional/contested/unsupported`)
- `claude-obsidian` `autoresearch/SKILL.md:94` Topic Selection A/B/C
- `claude-blog` `skills/blog-write/SKILL.md: Phase 0-7` and `blog-delivery-contract.md` 5 gates (here lite: gate 4 ≥90 + zero P0 only)
- `blog-config.json` at vault root

## Workflow

1. **blog-research** — `Task` `blog-research` with topic. If label `chưa chín` → HARD-BOUND stop, print reason. Else proceed.
2. **blog-outline** — `Task` `blog-outline` with `research-report-{ts}.json` → emits `<right-place>/<slug>.md` (`publish: false`, `permalink: ""`). No separate outline artifact.
3. **blog-write** — `Task` `blog-write` consumes same post path, drafts answer-first, evidence-backed, `vi` default, `humanizer` auto-applied (direct, no diff). 1500-3000w, H1→H2→H3, skip chart.
4. **blog-verify** — `Task` `blog-verify` → `skills/blog-verify/reports/verify-report-{ts}.md`. If `BLOCKING: true` (<90 or P0) → feed report to `blog-write` next iteration (max 3). On `BLOCKING: false` → **pause**.
5. **Never call `blog-publish`** — user must run `/blog-publish <post>` explicitly (`publish.explicit_only: true`).

## Artifacts

This skill emits **no separate artifact**; stage artifacts are the pipeline artifacts (research json, post md, verify report). Session report summarizes each stage.

## Report

Print pipeline summary: topic, core/garden label, post path, verify BLOCKING, next step (`/blog-publish <path>` or fix loop).

## Distilled Adapters (v2 — local verbatim)

- `obsidian-cli` (kepano): `../obsidian-cli/SKILL.md` — primary transport `obsidian read/search`, fallback filesystem `Read/Grep` per `personal-wiki/.vault-meta/transport.json`
- `obsidian-markdown` (kepano): `../obsidian-markdown/SKILL.md` + `references/{CALLOUTS,EMBEDS,PROPERTIES}.md` — canonical wikilink/callout/embed syntax for `blog-outline`/`blog-write` outputs
- `defuddle` (kepano+obsidian): `../defuddle-kepano/SKILL.md` (kepano wrapper) + `../defuddle-obsidian/SKILL.md` (claude-obsidian) — both wrap `defuddle-cli`; use `defuddle parse <url> --md` before `WebFetch` to save 40-60% tokens
- `wiki-retrieve` provisioned in `personal-wiki` via `bash bin/setup-retrieve.sh --no-llm` (619 chunks, tier synthetic) — `blog-research` should call `python3 $WIKI_PATH/scripts/retrieve.py "<query>" --top 5` before fallback to `hot.md→index.md`
- `claude-blog` shared: `../blog-shared/references/{quality-scoring,synthesis-contract,blog-delivery-contract,content-templates,visual-media,eeat-signals,flow-alignment,internal-linking,research-quality}.md` + `templates/{12 types}.md`
- `blog-analyze/seo-check/factcheck/geo` (claude-blog): replace `verify.py` heuristic with 5-category 100pt + 11-step SEO + tier T1-T5 fact-check + AI citation readiness
- `blog-brief/strategy/cluster/schema/repurpose/rewrite/style/audit` — see respective `ADAPTER.md` for upstream source and role

