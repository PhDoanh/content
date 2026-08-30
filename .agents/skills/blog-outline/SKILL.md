---
name: blog-outline
description: Creates structured outline (1500-3000w, H2/H3, FAQ for cores only) and emits post skeleton in-place at right folder. Use when user says "/blog-outline", "create outline", "plan sections".
allowed-tools: Read, Write, Glob, Grep, Bash, WebFetch
---

# blog-outline — Outline + In-Place Post Skeleton

Runs inside `content`. Emits directly to `<right-place>/<slug>.md` with `publish: false` (no separate outline artifact). Consumes `research-report-{ts}.json` from `blog-research`.

## References (verbatim reuse)

- `claude-blog` `blog-outline/SKILL.md: Step 1-5` (Step 2 SERP analyze top 5 headings/visuals/gaps + AI Overviews/PAA; Step 3 outline `# Outline: [Topic]` with Title Suggestions 40-60 chars, Target Parameters `Primary keyword, intent, ~[X,XXX] words advisory never score/gate, H2 6-8, Flesch 60-70`, each H2 `Answer-first opener + Key points + H3 + Stat + Chart + Image`, Optional FAQ 3-5, Conclusion 100-150, Internal Zones, Gaps 3-5; Guidelines: question H2 only when intent supports, section estimates advisory)
- `claude-blog` `blog-brief/SKILL.md: Step 5` (Title/Meta/TL;DR/Information Gain/Content Outline 6-8 H2s with Answer-first/Chart/Image/Key stat, Statistics table, Evidence-Backed Plan, Competitive Gaps, Internal Architecture, E-E-A-T, Distribution)
- `approved-solution.md:40` `wiki-to-brief` claim-only extract, read-only `wiki-query` + `claim-ledger` (private thoughts never verbatim, provenance required)
- `claude-blog` `content-templates.md` 12 templates (auto-detect) and `blog-brief` Template Recommendation
- `content/templates/article.md` canonical (`title {1: 50-60}, description {2: 140-160}, permalink "", lang vi, publish false, updated YYYY-MM-DD, tags, aliases, cssclasses, socialDescription {3: ~100}, socialImage ""`) + `private/ai-prompts.md` Title/Description/SocialDescription {n: order} templates

## Workflow

1. Resolve `research-report-{ts}.json` path (arg or latest `ls -t skills/blog-research/reports/research-report-*.json | head -1`).
2. Map topic to core|garden via `blog-config.json:cores/garden` Q-R-3 approved. For cores, run SERP Step 2 verbatim (WebSearch full visible surface, WebFetch top 2-3 headings only if snippets insufficient, URL hygiene `http/https` only, reject `javascript:data:file:`, DNS private-IP block, size/timeout cap, untrusted).
3. Build outline: Core `H2 6-8` (~300-400w each, 1500-3000 advisory) + `FAQ 3-5` + `Links 5-10` distributed; Garden `H2 4-6`, `FAQ 0`, `Links 2-3` (Q-O-1/Q-O-2 approved). Choose template (12 types) but adapt to `templates/article.md` structure, not claude-blog's MDX hero pipeline.
4. Decide target folder per `AGENTS.md` mapping (Fullstack→`system-foundations|best-practices`, AI-Driven→`ai-orchestration`, Automation→`automation`, Garden→`beyond-code/*`). Slug auto ≤4 words, kebab-case from title (`slugify(title)[:4w]`, resolve collision `-${n}`).
5. Write post skeleton: frontmatter with `title, description, permalink: "", lang: vi, publish: false, updated: today, tags: [core tag + level Beginner|Intermediate|Advanced|Expert + GenAI Q-P-2 always], aliases: [], cssclasses: [], socialDescription, socialImage: ""` (Q-O-3 respect templates). Body = outline sections with `Answer-first opener` placeholders + `Key points` bullets + H3 stubs + `Key statistic to find` + `Chart suggestion` markers (but `write.skip_chart: true`, so markers are advisory only) + `Image placement` markers + `Conclusion` + `Internal Linking Zones` + `Content Gaps to Exploit`. Use Obsidian syntax (`[[wikilink]]`, callouts, `%% media type %%`).
6. Ensure `publish: false` trusted, no `.drafts/`, no `quartz sync`.

## Output

- Artifact: `<right-place>/<slug>.md` (post file is the artifact; lives in git, published later only via `blog-publish`). No separate `outlines/*.md`.
- Session: print outline preview + post path. Next: `blog-write` edits same file in-place.

## Safety

Never write to `personal-wiki`. Reports pruned via `research-report` dir; post file stays.
