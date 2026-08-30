---
name: blog-publish
description: Publishes approved post via native git (commit + push) to content:main, bumps updated, explicit only. Use when user says "/blog-publish", "publish post", "send live".
---

# blog-publish — Native Git Publish (Explicit Only)

Runs inside `content` repo/submodule `PhDoanh/content`. Only skill allowed to mutate git. Explicit-only per `blog-config.json:publish.explicit_only: true` (even `/blog` orchestrator never calls this).

## References (verbatim reuse)

- `personal-wiki/skills/blog/scripts/github_publish.py:29-120`
- `claude-blog` `blog-write` Phase 7 Delivery (present only after gate 4 pass) and `blog-delivery-contract.md` iteration loop max 3
- `blog-config.json:publish` (explicit_only, bump_updated, commit_message_template `feat(blog): add draft "{title}"`, default_branch `main`, method `native_git`)

## Workflow

1. Resolve post path arg (must be `content/<folder>/<slug>.md` with `verify` passed `BLOCKING:false`). Reject if `publish: true` already or verify missing; ask user to run `/blog-verify`.
2. Read frontmatter `title`; set `updated` to today `YYYY-MM-DD` via targeted edit; ensure `permalink: ""` stays manual, `lang: vi`, `publish` to `true`.
3. Native git: verify `content` is git repo (`git -C . rev-parse --is-inside-work-tree`), `git status` clean except post; `git add -- "<post>"` (targeted, warn if other unstaged remain — not staged); `git commit -m "feat(blog): add draft \"<title>\""`; `git push origin main` (or `HEAD:main` if detached).
4. On push success, session report with commit SHA, push status, permalink, next `24h` Pages delay note. On failure, keep file local, report for manual `git push` sync.

## Output

- No artifact file; session report is the record (commit SHA + push status). Post file remains in git.

## Safety

Never `git add -A`; always targeted add via post path. Mutate only post file; do not alter `AGENTS.md`/`blog-config.json`/`private/*`. Verify post passed `blog-verify` before publishing.
