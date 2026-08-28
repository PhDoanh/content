---
title: "Git Foundations & Modern Workflows: Internals to Stacked PRs"
description: "A practical synthesis of Git's three-tree model, objects, branching and remotes, plus modern workflows: Conventional Commits, GitHub Flow, Spec-Driven Development and Stacked PRs for reviewable delivery."
permalink: "git-foundations-modern-workflows-internals-to-stacked-prs"
lang: en
publish: false
updated: 2026-08-28
tags:
  - system-foundations
  - git
  - github-flow
  - conventional-commits
aliases:
  - git-foundations-modern-workflows
cssclasses:
socialDescription: "From Git's objects and three states to GitHub Flow, Conventional Commits, SDD and Stacked PRs — a reviewable delivery system."
socialImage: ""
---

- git
- system-foundations
- github-flow
- conventional-commits
- spec-driven-development
- stacked-prs

# Git Foundations & Modern Workflows: From Internals to Stacked Pull Requests

Git looks simple — `add`, `commit`, `push` — until you need to undo, rebase, or land a large feature without blocking review. This article synthesizes twelve evergreen notes on Git's internals and the workflows built on top of them: the three-tree model and object store, references and branching, merge vs. rebase, reset and recovery, remotes, plus Conventional Commits, GitHub Flow, Spec-Driven Development (SDD) and Stacked PRs.

> Sources: `ACID` is unrelated; this draft draws on `Git Three States`, `Git Objects`, `Git References`, `Git Branching`, `Git Merge and Rebase`, `Git Reset Demystified`, `Git Undo Operations`, `Git Working with Remotes`, `Conventional Commits`, `GitHub Flow`, `Spec-Driven Development (SDD)`, `Stacked Pull Requests`.

## 1. The Three Trees and Three States

Every file lives in one of three states — **modified**, **staged**, **committed** — backed by three trees:

| Tree | Location | Role |
|------|----------|------|
| `HEAD` | `.git/HEAD` → branch ref → commit | Last snapshot |
| Index | `.git/index` | Proposed next commit |
| Working directory | Files on disk | Your edits |

Lifecycle: `Untracked --(add)--> Staged --(commit)--> Committed --(edit)--> Modified`.

Useful diffs target different pairs:

```bash
git diff              # working tree vs index
git diff --staged     # index vs HEAD
```

This model makes `reset` predictable. `reset` moves the branch ref, then optionally resets `index` and `working directory` in order:

| Mode | HEAD | Index | Workdir |
|------|------|-------|---------|
| `--soft` | move | — | — |
| `--mixed` (default) | move | reset | — |
| `--hard` | move | reset | reset |

`git reset HEAD~1 --soft` undoes a commit but keeps changes staged; `git reset HEAD~1 --hard` discards them. With a path, `git reset HEAD <file>` unstages that file (modern equivalent: `git restore --staged <file>`).

> Takeaway: If you pick the wrong flag, `git reflog` still knows where you were — see §4.

## 2. Objects, References, Branches

Git is a content-addressable filesystem. Every object is `SHA-1("type size\0content")`:

- **Blob** — raw file content, no path. Same content → same hash, even across files.
- **Tree** — directory: `name → (mode, object ID)` mapping to blobs or other trees. Paths live here, not in blobs.
- **Commit** — points to one root tree, zero or more parents, plus author/committer metadata.

Branches and tags are just **references** — pointers to a commit:

- Branch (`refs/heads/main`) moves with each commit on that branch.
- Tag (`refs/tags/v1.2.0`) — lightweight or annotated — stays fixed.
- `HEAD` is `ref: refs/heads/<branch>` or a detached commit.

`Git References` and `Git Branching` emphasize that branches are cheap (a 41-byte file). Create them liberally, delete after merge — the PR preserves history.

## 3. Branching, Merge vs. Rebase, Remotes

**Branching** isolates work. **Merge** preserves history with a merge commit; **rebase** rewrites it into a linear sequence. Choose by team convention, then enforce with branch protection:

- Require pull request, 1–2 approvals, `dismiss stale approvals`, `require status checks`, `require branches up to date`, `require linear history` for squash/rebase teams.
- `CODEOWNERS` (`*.js @frontend-team`) auto-assigns reviewers.

**Working with remotes** is `fetch` + `merge` (or `pull`). Track upstream:

```bash
git switch -c feat/auth
git push -u origin feat/auth
git fetch origin
git rebase origin/main
```

For large features, a single long-lived branch stalls review. Use a **stack** instead.

## 4. Undo Without Panic

Common undo operations, ordered by blast radius:

```bash
# Undo last commit but keep changes staged
git reset --soft HEAD~1

# Unstage a file
git restore --staged README.md  # or git reset HEAD README.md

# Discard working-tree changes to a file
git restore README.md           # or git checkout HEAD -- README.md

# Amend last commit (message or forgotten file)
git commit --amend

# Revert a pushed commit (safe, creates new commit)
git revert <sha>

# Recover a lost commit/branch
git reflog  # HEAD history, not commit history
git switch -c rescue <sha-from-reflog>
```

`reflog` records every `HEAD` move for ~90 days — your safety net after a bad `reset --hard`.

## 5. Conventional Commits — Commits as a Protocol

Structure turns `git log` into data:

```
<type>(<scope>): <description>

[optional body]

[optional footer(s)]
```

`feat(api): add /users endpoint` → SemVer `MINOR`; `fix(parser): handle null` → `PATCH`; `feat(api)!:` or `BREAKING CHANGE:` in footer → `MAJOR`. Types `docs/style/refactor/test/chore/perf` do not bump but keep history searchable.

Tooling closes the loop: `commitlint` validates messages, `semantic-release`/`release-please` bump versions and publish, `standard-version` generates changelogs. Teams that adopt the spec get automated releases without manual versioning debates.

## 6. GitHub Flow — The Six Steps

A lightweight, branch-based flow built for continuous delivery:

1. **Create branch** — short, descriptive (`add-code-of-conduct`).
2. **Commit** — clear messages; one branch per unrelated change.
3. **Open PR** — use draft PRs for early feedback.
4. **Review** — line-level comments, additional pushes.
5. **Merge** — squash, rebase, or merge commit per team rule.
6. **Delete branch** — history lives in the PR.

Keep PRs under ~400 changed lines (large PRs are rubber-stamped) and respond within 24 hours — review latency predicts velocity more than any other metric. `Closes #123` keywords link PRs to issues automatically.

## 7. Spec-Driven Development — What to Build, In Order

GitHub Flow answers *how to deliver*; SDD answers *what to build* via a spec chain (spec-kit slash commands):

```
/speckit.specify  →  /speckit.plan  →  /speckit.tasks  →  /speckit.implement
      spec.md           plan.md          tasks.md          code
```

- Artifacts live in `specs/<nnn>-<slug>/` (`spec.md`, `plan.md`, `tasks.md`, `contracts/`).
- `/speckit.specify` creates `feat/xxx-feature` from the base branch.
- Tasks carry domain prefixes (`AUTHZ`, `FOUND`) for traceability.
- Human **review gates** sit between phases — the spec is approved before it drives code, preventing an agent from optimizing into unwanted behavior.

SDD's sub-issue branches feed directly into the next workflow.

## 8. Stacked Pull Requests — Parallel, Reviewable Delivery

When a feature splits into dependent slices (`A1 → E1 → B3 → B4`), a single branch blocks testing. A **stack** makes each slice independently reviewable:

```bash
git switch feat-base && git pull
git switch -c feat-a1   # push A1
git switch -c feat-e1   # from feat-a1, push E1 (depends on A1)
git switch -c feat-b3   # from feat-e1
```

Open one PR per slice, basing each PR on its direct dependency so reviewers see only that slice's diff:

| PR | Source | Base | Reviewer sees |
|----|--------|------|---------------|
| A1 | `feat-a1` | `feat-base` | only A1 |
| E1 | `feat-e1` | `feat-a1` | only E1 |
| B3 | `feat-b3` | `feat-e1` | only B3 |

The top branch contains the whole stack and runs integration tests before anything merges. Merge **bottom-up** (A1 → E1 → B3 → B4), retargeting bases as lower PRs land. Do not stack independent changes — branch them directly off `feat-base`.

### Putting It Together

```
spec → plan → tasks → (stacked branches/PRs) → GitHub Flow merges → Conventional Commits drive SemVer releases
```

Fundamentals (trees/objects/references) explain *why* reset and branching behave that way; workflows make that behavior scale. The combination is an evergreen delivery system: small, reversible commits, spec-first scope, and parallel review without waiting for dependencies to land on `main`.
