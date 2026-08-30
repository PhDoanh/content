# AGENTS.md — content vault (blog)

This vault is the **public, marketing-first** side of the blog. All pipeline stages run **inside this vault** (`cwd = content`). The private vault `personal-wiki` is never mutated from here.

## Durable facts

- **3 core SEO pillars** (source: `index.md`): `Fullstack Development` | `Automation` | `AI-Driven Development`. Sub-clusters map Q-R-3: `AI-Driven → ai-orchestration (+ agentic-workflows)`, `Fullstack → system-foundations + best-practices`, `Automation → automation` (or `best-practices/automation` if no top-level folder), `Beyond Code → beyond-code/*` = digital garden (no SEO gates).
- **Private vault absolute path**: `WIKI_PATH=/mnt/d/phdoanh/personal-wiki`. Always resolve `wiki-query` with `--vault "$WIKI_PATH"` (explicit). Never infer from plugin directory or `cwd`.
- **One-way data flow**: `personal-wiki (wiki/)` → read-only `wiki-query`/`wiki-retrieve` + `claim-ledger` → `<right-place>/<slug>.md` with `publish: false` → `blog-verify` → explicit `blog-publish` only. Never write to `personal-wiki` from `content` context.
- **Language**: Always `vi` by default; preserve English technical terms inline. Only `en`/`ja` when explicitly requested.
- **Template**: `templates/article.md` is canonical (`title 50-60, description 140-160, socialDescription ~100, permalink "", lang vi, publish false, updated YYYY-MM-DD, tags, aliases, cssclasses, socialImage`). Slug ≤4 words, kebab-case, auto from title. `permalink` manual (empty until publish). `GenAI` + level tags (`Beginner|Intermediate|Advanced|Expert` in `tags/*.md`) are injected at outline stage.
- **Config**: `blog-config.json` at vault root (centralized, no hard-code).

## Agent Skills (all under `.agents/skills/` — neutral path for OpenCode + Antigravity)

- `/blog` orchestrator — research→outline→write(+humanizer)→verify, **pause before publish** (user must run `/blog-publish` explicitly)
- `/blog-research` — vault-first collection (`whole wiki/`), SERP via `blog-cluster` only for 3 cores
- `/blog-outline` — 1500-3000w outline; FAQ 3-5 + 5-10 links only for cores; garden muted
- `/blog-write` — draft in-place, answer-first, evidence-backed, Flesch 60-70, H1→H2→H3, auto `humanizer`
- `/blog-verify` — 5-gate lite (≥90 + zero P0 blocking) → `reports/verify-report-{ts}.md`
- `/blog-publish` — native git publish (explicit only), bumps `updated`
- `/humanizer` — separate, de-slops 29 patterns; auto-called by `blog-write`

## Conventions

- No `.drafts/` folder. Drafts live directly at right place (`content/<sub>/<slug>.md`) with `publish: false` until verified.
- Reports under `skills/*/reports/` are **gitignored**, keep 3 then prune.
- Never `quartz sync` from here (`content` is git repo/submodule of `PhDoanh/blog`).
- `private/*` is gitignored; approved solution + drafts stay there.
