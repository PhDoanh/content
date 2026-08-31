# Adapter: obsidian-cli (kepano/obsidian-skills)

- **Source**: `kepano/obsidian-skills` `skills/obsidian-cli/SKILL.md` (106 lines, 2026)
- **Distilled to**: `.agents/skills/obsidian-cli/` (verbatim)
- **Role in pipeline**: Primary transport for vault operations in `personal-wiki`. Preferred over filesystem fallback. `blog-research` should attempt `obsidian read/search` via CLI when `transport.json: preferred=cli`, fallback to filesystem `Read/Grep` if CLI unavailable (Obsidian not running).
- **Usage note**: Requires Obsidian 1.12+ running. In headless/WSL, fallback to filesystem automatically. Do not install `.vault-meta` into `content`; this adapter is reference-only for `personal-wiki` operations.
- **Original**: https://github.com/kepano/obsidian-skills
