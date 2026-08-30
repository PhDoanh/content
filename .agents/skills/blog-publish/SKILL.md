---
name: blog-publish
description: Publishes approved post via native git (commit + push) to content:main, bumps updated, explicit only. Use when user says "/blog-publish", "publish post", "send live".
allowed-tools: Read, Bash, Grep
---

# blog-publish — Native Git Publish (Explicit Only)

Runs inside `content` repo/submodule `PhDoanh/content`. Only skill allowed to mutate git. Explicit-only per `blog-config.json:publish.explicit_only: true` (even `/blog` orchestrator never calls this).

## References (verbatim reuse)

- `personal-wiki/skills/blog/scripts/github_publish.py:29-120` (deterministic native path: `gh auth switch` + `atexit restore`, `git add -- <draft>` targeted, `--draft-path` required, fallback `FALLBACK_TO_MCP` → removed per Q-P-3 native git)
- `claude-blog` `blog-write` Phase 7 Delivery (present only after gate 4 pass) and `blog-delivery-contract.md` iteration loop max 3
- `blog-config.json:publish` (explicit_only, bump_updated, commit_message_template `feat(blog): add draft "{title}"`, default_branch `main`, method `native_git`)

## Workflow

1. Resolve post path arg (must be `content/<folder>/<slug>.md` with `verify` passed `BLOCKING:false`). Reject if `publish: true` already or verify missing; ask user to run `/blog-verify`.
2. Read frontmatter `title`; set `updated` to today `YYYY-MM-DD` (Q-P-1 yes) via targeted edit; ensure `permalink: ""` stays manual, `lang: vi`, `publish` stays `false` until human flips in CMS (or via this skill only if explicitly asked to publish `publish: true`).
3. Native git: verify `content` is git repo (`git -C . rev-parse --is-inside-work-tree`), `git status` clean except post; `git add -- "<post>"` (targeted, warn if other unstaged remain — not staged); `git commit -m "feat(blog): add draft \"<title>\""`; `git push origin main` (or `HEAD:main` if detached). If `GH_BLOG_ACCOUNT` set, optional `gh auth switch` before push and restore after, but native git method is primary per Q-P-3.
4. On push success, session report with commit SHA, push status, permalink, next `24h` Pages delay note. On failure, keep file local, report for manual `git push` sync; no MCP fallback per Q-P-3.
5. No separate publish artifact; report is session-only (mirrors git log). Pruning not needed.

## Output

- No artifact file; session report is the record (commit SHA + push status). Post file remains in git.
- Next: CMS `Ready` workflow or direct Pages 24h.

## Safety

Never `git add -A`; always targeted add via post path. Mutate only post file; do not alter `AGENTS.md`/`blog-config.json`/`private/*`. Verify post passed `blog-verify` before publishing.
