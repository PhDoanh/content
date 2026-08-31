# Adapter: defuddle (kepano/obsidian-skills)

- **Source**: `kepano/obsidian-skills` `skills/defuddle/SKILL.md` (41 lines) — kepano wrapper around `defuddle-cli` (github.com/kepano/defuddle)
- **Distilled to**: `.agents/skills/defuddle-kepano/` (verbatim)
- **Role in pipeline**: Pre-process all `WebFetch` URLs in `blog-write` Phase 2 and `blog-verify` fact-check. Saves 40-60% tokens, strips ads/nav. Use `defuddle parse <url> --md` preferentially over raw `WebFetch`.
- **Install**: `npm install -g defuddle-cli` then `defuddle --version` to verify.
- **Note**: `claude-obsidian:defuddle` (personal-wiki) is canonical for vault ingestion; this kepano variant is canonical for blog pipeline web cleaning. Both wrap same CLI.
- **Original**: https://github.com/kepano/defuddle
