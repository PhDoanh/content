# AGENTS.md

Content vault for `PhDoanh/blog` (Quartz). Git submodule `PhDoanh/content` (`main`). Push to `main` triggers `.github/workflows/dispatch-blog.yml` → `repository_dispatch` to `PhDoanh/blog`.

## Vault

- `cwd` is vault root per `blog-config.json: vault.content_path="."` (`/mnt/d/phdoanh/blog/content`).
- Source knowledge base is **read-only** `personal-wiki`: `$WIKI_PATH` or default `/mnt/d/phdoanh/personal-wiki`. Never `Write` to it. Vault read is **filesystem only** via `Read/Grep/Glob` on `$WIKI_PATH/wiki/**/*.md` (no `obsidian-cli`).
- `wiki-retrieve` provisioned in `personal-wiki` (`bash bin/setup-retrieve.sh --no-llm` → 619 chunks synthetic, `bm25/index.json` vocab 13959). Prefer `python3 "$WIKI_PATH/scripts/retrieve.py" --top 5` before fallback `wiki/hot.md → index.md`.
- Web cleaning: `defuddle` (`npm i -g defuddle`, 0.1.0) — `defuddle parse <url> --md` before any `WebFetch` (saves 40-60% tokens).

## Pipeline — 5+1 Skills in `.agents/skills/` (Anthropic `version: 2.3.0`)

Orchestrator `blog` runs `research → outline → write (+humanizer) → verify` and **pauses** — never auto-calls `blog-publish` (`publish.explicit_only: true`).

| Skill | Input → Output | Key constraint |
|-------|---------------|----------------|
| `blog-research` | `scan_candidates.py` + `cluster_graph.py` → `reports/research-report-{ts}.json` (keep 3, prune by `mtime`) | Vault-first, filesystem only. Garden skips SERP. Experience sufficiency gate (pauses for author input if <2 experience notes). Distillation tagging (`PUBLIC`, `NEEDS_DISTILLATION`, `INTERNAL_ONLY`). |
| `blog-outline` | `research-report.json` → `<right-place>/<slug>.md` (`publish: false`) | In-place only. Outline frontmatter restricted: `title`, `description`, `lang: vi`, `publish: false`, `tags` (3-5 specialized topic tags + `GenAI` + Level), `socialDescription`. `permalink: ""` empty, `updated` omitted. Slug ≤4 words kebab-case. H2 headings end with emojis. Video suggestions commented out. Deterministic budget validation via `text_length.py`. |
| `blog-write` | outline post → same file full draft | Bumps `updated: today`. Persona voice (storytelling, Feynman, "Tôi", H2 emojis, 2-4 sentences/para). Narrative grounded in authentic author experiences (no generic dev war stories). Distills internal context (zero leaked codenames like F2T, LOOP, QualityEvaluator). Zero dead links (must resolve to `publish: true` in `content/`). Videos commented out. Deterministic word count ≤3000w. |
| `blog-verify` | post → `reports/verify-report-{ts}.md` (keep 3) `BLOCKING: true/false` last line | Fast deterministic P0 check (`verify_post.py`: P0-WC, P0-FM, P0-DEADLINK, P0-IFRAME, P0-EMOJI, P0-LEAK, P0-EDT, P0-CALLOUT, P0-CHARSET, P0-EVERGREEN) + parallel subagents (`blog-analyze` + `blog-seo-check` + `blog-factcheck` + `blog-geo`). `Gating ≥90 + zero P0`. |
| `blog-publish` | Only skill that mutates git | Explicit only. Sets `publish: true`, targeted `git add -- <post>` → `commit` → `push origin main`. Never `git add -A`. |

Distilled non-custom skills (reference-only, compat any executor via abstract `call subagent`): `defuddle/`, `obsidian-markdown/`, `blog-shared/` (16 references + 12 templates + deterministic scripts), `blog-analyze|seo-check|factcheck|geo|brief|audit|style|strategy|cluster|schema|repurpose|rewrite` — see `.agents/skills/README.md` for provenance.

## Config Source of Truth

`blog-config.json` v2 — thresholds live here, not in prose:

- **Cores→folder:** Fullstack→`system-foundations|best-practices`, Automation→`automation|best-practices/automation`, AI-Driven→`ai-orchestration|ai-orchestration/agentic-workflows`, Garden→`beyond-code/*`
- **Taxonomy:** always add `GenAI` + one level `Beginner|Intermediate|Advanced|Expert` + 3-5 specialized topic tags. Core folder names (`fullstack`, `system-foundations`, etc.) are prohibited in tags.
- **Research:** `min_wikilinks 2, min_cluster_notes 3, min_cluster_words 800`, block `news/changelog/wip/todo/draft`, experience sufficiency check
- **Outline:** `1500–3000w`, `per_h2 300–400w`, `internal_links 5–10 core / 2–3 garden`, deterministic `text_length.py` validation
- **Verify:** `score_threshold 90`, `require_zero_p0 true`, fast deterministic `verify_post.py`
- **Write:** `skip_chart true`, `flesch 60–70`, `H1→H2→H3 no skip`, `lang_char_ratio_warn_threshold 0.3`, hard limit 3000w

## Frontmatter & Conventions

Template `templates/article.md`: `title (50–60), description (140–160), permalink "", lang vi, publish false, updated YYYY-MM-DD, tags, aliases, cssclasses, socialDescription (~100), socialImage ""`.

- Stage permissions: Outline fills `title, description, lang, publish: false, tags, socialDescription`. Write sets `updated: today`. Publish sets `publish: true`. `permalink` remains manual/empty until publish.
- `contribution.md` mandatory: H2 start (no H1 in body), evergreen, `#GenAI` for AI-assisted, emoji on every H2 heading, hide drafts/editorial with `%% %%` or `<!-- -->`. Language default `vi` (preserve English terms).
- Reports under `.agents/skills/*/reports/` are `.gitignore`'d. Deterministic checks under `.agents/skills/blog-shared/scripts/`.

## Git & Publish Gotchas

- Verify worktree: `git -C . rev-parse --is-inside-work-tree` (submodule).
- Publish: `git add -- "<post>" && git commit -m 'feat(blog): add draft "<title>"' && git push origin HEAD:main` — warn if other dirty files remain.
- After push, 24h delay before Pages reflects change (dispatch to `PhDoanh/blog` must succeed; check Actions).

## References

- `blog-config.json` — pipeline thresholds & folder mapping
- `.agents/skills/README.md` — distilled adapter provenance
- `.agents/skills/*/SKILL.md` (v2.1.0, `allowed-tools` frontmatter) — authoritative workflow; call subagent abstract, not executor-specific
- `contribution.md` — writing rules & display-bug workarounds
