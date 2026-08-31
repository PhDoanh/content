# Adapter: blog-shared (claude-blog shared references + templates)

- **Source**: `AgriciDaniel/claude-blog` `skills/blog/references/*` (16 files) + `skills/blog/templates/*` (12 files)
- **Distilled to**: `.agents/skills/blog-shared/references/` + `templates/`
- **Role in pipeline**: Shared contracts consumed by multiple distilled adapters. `blog-write`, `blog-outline`, `blog-brief`, `blog-analyze`, `blog-geo`, `blog-seo-check`, `blog-audit` all read from here via relative `../blog-shared/references/<file>`.
- **Key files**:
  - `quality-scoring.md` — 100pt Content30/SEO25/E-E-A-T15/Technical15/AI15
  - `blog-delivery-contract.md` — 5-gate BLOCKING true/false, max 3 iterations
  - `synthesis-contract.md` — 6 LAWs for synthesis output
  - `content-templates.md` — 12 template selection criteria
  - `visual-media.md`, `eeat-signals.md`, `internal-linking.md`, `flow-alignment.md`, etc.
  - `templates/how-to-guide.md` … `tutorial.md` (12 types)
- **Original**: https://github.com/AgriciDaniel/claude-blog
