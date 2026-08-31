#!/usr/bin/env python3
"""
finalize_outline.py — Sets `updated` to today, validates lang vs body char distribution,
trusts `publish: false`.

Usage:
  python3 finalize_outline.py --post <path> --config blog-config.json
"""
import json, re, sys, argparse, unicodedata, datetime

def lang_ratios(body):
    vi_diacritics = re.compile(
        r"[\u00e0\u00e1\u1ea1\u1ea3\u00e3\u00e2\u1ea7\u1ea5\u1ead\u1ea9\u1eab"
        r"\u0103\u1eb1\u1eaf\u1eb7\u1eb3\u1eb5\u00e8\u00e9\u1eb9\u1ebb\u1ebd"
        r"\u00ea\u1ec1\u1ebf\u1ec7\u1ec3\u1ec5\u00ec\u00ed\u1ecb\u1ec9\u0129"
        r"\u00f2\u00f3\u1ecd\u1ecf\u00f5\u00f4\u1ed3\u1ed1\u1ed9\u1ed5\u1ed7"
        r"\u01a1\u1edd\u1edb\u1ee3\u1edf\u1ee1\u00f9\u00fa\u1ee5\u1ee7\u0169"
        r"\u01b0\u1eeb\u1ee9\u1ef1\u1eed\u1eef\u1ef3\u00fd\u1ef5\u1ef7\u1ef9\u0111]",
        re.IGNORECASE,
    )
    ja_chars = re.compile(r"[\u3040-\u30ff\u4e00-\u9fff]")
    total = max(len(re.sub(r"\s", "", body)), 1)
    vi = len(vi_diacritics.findall(body))
    ja = len(ja_chars.findall(body))
    return {"vi": vi / total, "ja": ja / total, "en": len(re.findall(r"[A-Za-z]", body)) / total}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--post", required=True, help="Path to post file to finalize")
    ap.add_argument("--config", required=True)
    args = ap.parse_args()
    cfg = json.load(open(args.config, encoding="utf-8"))
    text = open(args.post, encoding="utf-8").read()
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.DOTALL)
    if not m:
        print("ERROR: post has no frontmatter", file=sys.stderr); sys.exit(1)
    fm_raw, body = m.group(1), m.group(2)
    # bump updated (Q-P-1 yes, but outline also sets today)
    today = datetime.date.today().isoformat()
    if re.search(r"^updated:", fm_raw, re.MULTILINE):
        fm_raw = re.sub(r"^updated:.*$", f"updated: {today}", fm_raw, flags=re.MULTILINE)
    else:
        fm_raw += f"\nupdated: {today}"
    # lang check (warn only)
    lang_m = re.search(r"^lang:\s*(\w+)", fm_raw, re.MULTILINE)
    default_lang = cfg.get("write", {}).get("default_lang", cfg.get("default_lang", "vi"))
    declared = lang_m.group(1) if lang_m else default_lang
    ratios = lang_ratios(body)
    dominant = max(ratios, key=ratios.get)
    thresh = cfg.get("write", {}).get("lang_char_ratio_warn_threshold", 0.3)  # blog-config.json:write.lang_char_ratio_warn_threshold
    if dominant != declared and ratios[dominant] > thresh:
        print(f"WARNING: declared lang='{declared}' but content seems '{dominant}' (~{ratios[dominant]:.0%})", file=sys.stderr)
    # permalink is MANUAL per Q3 — do not touch, just ensure it exists empty if missing
    if not re.search(r"^permalink:", fm_raw, re.MULTILINE):
        fm_raw += '\npermalink: ""'
    # keep publish false
    if not re.search(r"^publish:", fm_raw, re.MULTILINE):
        fm_raw += "\npublish: false"
    final = f"---\n{fm_raw}\n---\n{body}"
    open(args.post, "w", encoding="utf-8").write(final)
    print(json.dumps({"post": args.post, "updated": today, "permalink_manual": True}, ensure_ascii=False))

if __name__ == "__main__":
    main()
