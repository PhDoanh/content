#!/usr/bin/env python3
"""
write_report.py — helper to write verbatim research-report-{ts}.json for blog-research.

Keeps 3 then prune.
Usage: echo '{"topic": "...", "label": "..."}' | python3 write_report.py --config blog-config.json
"""
import json, os, sys, glob, datetime, argparse

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--config", default="blog-config.json")
    ap.add_argument("--report-dir", default=None)
    args = ap.parse_args()
    cfg = json.load(open(args.config, encoding="utf-8")) if os.path.isfile(args.config) else {}
    r_cfg = cfg.get("research", {})
    report_dir = args.report_dir or r_cfg.get("report_dir", "skills/blog-research/reports")
    content_root = os.getcwd()
    abs_dir = report_dir if os.path.isabs(report_dir) else os.path.join(content_root, ".agents", report_dir) if not report_dir.startswith(".agents") and not os.path.isdir(os.path.join(content_root, report_dir)) else os.path.join(content_root, report_dir)
    # normalize: if path is skills/blog-research/reports -> .agents/skills/...
    if report_dir.startswith("skills/"):
        abs_dir = os.path.join(content_root, ".agents", report_dir)
    if not os.path.isdir(abs_dir):
        abs_dir = os.path.join(content_root, ".agents/skills/blog-research/reports")
    os.makedirs(abs_dir, exist_ok=True)
    data = json.load(sys.stdin) if not sys.stdin.isatty() else {}
    # enrich timestamp
    data["generated_at"] = datetime.datetime.now().isoformat()
    ts = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
    path = os.path.join(abs_dir, f"research-report-{ts}.json")
    open(path, "w", encoding="utf-8").write(json.dumps(data, ensure_ascii=False, indent=2))
    keep = r_cfg.get("keep_reports", 3)
    reports = sorted(glob.glob(os.path.join(abs_dir, "research-report-*.json")))
    if len(reports) > keep:
        for old in reports[:-keep]:
            try: os.remove(old)
            except: pass
    print(json.dumps({"report": path, "keep": keep}, ensure_ascii=False))
    print(path, file=sys.stderr)

if __name__ == "__main__":
    main()
