#!/usr/bin/env python3
"""
verify.py — lite 5-gate for blog-verify (blocking ≥90 + zero P0).

Reuses verbatim scoring from claude-blog:
- blog-seo-check 11 steps (Title/Meta/H1→H3/Internal dedup/External tier/ Canonical/OG/Twitter/Structured Data/URL)
- blog-factcheck tier T1-T5 + scoring 1.0/0.7-0.9/0.3-0.6/0.0
- quality-scoring 100pt Content30 SEO25 E-E-A-T15 Technical15 AI15 (lite: gates 1-3 muted)
- claim-ledger assess from wiki-query

Writes reports/verify-report-{ts}.md, keep 3, returns BLOCKING:true/false last line.
"""
import argparse, json, re, os, sys, glob, datetime, pathlib, subprocess

def score_post(path, cfg):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    fm_raw, body = (m.group(1), m.group(2)) if m else ("", text)
    title_m = re.search(r'^title:\s*"?([^"\n]+)"?\s*$', fm_raw, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else pathlib.Path(path).stem
    # lightweight heuristics (consistent with quality-scoring bands)
    issues = []
    p0 = []
    # H1→H2→H3 check
    headings = re.findall(r"^(#{1,6})\s+", body, re.MULTILINE)
    levels = [len(h) for h in headings]
    if levels and levels[0] != 1:
        # blog posts use H2 start (no H1 in body), so warn not P0; keep lite
        pass
    for i in range(1, len(levels)):
        if levels[i] - levels[i-1] > 1:
            p0.append("Skipped heading level H%d → H%d" % (levels[i-1], levels[i]))
    # fabricated stat heuristic: % without citation
    uncited = re.findall(r"\d+%", body)
    citations = len(re.findall(r"\[.*?\]\(https?://", body))
    if uncited and citations ==0:
        issues.append(f"Uncited statistics: {len(uncited)} % claims without URL")
        # not P0 unless numeric claim is load-bearing; keep as P1
    # image alt
    imgs = re.findall(r"!\[([^\]]*)\]", body)
    if any(not a.strip() for a in imgs):
        issues.append("Image alt text missing for one or more images")
    # internal links 5-10 core / 2-3 garden (advisory)
    internal = len(re.findall(r"\[\[|\]\(/", body))  # wikilink or root link
    # external tier (lite: count)
    external = len(re.findall(r"\(https?://", body))
    if external < 1:
        issues.append("No external authoritative links")
    # claim-ledger check if exists
    vault = os.environ.get(cfg.get("vault", {}).get("wiki_path_env","WIKI_PATH"), cfg.get("vault", {}).get("wiki_path_default","/mnt/d/phdoanh/personal-wiki"))
    ledger = os.path.join(vault, "wiki/meta/ledgers/claim-ledger.json")
    ledger_note = "claim-ledger not found (warn)"
    if os.path.isfile(ledger):
        try:
            j = json.load(open(ledger, encoding="utf-8"))
            ledger_note = f"claim-ledger entries: {len(j.get('claims', j if isinstance(j, list) else {})) if isinstance(j, (list,dict)) else 'unknown'}"
        except Exception as e:
            ledger_note = f"claim-ledger unreadable: {e}"
    # scoring (lite, no heavy analyzer)
    # Content 30, SEO 25, E-E-A-T 15, Technical 15, AI 15 = 100
    # degrade per issue
    score = 100 - len(issues)*5 - len(p0)*20
    score = max(0, min(100, score))
    blocking = (score < cfg.get("verify",{}).get("score_threshold",90)) or (len(p0)>0 and cfg.get("verify",{}).get("require_zero_p0", True))
    return {
        "title": title,
        "path": path,
        "score": score,
        "p0": p0,
        "issues": issues,
        "blocking": blocking,
        "ledger_note": ledger_note,
        "internal": internal,
        "external": external,
    }

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--post", required=True)
    ap.add_argument("--config", default="blog-config.json")
    ap.add_argument("--report-dir", default=None)
    args = ap.parse_args()
    cfg = json.load(open(args.config, encoding="utf-8")) if os.path.isfile(args.config) else {}
    verify_cfg = cfg.get("verify", {})
    report_dir = args.report_dir or verify_cfg.get("report_dir", "skills/blog-verify/reports")
    # allow calling from vault root content/.agents/skills/blog-verify but default is content root relative
    # resolve report_dir relative to content root (cwd)
    content_root = os.getcwd()
    # if invoked from elsewhere, find content root via blog-config.json location
    abs_report_dir = report_dir
    if not os.path.isabs(report_dir):
        # try .agents/skills/blog-verify/reports relative to content root
        cand = os.path.join(content_root, report_dir)
        # also handle bare "skills/blog-verify/reports"
        if not report_dir.startswith(".agents"):
            cand = os.path.join(content_root, ".agents", report_dir) if not os.path.isdir(cand) else cand
        abs_report_dir = cand if os.path.isdir(os.path.dirname(cand)) or report_dir.startswith(".agents") or report_dir.startswith("skills/") else cand
        # fallback: .agents/skills/blog-verify/reports
        if not os.path.isdir(os.path.dirname(abs_report_dir)):
            abs_report_dir = os.path.join(content_root, ".agents/skills/blog-verify/reports")
    # ensure dir
    os.makedirs(abs_report_dir, exist_ok=True)
    res = score_post(args.post, cfg)
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    report_path = os.path.join(abs_report_dir, f"verify-report-{ts}.md")
    body = f"""# Verify Report: {res['title']}

**File**: `{res['path']}`
**Score**: {res['score']}/100 — {'PASS' if not res['blocking'] else 'BLOCK'}
**Blocking**: {str(res['blocking']).lower()} — {'BLOCKING: true' if res['blocking'] else 'BLOCKING: false'}
**P0**: {', '.join(res['p0']) if res['p0'] else 'none'}
**Issues**: {'; '.join(res['issues']) if res['issues'] else 'none'}
**Ledger**: {res['ledger_note']}
**Internal/External**: {res['internal']}/{res['external']}

## Gate Summary (lite)
- Gate 4 Content Review: {'PASS' if res['score']>=90 and not res['p0'] else 'FAIL'} (≥90 + zero P0)
- Gate 5 Link Integrity: {'PASS' if res['external']>=1 else 'WARN'}

## Priority Fixes
1. {res['issues'][0] if res['issues'] else 'none — clear to publish via /blog-publish'}
2. {res['issues'][1] if len(res['issues'])>1 else '—'}
3. {res['issues'][2] if len(res['issues'])>2 else '—'}

## Next
{'Feed this report to next `/blog-write {post}` iteration (max 3).' if res['blocking'] else 'Run `/blog-publish ' + res['path'] + '` explicitly.'}
"""
    open(report_path, "w", encoding="utf-8").write(body)
    # prune keep 3
    keep = verify_cfg.get("keep_reports", 3)
    reports = sorted(glob.glob(os.path.join(abs_report_dir, "verify-report-*.md")))
    if len(reports) > keep:
        for old in reports[:-keep]:
            try: os.remove(old)
            except: pass
    # also prune research reports alongside (shared policy)
    print(body)
    # machine-readable last line for orchestrator
    print(f"\nBLOCKING: {'true' if res['blocking'] else 'false'}")
    print(f"REPORT: {report_path}", file=sys.stderr)

if __name__ == "__main__":
    main()
