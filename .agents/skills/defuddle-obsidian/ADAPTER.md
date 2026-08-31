# Adapter: defuddle (claude-obsidian)

- **Source**: `claude-obsidian` `skills/defuddle/SKILL.md` (personal-wiki)
- **Distilled to**: `.agents/skills/defuddle-obsidian/` (verbatim) — preserved for provenance; pipeline should prefer `defuddle-kepano` for web cleaning (kepano is upstream for `obsidian-cli`/`obsidian-markdown` consistency), but both wrap same `defuddle-cli`.
- **Role**: Vault ingestion cleaning in personal-wiki; blog pipeline may fallback to this if kepano version unavailable.
