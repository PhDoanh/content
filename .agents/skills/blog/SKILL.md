---
name: blog
description: Orchestrates full pipeline research → outline → write (+humanizer) → verify, pausing before publish. Use when user says "/blog", "run full blog pipeline", "produce post end-to-end".
version: 2.2.0
author: PhDoanh
license: MIT
allowed-tools: Read, Bash, Task
---

# blog — Full Pipeline Orchestrator

Runs inside `content` vault (`cwd = content`). All stages are read-only vs `personal-wiki` except `blog-outline`/`blog-write` which write the in-place post.

## When to Use

- User provides topic and wants end-to-end draft (`/blog <topic>`)
- Manual invocation of full pipeline with human-in-the-loop pauses

## References

- **Vault read** — filesystem via `Read/Grep/Glob` directly on `$WIKI_PATH/wiki/**/*.md`.
- **Retrieval** — call subagent with `wiki-retrieve` if `python3 "$WIKI_PATH/scripts/retrieve.py" --vault "$WIKI_PATH" --verify` succeeds; fallback to `wiki/hot.md → wiki/index.md + text search`. Evidence assessment via `../blog-shared/references/synthesis-contract.md: 6 LAWs` + `claim-ledger` if present.
- **Synthesis & quality** — `../blog-shared/references/{quality-scoring.md: 100pt, blog-delivery-contract.md: Gate 4 (≥90 AND zero P0 → BLOCKING true/false, max 3 iterations), synthesis-contract.md, flow-alignment.md}`.
- **Pipeline stages** — call subagent for each: `blog-research` → `blog-outline` → `blog-write` → `blog-verify`. Never call `blog-publish` (explicit-only per `blog-config.json: publish.explicit_only:true`).
- **Syntax & egress** — `../obsidian-markdown/SKILL.md` for `[[wikilink]]`/`![[embed]]`/callouts; `../defuddle/SKILL.md` before any `WebFetch`; `../blog-shared/templates/*.md` (12 types) for template selection.
- **Config** — `blog-config.json` at vault root (single source of truth for thresholds).

## Workflow

1. **blog-research** — call subagent with `blog-research` and topic. If result label `chưa chín` or `nội dung thời sự` → HARD-BOUND stop, print reason. Else proceed.
2. **blog-outline** — call subagent with `blog-outline` and `research-report-{ts}.json` path. **Note:** `blog-outline` will run evergreen validation and word count estimation first. If the topic requires atomization (estimated > 3000w), `blog-outline` will pause to present the split. Orchestrator waits for the confirmed single-article scope before continuing.
3. **blog-write** — call subagent with `blog-write` and post path; drafts answer-first, evidence-backed, `vi` default, humanizer + persona calibration auto-applied. Hard limit 3000w. Editorial sections removed or commented. Callout titles Vietnamese. Charset normalized.
4. **blog-verify** — call subagent with `blog-verify` and post path → `reports/verify-report-{ts}.md`. New P0 gates checked: word count (P0-WC), visible editorial (P0-EDT), mixed callout language (P0-CALLOUT), non-basic charset (P0-CHARSET), non-evergreen framing (P0-EVERGREEN). If `BLOCKING: true` → feed report to `blog-write` next iteration (max 3). On `BLOCKING: false` → **pause**.
5. **Never call `blog-publish`** — user must run `blog-publish` explicitly with post path after `BLOCKING:false`.

## Artifacts

This skill emits **no separate artifact**; stage artifacts are the pipeline artifacts (research json, post md, verify report). Session report summarizes each stage.

## Output

Print pipeline summary: `topic, core/garden label, post path, verify BLOCKING, next step (/blog-publish <path> or fix loop)`.

## Safety

- Vault is read-only vs `personal-wiki`; never `Write` to `$WIKI_PATH`.
- Explicit-only publish: even orchestrator never mutates git.
- Do NOT read `contribution.md` for pipeline rules — it is for human contributors only.
