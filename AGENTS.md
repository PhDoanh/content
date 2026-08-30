# AGENTS.md

Content vault for `PhDoanh/blog` (Quartz). This repo is a **git submodule** (`PhDoanh/content`, branch `main`). Push to `main` fires `.github/workflows/dispatch-blog.yml` → `repository_dispatch` to `PhDoanh/blog`.

## Vault Root & External Dependency

- `cwd` is vault root: `/mnt/d/phdoanh/blog/content` (see `blog-config.json: vault.content_path: "."`).
- Primary knowledge base is **read-only** `personal-wiki`: `$WIKI_PATH` or default `/mnt/d/phdoanh/personal-wiki`. Never `Write` to it.

## Pipeline — 5 Skills in `.agents/skills/`

Orchestrator `blog` runs `research → outline → write (+humanizer) → verify` and **pauses** — never auto-calls `blog-publish` (`publish.explicit_only: true`).

| Skill | What it does | Key constraint |
|-------|--------------|----------------|
| `blog-research` | Vault-first: scans `$WIKI_PATH/wiki/` via `scan_candidates.py` + `cluster_graph.py`, wiki-query Deep, optional `blog-cluster plan` for 3 cores only | Wiki-only — no web search here. Artifact: `.agents/skills/blog-research/reports/research-report-{ts}.json` (keep 3) |
| `blog-outline` | Consumes research report, SERP for cores, writes **in-place** post `<right-place>/<slug>.md` with `publish: false` | No separate outline file. Slug ≤4 words kebab-case, collision `-${n}`. Core H2 6–8 + FAQ 3–5, Garden H2 4–6 + FAQ 0 |
| `blog-write` | Expands outline → full draft in-place, web stats/images/YouTube now, auto humanizer (29 patterns), Flesch 60–70, H1→H2→H3 | `write.skip_chart: true`. Keep `publish: false` |
| `blog-verify` | Lite 5-gate: only `content_review` (≥90 + zero P0 blocking) + `link_integrity` active; `hero/pdf/visual` muted | `BLOCKING: true/false` last line. Loop max 3 via `blog-write`. Artifact: `.agents/skills/blog-verify/reports/verify-report-{ts}.md` (keep 3) |
| `blog-publish` | Only skill that mutates git. Bumps `updated` to today, targeted `git add -- <post>` → `commit` → `push origin main` | Explicit only — user runs `/blog-publish <post>` after `BLOCKING:false`. Never `git add -A` |

## Config Source of Truth

`blog-config.json` (version 2) — all thresholds live here, not in prose:

- **Cores** (`cores`/`garden`): `Fullstack→system-foundations|best-practices`, `AI-Driven→ai-orchestration|ai-orchestration/agentic-workflows`, `Automation→automation|best-practices/automation`, Garden→`beyond-code/*`
- **Taxonomy**: always add `GenAI` + one level tag `Beginner|Intermediate|Advanced|Expert` (tags are publish gates)
- **Research**: `min_wikilinks 2, min_cluster_notes 3, min_cluster_words 800`, block `news/changelog/wip/todo/draft`
- **Outline**: `1500–3000w`, `per_h2 300–400w`, `internal_links 5–10 core / 2–3 garden`
- **Verify**: `score_threshold 90`, `require_zero_p0 true`, `lite true`
- **Publish**: `commit_message_template: 'feat(blog): add draft "{title}"'`, `method: native_git`, `default_branch: main`

## Frontmatter & Conventions

Template `templates/article.md`:

- `contribution.md` mandatory: H1→H2→H3 no skip, evergreen, `#GenAI` for AI-assisted, hide drafts with `%% %%` or `<!-- -->`.
- Language default `vi` (preserve English terms). No build/lint/test to run — this is a markdown vault.
- Reports as artifact under `.agents/skills/*/reports/` or `skills/*/reports/` are `.gitignore`'d.

## Git & Publish Gotchas

- Verify inside worktree: `git -C . rev-parse --is-inside-work-tree`.
- Add, commit, and push: `git add -- "<post>" && git commit -m 'feat(blog): add draft "<title>"' && git push origin HEAD:main` - warn if other dirty files remain.
- After push, 24h delay before Pages reflects change (via `PhDoanh/blog` dispatch).

## References to Keep

- `blog-config.json` — pipeline thresholds & folder mapping
- `.agents/skills/*/SKILL.md` — authoritative workflow per stage
- `contribution.md` — writing rules & display-bug workarounds
