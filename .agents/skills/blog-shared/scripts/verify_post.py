#!/usr/bin/env python3
"""
verify_post.py — Fast deterministic P0 pre-check for blog-verify.
Checks:
  - text_length and frontmatter rules (via text_length.py)
  - P0-DEADLINK: all [[wikilinks]] in body must exist in content/ and have publish: true
  - P0-IFRAME: no live <iframe> in draft (videos must be HTML comments)
  - P0-EMOJI: every H2 must end with an emoji
  - P0-LEAK: no internal project codenames (e.g. F2T, QualityEvaluator) or raw wiki note titles
  - P0-EDT: no visible editorial sections (Vùng liên kết, Khoảng trống, visible chart callouts)
  - P0-CALLOUT: all callout titles must be Vietnamese (except [!tldr])
  - P0-CHARSET: no curly quotes, ellipsis glyphs, or non-breaking spaces

Usage:
  python3 .agents/skills/blog-shared/scripts/verify_post.py --post <path> [--format text|json]
"""
import sys, os, re, json, argparse, unicodedata

# Helper to load all published blog post names/slugs
def get_published_blog_targets(content_root):
    published = {}
    for root, dirs, files in os.walk(content_root):
        if ".agents" in root or ".git" in root:
            continue
        for f in files:
            if f.endswith(".md"):
                full_path = os.path.join(root, f)
                try:
                    text = open(full_path, "r", encoding="utf-8").read()
                    # check publish: true
                    is_published = bool(re.search(r"^publish:\s*true\b", text, re.MULTILINE))
                    base = os.path.splitext(f)[0]
                    rel = os.path.relpath(full_path, content_root)
                    rel_no_ext = os.path.splitext(rel)[0]
                    # Title from frontmatter
                    title_m = re.search(r"^title:\s*[\"']?(.*?)[\"']?$", text, re.MULTILINE)
                    title = title_m.group(1) if title_m else ""
                    
                    target_info = {"file": rel, "published": is_published}
                    published[base.lower()] = target_info
                    published[rel_no_ext.lower()] = target_info
                    if title:
                        published[title.lower()] = target_info
                except Exception:
                    pass
    return published

def check_emoji(char):
    # Checks if a character is an emoji or symbol
    cat = unicodedata.category(char)
    if cat in ("So", "Sk"):
        return True
    cp = ord(char)
    # Common emoji ranges
    if (0x1F300 <= cp <= 0x1FAFF) or (0x2600 <= cp <= 0x27BF) or (0xFE00 <= cp <= 0xFE0F):
        return True
    return False

def heading_ends_with_emoji(h_text):
    clean = h_text.strip()
    if not clean:
        return False
    # Check last non-whitespace character
    last_char = clean[-1]
    if check_emoji(last_char):
        return True
    # In case of modifier / variation selector
    if len(clean) >= 2 and (check_emoji(clean[-2]) or check_emoji(clean[-1])):
        return True
    return False

def run_checks(post_path, content_root):
    from text_length import validate_post
    
    tl_res = validate_post(post_path, stage="verify")
    text = open(post_path, "r", encoding="utf-8").read()
    
    # Split frontmatter and body
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not m:
        return {"error": "Missing frontmatter", "passed": False}
    fm_text, body = m.group(1), m.group(2)
    
    # Strip comments to inspect visible body
    visible_body = re.sub(r"%%.*?%%", "", body, flags=re.DOTALL)
    visible_body = re.sub(r"<!--.*?-->", "", visible_body, flags=re.DOTALL)
    
    p0_issues = []
    warnings = []
    
    # Integrate text_length failures
    for c in tl_res.get("checks", []):
        if not c["passed"]:
            if c["critical"]:
                p0_issues.append(f"[{c['check']}] {c['message']}")
            else:
                warnings.append(f"[{c['check']}] {c['message']}")
                
    # 1. P0-DEADLINK: Check internal wikilinks
    published_targets = get_published_blog_targets(content_root)
    raw_wikilinks = re.findall(r"\[\[(.*?)\]\]", visible_body)
    dead_links = []
    for wl in raw_wikilinks:
        target = wl.split("|")[0].split("#")[0].strip().lower()
        if not target:
            continue
        # Check if target exists in published_targets with publish: true
        if target in published_targets:
            if not published_targets[target]["published"]:
                dead_links.append(f"[[{wl}]] -> target exists but publish: false")
        else:
            dead_links.append(f"[[{wl}]] -> no such file or post in content/")
            
    if dead_links:
        p0_issues.append(f"[P0-DEADLINK] Found {len(dead_links)} dead/unpublished internal links: " + ", ".join(dead_links[:5]))
        
    # 2. P0-IFRAME: No live <iframe> in draft
    iframes = re.findall(r"<iframe[\s\S]*?>[\s\S]*?</iframe>|<iframe[\s\S]*?/>", visible_body)
    if iframes:
        p0_issues.append(f"[P0-IFRAME] Found {len(iframes)} live <iframe> embeds in draft! Video must be commented out as <!-- Video suggestion: ... -->")

    # 3. P0-EMOJI: Every H2 must end with an emoji
    h2_matches = re.findall(r"^##\s+(.*?)$", visible_body, re.MULTILINE)
    missing_emoji_h2 = []
    for h in h2_matches:
        # Ignore comments or internal sections
        if "<!--" in h or "-->" in h:
            continue
        if not heading_ends_with_emoji(h):
            missing_emoji_h2.append(h)
    if missing_emoji_h2:
        p0_issues.append(f"[P0-EMOJI] {len(missing_emoji_h2)} H2 headings missing emoji: " + "; ".join(f"'{h}'" for h in missing_emoji_h2[:3]))

    # 4. P0-LEAK: Wiki context leakage (internal project codenames, raw wiki note titles)
    leak_patterns = [
        r"\bF2T\b", r"\bQualityEvaluator\b", r"\brolling window\b", r"\(Analysis\)",
        r"\bChapter \d+\b"
    ]
    leaks = []
    for lp in leak_patterns:
        matches = re.findall(lp, visible_body, re.IGNORECASE)
        if matches:
            leaks.append(f"Pattern '{lp}' found ({len(matches)} times)")
    if leaks:
        p0_issues.append(f"[P0-LEAK] Wiki internal context leaked in body: " + "; ".join(leaks))

    # 5. P0-EDT: Visible editorial content
    editorial_patterns = [
        (r"^##\s+Vùng liên kết nội bộ", "Visible 'Vùng liên kết nội bộ' section"),
        (r"^##\s+Khoảng trống nội dung", "Visible 'Khoảng trống nội dung' section"),
        (r">\s*\[!chart\]", "Visible [!chart] callout (must be commented out)"),
        (r"SEO\s*&\s*GEO", "Visible SEO & GEO planning block"),
        (r"Word count plan:", "Visible Word count plan")
    ]
    for ep, msg in editorial_patterns:
        if re.search(ep, visible_body, re.MULTILINE):
            p0_issues.append(f"[P0-EDT] {msg}")

    # 6. P0-CALLOUT: Callout language check
    callout_headers = re.findall(r"^>\s*\[!(\w+)\]\s*(.*)$", visible_body, re.MULTILINE)
    english_titles = ["Answer-first", "Tip and Tricks", "Internal linking", "Read more", "Note"]
    mixed_callouts = []
    for c_type, c_title in callout_headers:
        c_title_clean = c_title.strip()
        if c_type.lower() == "tldr":
            continue
        for et in english_titles:
            if et.lower() in c_title_clean.lower():
                mixed_callouts.append(f"[!{c_type}] {c_title_clean}")
    if mixed_callouts:
        p0_issues.append(f"[P0-CALLOUT] English callout titles found: " + ", ".join(mixed_callouts))

    # 7. P0-CHARSET: AI signal charset
    bad_chars = []
    for c in visible_body:
        cp = ord(c)
        if cp in (0x201C, 0x201D, 0x2018, 0x2019):
            bad_chars.append(f"Curly quote U+{cp:04X}")
        elif cp == 0x2026:
            bad_chars.append("Ellipsis glyph U+2026")
        elif cp == 0x00A0:
            bad_chars.append("Non-breaking space U+00A0")
    if bad_chars:
        p0_issues.append(f"[P0-CHARSET] AI-signal characters found: {set(bad_chars)}")

    passed = len(p0_issues) == 0
    return {
        "file": post_path,
        "passed": passed,
        "blocking": not passed,
        "p0_issues": p0_issues,
        "warnings": warnings,
        "body_word_count": tl_res.get("body_word_count")
    }

def main():
    parser = argparse.ArgumentParser(description="Deterministic P0 verification check")
    parser.add_argument("--post", required=True, help="Path to post file")
    parser.add_argument("--content-root", default=".", help="Root of content directory")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    
    script_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, script_dir)
    
    res = run_checks(args.post, args.content_root)
    
    if args.format == "json":
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"=== Blog Verification Fast P0 Check ===")
        print(f"File: {args.post}")
        print(f"Body words: {res.get('body_word_count')}")
        print(f"BLOCKING: {'true' if res.get('blocking') else 'false'}")
        if res.get("p0_issues"):
            print(f"\nP0 Issues ({len(res['p0_issues'])}):")
            for p in res["p0_issues"]:
                print(f"  ❌ {p}")
        if res.get("warnings"):
            print(f"\nWarnings ({len(res['warnings'])}):")
            for w in res["warnings"]:
                print(f"  ⚠️  {w}")
        if res["passed"]:
            print("\n✅ All deterministic P0 checks PASSED!")
            
    sys.exit(0 if res.get("passed") else 1)

if __name__ == "__main__":
    main()
