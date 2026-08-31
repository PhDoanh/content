# Adapter: obsidian-markdown (kepano/obsidian-skills)

- **Source**: `kepano/obsidian-skills` `skills/obsidian-markdown/SKILL.md` (196 lines) + `references/CALLOUTS.md`, `EMBEDS.md`, `PROPERTIES.md`
- **Distilled to**: `.agents/skills/obsidian-markdown/` (verbatim)
- **Role in pipeline**: Canonical syntax for all `blog-outline` / `blog-write` outputs. Ensures `[[wikilink]]`, `![[embed]]`, callouts `> [!type]`, properties YAML are Quartz-compatible. Replaces LLM guesswork.
- **Precedence**: Prefer this kepano version over `claude-obsidian:obsidian-markdown` fallback when both available.
- **Original**: https://github.com/kepano/obsidian-skills
