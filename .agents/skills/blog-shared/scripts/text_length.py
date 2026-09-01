#!/usr/bin/env python3
"""
text_length.py — Deterministic length and frontmatter validation for blog pipeline.
Checks:
  - Body word count (strips frontmatter, comments, code blocks)
  - Slug length (<= 4 words, kebab-case)
  - Frontmatter character counts (title, description, socialDescription)
  - Tag rules (3-5 specialized + GenAI + Level tag, no folder names)
  - Stage-specific frontmatter field permissions (outline, write, verify, publish)

Usage:
  python3 .agents/skills/blog-shared/scripts/text_length.py --post <path> [--stage outline|write|verify|publish] [--format text|json]
"""
import sys, os, re, json, argparse, datetime

CORE_FOLDER_TAGS = {
    "fullstack", "system-foundations", "automation", "ai-orchestration",
    "best-practices", "beyond-code"
}
LEVEL_TAGS = {"Beginner", "Intermediate", "Advanced", "Expert"}

def parse_frontmatter(text):
    m = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    raw_fm = m.group(1)
    body = m.group(2)
    data = {}
    current_key = None
    list_items = []
    
    for line in raw_fm.splitlines():
        line = line.rstrip()
        if not line:
            continue
        key_match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*)$", line)
        if key_match:
            if current_key and list_items:
                data[current_key] = list_items
                list_items = []
            k, v = key_match.group(1), key_match.group(2).strip()
            current_key = k
            if v == "" or v is None:
                data[k] = ""
            else:
                if (v.startswith('"') and v.endswith('"')) or (v.startswith("'") and v.endswith("'")):
                    v = v[1:-1]
                elif v.lower() == "true":
                    v = True
                elif v.lower() == "false":
                    v = False
                data[k] = v
        elif line.startswith("  - ") or line.startswith("- "):
            item = re.sub(r"^\s*-\s*", "", line).strip()
            if (item.startswith('"') and item.endswith('"')) or (item.startswith("'") and item.endswith("'")):
                item = item[1:-1]
            list_items.append(item)
    
    if current_key and list_items:
        data[current_key] = list_items
        
    return data, body

def calculate_body_words(body):
    t = body
    t = re.sub(r"%%.*?%%", "", t, flags=re.DOTALL)
    t = re.sub(r"<!--.*?-->", "", t, flags=re.DOTALL)
    t = re.sub(r"\x60{3}.*?\x60{3}", "", t, flags=re.DOTALL)
    t = re.sub(r"\x60[^\n`]+?\x60", "", t)  # inline code
    words = t.split()
    return len(words), t

def check_slug(filepath):
    filename = os.path.basename(filepath)
    slug, _ = os.path.splitext(filename)
    if slug == "index":
        slug = os.path.basename(os.path.dirname(os.path.abspath(filepath)))
    words = slug.split("-")
    is_kebab = bool(re.match(r"^[a-z0-9]+(-[a-z0-9]+)*$", slug))
    return {
        "slug": slug,
        "word_count": len(words),
        "is_kebab": is_kebab,
        "passed": len(words) <= 4 and is_kebab,
        "issue": None if (len(words) <= 4 and is_kebab) else f"Slug '{slug}' has {len(words)} words (max 4) or not kebab-case"
    }

def validate_post(post_path, stage="verify"):
    if not os.path.exists(post_path):
        return {"error": f"File not found: {post_path}", "passed": False}
    
    text = open(post_path, "r", encoding="utf-8").read()
    fm, body = parse_frontmatter(text)
    if fm is None:
        return {"error": "Missing frontmatter '---' block", "passed": False}
    
    body_wc, cleaned_body = calculate_body_words(body)
    slug_check = check_slug(post_path)
    
    results = {
        "file": post_path,
        "stage": stage,
        "body_word_count": body_wc,
        "body_wc_passed": 1500 <= body_wc <= 3000 if stage in ["write", "verify"] else body_wc <= 3000,
        "slug": slug_check,
        "checks": [],
        "passed": True
    }
    
    def add_check(name, passed, message, is_critical=True):
        results["checks"].append({
            "check": name,
            "passed": passed,
            "message": message,
            "critical": is_critical
        })
        if is_critical and not passed:
            results["passed"] = False

    # 1. Body word count check
    if stage in ["write", "verify"]:
        if body_wc > 3000:
            add_check("body_word_count", False, f"Body word count is {body_wc} (hard limit is 3000 words)", True)
        elif body_wc < 1500:
            add_check("body_word_count", False, f"Body word count is {body_wc} (recommended minimum 1500 words)", False)
        else:
            add_check("body_word_count", True, f"Body word count is {body_wc} (within 1500-3000 range)", True)
    elif stage == "outline":
        if body_wc > 3000:
            add_check("body_word_count", False, f"Outline body word count is {body_wc} (exceeds 3000 words)", True)
        else:
            add_check("body_word_count", True, f"Outline body word count is {body_wc}", True)

    # 2. Slug check
    add_check("slug_length", slug_check["passed"], slug_check["issue"] or f"Slug '{slug_check['slug']}' is <=4 words kebab-case", False)

    # 3. Title length (50-60 chars)
    title = str(fm.get("title", ""))
    t_len = len(title)
    if 50 <= t_len <= 60:
        add_check("title_length", True, f"Title length {t_len} chars (ideal 50-60)", False)
    elif 40 <= t_len <= 70:
        add_check("title_length", True, f"Title length {t_len} chars (acceptable 40-70, ideal 50-60)", False)
    else:
        add_check("title_length", False, f"Title length {t_len} chars (outside 40-70 range: '{title}')", False)

    # 4. Description length (140-160 chars)
    desc = str(fm.get("description", ""))
    d_len = len(desc)
    if 140 <= d_len <= 160:
        add_check("description_length", True, f"Description length {d_len} chars (ideal 140-160)", False)
    elif 120 <= d_len <= 180:
        add_check("description_length", True, f"Description length {d_len} chars (acceptable 120-180, ideal 140-160)", False)
    else:
        add_check("description_length", False, f"Description length {d_len} chars (outside 120-180 range)", False)

    # 5. SocialDescription length (~100 chars: 70-130)
    sdesc = str(fm.get("socialDescription", ""))
    if sdesc:
        sd_len = len(sdesc)
        if 80 <= sd_len <= 120:
            add_check("social_description_length", True, f"SocialDescription length {sd_len} chars (~100)", False)
        elif 60 <= sd_len <= 140:
            add_check("social_description_length", True, f"SocialDescription length {sd_len} chars (acceptable 60-140)", False)
        else:
            add_check("social_description_length", False, f"SocialDescription length {sd_len} chars (outside 60-140 range)", False)
    else:
        add_check("social_description_length", False, "Missing socialDescription in frontmatter", True)

    # 6. Tags rules
    raw_tags = fm.get("tags", [])
    if isinstance(raw_tags, str):
        raw_tags = [raw_tags]
    tags = [t for t in raw_tags if t]
    
    # Must have GenAI
    has_genai = "GenAI" in tags
    add_check("tag_genai", has_genai, "Tags must include 'GenAI'", True)
    
    # Must have level
    found_levels = [t for t in tags if t in LEVEL_TAGS]
    has_level = len(found_levels) == 1
    add_check("tag_level", has_level, f"Tags must have exactly one Level ({LEVEL_TAGS}), found: {found_levels}", True)
    
    # Must NOT have core folder names
    leaked_folder_tags = [t for t in tags if t.lower() in CORE_FOLDER_TAGS]
    add_check("no_folder_tags", len(leaked_folder_tags) == 0, 
              f"Tags must NOT contain folder names {CORE_FOLDER_TAGS}; found leaked: {leaked_folder_tags}", True)
    
    # Specialized tags count: excluding GenAI and Level, should be 3-5
    specialized_tags = [t for t in tags if t != "GenAI" and t not in LEVEL_TAGS and t.lower() not in CORE_FOLDER_TAGS]
    spec_ok = 3 <= len(specialized_tags) <= 5
    add_check("specialized_tags_count", spec_ok, 
              f"Must have 3-5 specialized topic tags, found {len(specialized_tags)}: {specialized_tags}", False)

    # 7. Stage-specific Frontmatter permissions (Issue 1)
    if stage == "outline":
        # At outline: updated must NOT be set, permalink must be empty "", publish must be False
        if "updated" in fm and fm["updated"]:
            add_check("fm_stage_outline_updated", False, f"'updated' should NOT be filled at outline stage (found: {fm.get('updated')})", True)
        else:
            add_check("fm_stage_outline_updated", True, "'updated' is empty/omitted at outline stage", True)
            
        if fm.get("permalink", "") != "":
            add_check("fm_stage_outline_permalink", False, f"'permalink' must be empty \"\" at outline stage (found: {fm.get('permalink')})", True)
        else:
            add_check("fm_stage_outline_permalink", True, "'permalink' is empty at outline stage", True)
            
        if fm.get("publish") is not False:
            add_check("fm_stage_outline_publish", False, f"'publish' must be false at outline stage (found: {fm.get('publish')})", True)
        else:
            add_check("fm_stage_outline_publish", True, "'publish' is false at outline stage", True)
            
        if fm.get("aliases") and fm["aliases"] != [""]:
            add_check("fm_stage_outline_aliases", False, f"'aliases' should not be filled at outline stage (found: {fm.get('aliases')})", False)
        if fm.get("socialImage") and fm["socialImage"] != "":
            add_check("fm_stage_outline_socialImage", False, f"'socialImage' should not be filled at outline stage (found: {fm.get('socialImage')})", False)

    elif stage in ["write", "verify"]:
        if "updated" not in fm or not fm["updated"]:
            add_check("fm_updated_present", False, "'updated' date must be present after blog-write", True)
        else:
            add_check("fm_updated_present", True, f"'updated' date is {fm.get('updated')}", True)
            
        if fm.get("permalink", "") != "":
            add_check("fm_permalink_manual", False, f"'permalink' must remain empty \"\" until blog-publish (found: {fm.get('permalink')})", True)
        else:
            add_check("fm_permalink_manual", True, "'permalink' is correctly empty", True)
            
        if fm.get("publish") is not False:
            add_check("fm_publish_false", False, f"'publish' must be false before blog-publish (found: {fm.get('publish')})", True)
        else:
            add_check("fm_publish_false", True, "'publish' is correctly false", True)

    elif stage == "publish":
        if fm.get("publish") is not True:
            add_check("fm_publish_true", False, "'publish' must be true at publish stage", True)
        else:
            add_check("fm_publish_true", True, "'publish' is true", True)

    return results

def main():
    parser = argparse.ArgumentParser(description="Deterministic length and frontmatter validation")
    parser.add_argument("--post", required=True, help="Path to blog post markdown file")
    parser.add_argument("--stage", choices=["outline", "write", "verify", "publish"], default="verify", help="Pipeline stage")
    parser.add_argument("--format", choices=["text", "json"], default="text", help="Output format")
    args = parser.parse_args()
    
    res = validate_post(args.post, args.stage)
    
    if args.format == "json":
        print(json.dumps(res, indent=2, ensure_ascii=False))
    else:
        print(f"=== Text Length & Frontmatter Validation ({args.stage.upper()}) ===")
        print(f"File: {res.get('file', args.post)}")
        print(f"Body words: {res.get('body_word_count', 'N/A')}")
        print(f"Overall Passed: {res.get('passed', False)}")
        print("\nDetailed Checks:")
        for c in res.get("checks", []):
            status = "PASS" if c["passed"] else ("FAIL (P0)" if c["critical"] else "WARN")
            print(f"  [{status}] {c['check']}: {c['message']}")
            
    sys.exit(0 if res.get("passed", False) else 1)

if __name__ == "__main__":
    main()
