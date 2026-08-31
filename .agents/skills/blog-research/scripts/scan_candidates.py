#!/usr/bin/env python3
"""
Filesystem vault read via Glob directly on $WIKI_PATH/wiki/**/*.md.

- Reads WIKI_PATH (absolute, default /mnt/d/phdoanh/personal-wiki)
- Loads content/blog-config.json (vault root) for source_scope/research thresholds
- Scans wiki/
- No LLM calls

Reuses claude-obsidian wiki-query Assess evidence (claim-ledger) later in research step.
"""
import json, os, re, sys, glob
# Optional: yaml.safe_load for stricter frontmatter; fallback to manual parse if PyYAML unavailable

def load_config():
    # content vault root = cwd or vault param
    candidates = [
        os.environ.get("BLOG_CONFIG", ""),
        "blog-config.json",
        ".vault-meta/blog-config.json",
        os.path.join(os.environ.get("WIKI_PATH", "/mnt/d/phdoanh/personal-wiki"), ".vault-meta/blog-config.json"),
    ]
    for p in candidates:
        if p and os.path.isfile(p):
            with open(p, "r", encoding="utf-8") as f:
                return json.load(f), p
    raise FileNotFoundError("blog-config.json not found (tried BLOG_CONFIG, ./blog-config.json)")

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n(.*)$", re.DOTALL)

def parse_frontmatter(text):
    m = FRONTMATTER_RE.match(text)
    if not m:
        return {}, text
    raw_fm, body = m.group(1), m.group(2)
    fm = {}
    current_key = None
    for line in raw_fm.splitlines():
        if not line.strip():
            continue
        if line.startswith(" ") or line.startswith("\t"):
            item = line.strip()
            if item.startswith("- "):
                item = item[2:].strip().strip('"')
                fm.setdefault(current_key, [])
                if isinstance(fm.get(current_key), list):
                    fm[current_key].append(item)
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            current_key = key
            if val == "":
                fm[key] = []
            else:
                fm[key] = val.strip('"').strip("'")
    return fm, body

def extract_blog_refs(body, begin_marker, end_marker):
    if begin_marker not in body or end_marker not in body:
        return []
    chunk = body.split(begin_marker, 1)[1].split(end_marker, 1)[0]
    refs, entry = [], {}
    for line in chunk.splitlines():
        line = line.strip()
        if line.startswith("- post:"):
            if entry:
                refs.append(entry)
            entry = {"post": line.split("post:", 1)[1].strip()}
        elif line.startswith("date:"):
            entry["date"] = line.split("date:", 1)[1].strip()
        elif line.startswith("angle:"):
            entry["angle"] = line.split("angle:", 1)[1].strip()
    if entry:
        refs.append(entry)
    return refs

def main():
    import pathlib
    cfg, cfg_path = load_config()
    research = cfg.get("research", cfg)
    wiki_path = os.environ.get(cfg.get("vault", {}).get("wiki_path_env", "WIKI_PATH"), cfg.get("vault", {}).get("wiki_path_default", "/mnt/d/phdoanh/personal-wiki"))
    scopes = research.get("source_scope", cfg.get("source_scope", ["wiki/"]))
    blocklist = set(t.lower() for t in research.get("transient_tag_blocklist", cfg.get("transient_tag_blocklist", [])))
    eligible_status = set(research.get("maturity_levels_eligible", cfg.get("maturity_levels_eligible", ["mature","developing"])))
    min_links = research.get("min_wikilinks", cfg.get("min_wikilinks", 2))
    # blog_refs markers (legacy compat)
    blog_refs = cfg.get("blog_refs", {"begin_marker": "<!-- blog-refs:begin -->", "end_marker": "<!-- blog-refs:end -->"})
    begin_m = blog_refs.get("begin_marker", "<!-- blog-refs:begin -->")
    end_m = blog_refs.get("end_marker", "<!-- blog-refs:end -->")

    candidates = []
    for scope in scopes:
        pat = os.path.join(wiki_path, scope.strip("/"), "**/*.md")
        for fp in glob.glob(pat, recursive=True):
            if not os.path.isfile(fp):
                continue
            text = open(fp, encoding="utf-8", errors="ignore").read()
            fm, body = parse_frontmatter(text)
            tags = [t.strip().lower() for t in (fm.get("tags") or []) if isinstance(fm.get("tags"), list) or isinstance(t, str)]
            # normalize tags if single string
            if isinstance(fm.get("tags"), str):
                tags = [fm.get("tags").lower()]
            # blocklist
            if any(t.lower() in blocklist for t in tags):
                continue
            status = str(fm.get("status", "")).lower()
            if eligible_status and status and status not in eligible_status:
                # allow empty status as eligible (seed)
                if status:
                    continue
            # wikilinks count from related + body [[
            related = fm.get("related") or []
            if isinstance(related, str):
                related = [related]
            related_clean = [re.sub(r"^\[\[|\]\]$", "", str(v)) for v in related]
            wikilinks = len(related_clean) + len(re.findall(r"\[\[", body))
            if wikilinks < min_links:
                continue
            word_count = len(re.findall(r"\w+", body))
            # existing taxonomy
            existing = None
            for t in tags:
                if t in (cfg.get("taxonomy", {}).get("subclusters", []) if isinstance(cfg.get("taxonomy"), dict) else cfg.get("taxonomy", [])):
                    existing = t
                    break
            candidates.append({
                "title": fm.get("title") or pathlib.Path(fp).stem,
                "path": fp,
                "rel_path": os.path.relpath(fp, wiki_path),
                "tags": tags,
                "status": status,
                "word_count": word_count,
                "related": related_clean,
                "blog_refs": extract_blog_refs(body, begin_m, end_m),
                "existing_taxonomy_tag": existing,
            })

    out = {"candidates": candidates, "config_path": cfg_path, "wiki_path": wiki_path}
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
