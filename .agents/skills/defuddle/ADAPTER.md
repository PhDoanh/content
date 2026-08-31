# Adapter: defuddle (kepano/obsidian-skills)

- **Source**: `kepano/obsidian-skills` `skills/defuddle/SKILL.md` (41 lines)
- **Distilled to**: `.agents/skills/defuddle/` (verbatim)
- **Role in pipeline**: Pre-process all `WebFetch` URLs in `blog-write` Phase 2 and `blog-verify` fact-check. Saves 40-60% tokens, strips ads/nav. Use `defuddle parse <url> --md` preferentially over raw `WebFetch`.
- **Install**: `npm install -g defuddle` (merged package; `defuddle-cli@0.7.0` deprecated) — verified `defuddle 0.1.0`.

- **Original**: https://github.com/kepano/defuddle
