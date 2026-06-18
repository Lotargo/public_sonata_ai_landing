# Sonata public asset style guide

This repository should present Sonata as a technical research dossier, not as a generic AI product landing page. Visual assets should therefore feel like calm engineering evidence: structured, restrained, reproducible, and public-safe.

## Visual direction

Use an SVG-first workflow for diagrams and plots. SVG keeps text sharp on GitHub Pages, scales cleanly for Retina displays, and is easier to diff/review than binary PNG output.

The default generator uses:

- canvas: `1200 × 720`
- background: `#F8FAFC`
- panel: `#FFFFFF`
- text: `#0F172A`
- muted text: `#64748B`
- grid/border: `#E2E8F0` / `#CBD5E1`
- accents: blue `#2563EB`, violet `#7C3AED`, green `#059669`, amber `#D97706`, red `#DC2626`, cyan `#0891B2`

## Design rules

1. Prefer one idea per asset. Do not turn diagrams into dense posters.
2. Keep claims scoped: use charts and diagrams as evidence wrappers, not hype banners.
3. Use SVG for the canonical asset. Export PNG only for social previews, thumbnails, or platforms that cannot render SVG.
4. Use one consistent diagram grammar: cards, pills, restrained arrows, short labels, and stable spacing.
5. For plots, show the metric plainly. Avoid decorative gradients, aggressive shadows, and random palette changes.
6. Put detailed interpretation in the surrounding Markdown page rather than inside the figure.

## Regeneration

Run from the repository root:

```bash
python assets/generate_public_assets.py
```

The script writes professional SVG assets into:

- `assets/diagrams/*.svg`
- `assets/plots/*.svg`

The old PNG files can remain temporarily as compatibility fallbacks, but new pages should reference SVG first.