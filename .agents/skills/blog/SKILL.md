---
name: blog
description: Orchestrates full pipeline research → outline → write (+humanizer) → verify, pausing before publish. Use when user says "/blog", "run full blog pipeline", "produce post end-to-end".
version: 2.3.0
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
- **Deterministic verification** — `python3 .agents/skills/blog-shared/scripts/verify_post.py --post <post> --content-root .` (checks word count, frontmatter, dead links, iframes, emojis, context leaks, charsets).
- **Syntax & egress** — `../obsidian-markdown/SKILL.md` for `[[wikilink]]`/`![[embed]]`/callouts; `../defuddle/SKILL.md` before any `WebFetch`; `../blog-shared/templates/*.md` (12 types) for template selection.
- **Config** — `blog-config.json` at vault root (single source of truth for thresholds).

## Workflow

1. **blog-research** — call subagent with `blog-research` and topic.
   - If result label `chưa chín` or `nội dung thời sự` → HARD-BOUND stop, print reason.
   - If `experience_status: INSUFFICIENT` → **PAUSE** and present questionnaire to the author. Collect real experience input before passing enriched research report to `blog-outline`.
   - Distillation tags applied: `PUBLIC`, `NEEDS_DISTILLATION`, `INTERNAL_ONLY`.
2. **blog-outline** — call subagent with `blog-outline` and `research-report-{ts}.json` path.
   - Strictly enforces outline frontmatter: only `title`, `description`, `lang: vi`, `publish: false`, `tags` (3-5 specialized tags + `GenAI` + Level), `socialDescription`.
   - `permalink` remains empty `""`, `updated` is omitted until `blog-write`.
   - Deterministic word budget check: if budget > 3000w → pause and present atomization split to user.
   - Skeleton pre-formats H2 headings with emojis and video suggestions as HTML comments.
3. **blog-write** — call subagent with `blog-write` and post path.
   - Bumps `updated: today`. Keeps `publish: false` and `permalink: ""`.
   - Narrative flow strictly uses author experiences from research report (never fabricates generic developer war stories).
   - Distills internal context into universal lessons (no leaked internal codenames like F2T, LOOP, QualityEvaluator).
   - Prevents dead links: only link to existing published posts (`publish: true` in `content/`).
   - Video suggestions formatted as HTML comments (`<!-- Video suggestion: ... -->`).
   - Mandatory emoji at end of every H2 heading.
   - Hard limit 3000w (deterministic check).
4. **blog-verify** — call subagent with `blog-verify` and post path → `reports/verify-report-{ts}.md`.
   - Runs fast deterministic P0 check (`verify_post.py`) + subagents (`blog-analyze`, `blog-seo-check`, `blog-factcheck`, `blog-geo`).
   - P0 gates: P0-WC, P0-FM, P0-DEADLINK, P0-IFRAME, P0-EMOJI, P0-LEAK, P0-EDT, P0-CALLOUT, P0-CHARSET, P0-EVERGREEN.
   - If `BLOCKING: true` → feed report to `blog-write` next iteration (max 3).
   - On `BLOCKING: false` → **pause**.
5. **Never call `blog-publish`** — user must run `blog-publish` explicitly with post path after `BLOCKING:false`.

## Artifacts

This skill emits **no separate artifact**; stage artifacts are the pipeline artifacts (research json, post md, verify report). Session report summarizes each stage.

## Output

Print pipeline summary: `topic, core/garden label, post path, verify BLOCKING, next step (/blog-publish <path> or fix loop)`.

## Safety

- Vault is read-only vs `personal-wiki`; never `Write` to `$WIKI_PATH`.
- Explicit-only publish: even orchestrator never mutates git.
- Do NOT read `contribution.md` for pipeline rules — it is for human contributors only.
