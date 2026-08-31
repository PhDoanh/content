# AGENTS.md

Content vault for `PhDoanh/blog` (Quartz). Git submodule `PhDoanh/content` (`main`). Push to `main` triggers `.github/workflows/dispatch-blog.yml` → `repository_dispatch` to `PhDoanh/blog`.

## Vault

- `cwd` is vault root per `blog-config.json: vault.content_path="."` (`/mnt/d/phdoanh/blog/content`).
- Source knowledge base is **read-only** `personal-wiki`: `$WIKI_PATH` or default `/mnt/d/phdoanh/personal-wiki`. Never `Write` to it. Vault read is **filesystem only** via `Read/Grep/Glob` on `$WIKI_PATH/wiki/**/*.md` (no `obsidian-cli`).
- `wiki-retrieve` provisioned in `personal-wiki` (`bash bin/setup-retrieve.sh --no-llm` → 619 chunks synthetic, `bm25/index.json` vocab 13959). Prefer `python3 "$WIKI_PATH/scripts/retrieve.py" --top 5` before fallback `wiki/hot.md → index.md`.
- Web cleaning: `defuddle` (`npm i -g defuddle`, 0.1.0) — `defuddle parse <url> --md` before any `WebFetch` (saves 40-60% tokens).

## Pipeline — 5+1 Skills in `.agents/skills/` (Anthropic `version: 2.1.0`)

Orchestrator `blog` runs `research → outline → write (+humanizer) → verify` and **pauses** — never auto-calls `blog-publish` (`publish.explicit_only: true`).

| Skill | Input → Output | Key constraint |
|-------|---------------|----------------|
| `blog-research` | `scan_candidates.py` + `cluster_graph.py` → `reports/research-report-{ts}.json` (keep 3, prune by `mtime`) | Vault-first, filesystem only. Garden skips SERP. |
| `blog-outline` | `research-report.json` → `<right-place>/<slug>.md` (`publish: false`) | In-place only (no separate outline). SERP only for 3 cores. Slug ≤4 words kebab-case, collision `-${n}`. Core H2 6–8 + FAQ 3–5; Garden H2 4–6 + FAQ 0 |
| `blog-write` | outline post → same file full draft | Merged upstream Phases 0-7; `skip_chart: true` (no SVG). `humanizer` 29 patterns auto-applied after `blog-style` voice calibration |
| `blog-verify` | post → `reports/verify-report-{ts}.md` (keep 3) `BLOCKING: true/false` last line | Delegates via subagent to `blog-analyze` + `blog-seo-check` + `blog-factcheck` + `blog-geo` in parallel; `verify.py` heuristic removed. Lite: `Gating ≥90 + zero P0` |
| `blog-publish` | Only skill that mutates git | Explicit only. Bump `updated` to today, `git add -- <post>` targeted → `commit` → `push origin main`. Never `git add -A` |

Distilled non-custom skills (reference-only, compat any executor via abstract `call subagent`): `defuddle/`, `obsidian-markdown/`, `blog-shared/` (16 references + 12 templates), `blog-analyze|seo-check|factcheck|geo|brief|audit|style|strategy|cluster|schema|repurpose|rewrite` — see `.agents/skills/README.md` for provenance.

## Config Source of Truth

`blog-config.json` v2 — thresholds live here, not in prose:

- **Cores→folder:** Fullstack→`system-foundations|best-practices`, Automation→`automation|best-practices/automation`, AI-Driven→`ai-orchestration|ai-orchestration/agentic-workflows`, Garden→`beyond-code/*`
- **Taxonomy:** always add `GenAI` + one level `Beginner|Intermediate|Advanced|Expert` (publish gates)
- **Research:** `min_wikilinks 2, min_cluster_notes 3, min_cluster_words 800`, block `news/changelog/wip/todo/draft`
- **Outline:** `1500–3000w`, `per_h2 300–400w`, `internal_links 5–10 core / 2–3 garden`
- **Verify:** `score_threshold 90`, `require_zero_p0 true`, `lite true` (muted `hero/pdf/visual`)
- **Write:** `skip_chart true`, `flesch 60–70`, `H1→H2→H3 no skip`, `lang_char_ratio_warn_threshold 0.3`

## Frontmatter & Conventions

Template `templates/article.md`: `title (50–60), description (140–160), permalink "", lang vi, publish false, updated YYYY-MM-DD, tags, aliases, cssclasses, socialDescription (~100), socialImage ""`.

- `contribution.md` mandatory: H2 start (no H1 in body), evergreen, `#GenAI` for AI-assisted, hide drafts with `%% %%` or `<!-- -->`. Language default `vi` (preserve English terms).
- Reports under `.agents/skills/*/reports/` are `.gitignore`'d. No build/lint/test in this vault.

## Git & Publish Gotchas

- Verify worktree: `git -C . rev-parse --is-inside-work-tree` (submodule).
- Publish: `git add -- "<post>" && git commit -m 'feat(blog): add draft "<title>"' && git push origin HEAD:main` — warn if other dirty files remain.
- After push, 24h delay before Pages reflects change (dispatch to `PhDoanh/blog` must succeed; check Actions).

## References

- `blog-config.json` — pipeline thresholds & folder mapping
- `.agents/skills/README.md` — distilled adapter provenance
- `.agents/skills/*/SKILL.md` (v2.1.0, `allowed-tools` frontmatter) — authoritative workflow; call subagent abstract, not executor-specific
- `contribution.md` — writing rules & display-bug workarounds
