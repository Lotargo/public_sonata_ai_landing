# Public Sonata Landing

This directory is the staging area for the future portable public landing package for Sonata.

It is designed to be copied/exported into a separate public portfolio or GitHub Pages repository without exposing the private Sonata source code.

## Current structure

- `docs_tmp/` — temporary holding area for planning documents migrated from the repository root.
- `docs/` — future public-safe Markdown dossier pages.
- `pages/` — future static HTML pages.
- `assets/` — diagrams, plots, screenshots, thumbnails, and the public asset generator.
- `data/` — public-safe JSON summaries and claim/evidence matrices.
- `styles/` — CSS.
- `scripts/` — optional static JavaScript.

## Asset workflow

The public visual system is SVG-first. Regenerate the professional diagram and plot set with:

```bash
python assets/generate_public_assets.py
```

Canonical generated files should live in:

- `assets/diagrams/*.svg`
- `assets/plots/*.svg`

PNG files may be kept as compatibility fallbacks, but GitHub Pages and documentation pages should prefer SVG assets.

See `assets/ASSET_STYLE_GUIDE.md` for the visual rules.

## Rule

No private code, secrets, implementation recipes, or unsafe internal paths should be placed here.
