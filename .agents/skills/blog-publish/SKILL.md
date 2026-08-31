---
name: blog-publish
description: Publishes approved post via native git (commit + push) to content:main, bumps updated, explicit only. Use when user says "/blog-publish", "publish post", "send live".
version: 2.1.0
author: PhDoanh
license: MIT
allowed-tools: Read, Bash, Edit
---

# blog-publish — Native Git Publish (Explicit Only)

Runs inside `content` repo/submodule `PhDoanh/content`. Only skill allowed to mutate git. Explicit-only per `blog-config.json:publish.explicit_only:true` (even `blog` orchestrator never calls this).

## When to Use

- After `blog-verify` returned `BLOCKING: false` for the post
- User explicitly invokes with post path

## References

- `blog-config.json:publish` (`explicit_only, bump_updated, commit_message_template 'feat(blog): add draft "{title}"', default_branch main, method native_git`)
- `../blog-shared/references/blog-delivery-contract.md: Gate 4` (present only after gate 4 pass, iteration loop max 3)

## Workflow

1. Resolve post path arg (must be `content/<folder>/<slug>.md` with `verify` passed `BLOCKING:false`). Reject if `publish: true` already or verify missing; ask user to run `blog-verify`.
2. Read frontmatter `title`; set `updated` to today `YYYY-MM-DD` via targeted `Edit`; ensure `permalink: ""` stays manual, `lang: vi`, `publish` to `true`.
3. Native git — `Bash: git -C . rev-parse --is-inside-work-tree` (verify), `git status --porcelain` (warn if other dirty files remain — never `git add -A`), `git add -- "<post>"` (targeted), `git commit -m 'feat(blog): add draft "<title>"'` (escape `"` in title), `git push origin main` (or `HEAD:main` if detached).
4. On push success, session report with commit SHA, push status, permalink, next `24h` Pages delay note (via `PhDoanh/blog` dispatch). On failure, keep file local, report for manual `git push` sync.

## Output

- No artifact file; session report is the record (commit SHA + push status). Post file remains in git.

## Safety

- Never `git add -A`; always targeted add via post path. Mutate only post file; do not alter `AGENTS.md`/`blog-config.json`/`private/*`. Verify post passed `blog-verify` before publishing.
