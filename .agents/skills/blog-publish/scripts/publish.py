#!/usr/bin/env python3
"""
publish.py — deterministic publish for blog-publish (explicit only).
Renamed from github_publish.py, now native git primary (Q-P-3).

Usage:
  python3 publish.py --post <post_path> --repo-path <content_root> [--target-account <gh_account>] [--default-branch main]

Behavior Q-P-3: native git `git -C content add -- <post> && commit && push origin main`.
No .drafts/, post lives at right place with publish:false until human flips.
Bumps `updated` to today before commit (Q-P-1). Targeted add only, not -A.
"""
import argparse, json, os, re, sys, subprocess, datetime, shutil, atexit

original_account = None

def restore_account():
    global original_account
    if original_account and shutil.which("gh"):
        try:
            subprocess.run(["gh","auth","switch","--hostname","github.com","--user", original_account], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
        except Exception:
            pass

def run(cmd, cwd=None):
    return subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, shell=False)

def main():
    global original_account
    ap = argparse.ArgumentParser(description="Native git publish for content post (explicit only).")
    ap.add_argument("--post", required=True, help="Path to post file (absolute or repo-relative)")
    ap.add_argument("--repo-path", default=".", help="Repo root (content)")
    ap.add_argument("--target-account", default="", help="Optional gh account to switch to before push")
    ap.add_argument("--default-branch", default="main")
    ap.add_argument("--commit-msg", default="", help="Override commit message (default feat(blog): add draft \"<title>\")")
    args = ap.parse_args()

    repo = os.path.abspath(args.repo_path)
    post = args.post
    # resolve post relative/absolute
    if os.path.isabs(post):
        post_abs = post
        try:
            post_rel = os.path.relpath(post_abs, repo)
        except ValueError:
            post_rel = post_abs
    else:
        post_abs = os.path.join(repo, post)
        post_rel = post

    if not os.path.isfile(post_abs):
        print(f"ERROR: post not found: {post_abs}", file=sys.stderr); sys.exit(2)
    # verify verify passed? best-effort check for latest verify report BLOCKING:false
    # not blocking publish, just warn
    # bump updated Q-P-1
    text = open(post_abs, encoding="utf-8").read()
    today = datetime.date.today().isoformat()
    if re.search(r"^updated:", text, re.MULTILINE):
        text = re.sub(r"^updated:.*$", f"updated: {today}", text, flags=re.MULTILINE)
        open(post_abs, "w", encoding="utf-8").write(text)

    # optional gh switch
    if args.target_account and shutil.which("gh"):
        atexit.register(restore_account)
        try:
            r = run(["gh","api","user","--jq",".login"])
            if r.returncode==0 and r.stdout.strip():
                original_account = r.stdout.strip().strip('"')
        except Exception:
            pass
        sw = run(["gh","auth","switch","--hostname","github.com","--user", args.target_account])
        if sw.returncode!=0:
            print(f"WARNING: could not switch to {args.target_account}: {sw.stderr}", file=sys.stderr)

    # derive title for commit msg
    m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', text, re.MULTILINE)
    title = m.group(1).strip() if m else os.path.basename(post_abs)
    commit_msg = args.commit_msg or f'feat(blog): add draft "{title}"'

    # git checks
    if run(["git","rev-parse","--is-inside-work-tree"], cwd=repo).returncode !=0:
        print(f"ERROR: not a git repo: {repo}", file=sys.stderr); sys.exit(2)
    # targeted add
    add = run(["git","add","--", post_rel], cwd=repo)
    if add.returncode!=0:
        print(f"git add failed: {add.stderr}", file=sys.stderr); sys.exit(2)
    # warn other dirty
    st = run(["git","status","--porcelain"], cwd=repo)
    if st.stdout.strip():
        # filter out the post itself
        other = "\n".join(l for l in st.stdout.splitlines() if post_rel not in l)
        if other.strip():
            print(f"WARNING: other unstaged changes remain:\n{other}", file=sys.stderr)
    # nothing to commit?
    if run(["git","diff","--cached","--quiet"], cwd=repo).returncode==0:
        print("Nothing to commit."); sys.exit(0)
    cm = run(["git","commit","-m", commit_msg], cwd=repo)
    if cm.returncode!=0:
        print(f"git commit failed: {cm.stderr}", file=sys.stderr); sys.exit(2)
    push = run(["git","push","origin", f"HEAD:{args.default_branch}"], cwd=repo)
    if push.returncode!=0:
        print(f"git push failed: {push.stderr}", file=sys.stderr); sys.exit(2)
    print(f"OK: pushed {post_rel} to {args.default_branch} (commit: {commit_msg})")
    print(f"updated: {today} | 24h Pages delay expected")

if __name__ == "__main__":
    main()
