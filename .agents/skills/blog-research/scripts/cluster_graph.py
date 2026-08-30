#!/usr/bin/env python3
"""
Builds undirected graph from each note's `related` wikilinks (populated by
wiki-ingest, no invention), computes connected components restricted to
candidate set, filters by min_cluster_notes/min_cluster_words from
content/blog-config.json, suggests taxonomy via majority vote.
"""
import json, sys, argparse

def build_components(candidates):
    by_title = {c["title"]: c for c in candidates}
    visited = set()
    components = []
    for c in candidates:
        if c["title"] in visited:
            continue
        stack = [c["title"]]
        comp = []
        while stack:
            t = stack.pop()
            if t in visited or t not in by_title:
                continue
            visited.add(t)
            comp.append(by_title[t])
            for r in by_title[t].get("related", []):
                if r in by_title and r not in visited:
                    stack.append(r)
        components.append(comp)
    return components

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", default="-")
    ap.add_argument("--config", required=True)
    args = ap.parse_args()

    data = json.load(sys.stdin) if args.input == "-" else json.load(open(args.input, encoding="utf-8"))
    cfg = json.load(open(args.config, encoding="utf-8"))
    research = cfg.get("research", cfg)
    # support both old and new candidate shapes
    candidates = data.get("candidates") or data
    if isinstance(candidates, dict) and "candidates" in candidates:
        candidates = candidates["candidates"]

    components = build_components(candidates)

    min_notes = research.get("min_cluster_notes", cfg.get("min_cluster_notes", 3))
    min_words = research.get("min_cluster_words", cfg.get("min_cluster_words", 800))

    clusters = []
    for comp in components:
        total_words = sum(n.get("word_count", 0) for n in comp)
        if len(comp) < min_notes:
            continue
        if total_words < min_words:
            continue
        tag_votes = {}
        for n in comp:
            if n.get("existing_taxonomy_tag"):
                tag_votes[n["existing_taxonomy_tag"]] = tag_votes.get(n["existing_taxonomy_tag"], 0) + 1
        suggested_tag = max(tag_votes, key=tag_votes.get) if tag_votes else None
        clusters.append({
            "notes": [n["title"] for n in comp],
            "paths": [n["path"] for n in comp],
            "blog_refs_by_note": {n["title"]: n.get("blog_refs", []) for n in comp},
            "total_words": total_words,
            "suggested_taxonomy_tag": suggested_tag,
            "needs_taxonomy_decision": suggested_tag is None,
        })

    print(json.dumps({
        "clusters": clusters,
        "note": ("LLM must now: (a) pick 1 taxonomy tag per cluster if needs_taxonomy_decision, "
                 "(b) cross-check against content/<tag>/*.md publish:true posts to avoid "
                 "duplicate topics, (c) check each note's blog_refs for already-used angles, "
                 "(d) select at most 1 cluster or abstain (hard-bound: no forced output).")
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
