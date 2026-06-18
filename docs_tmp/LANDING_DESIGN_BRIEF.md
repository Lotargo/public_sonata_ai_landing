# Sonata Landing Design Brief

**Status:** draft  
**Location:** `public_sonata_landing/`  
**Purpose:** define the visual direction for the portable Sonata landing page without turning it into a large design manual.

---

## 1. Design intent

The landing should feel like a **technical dossier / research wiki**, not a startup pitch page.

It should communicate:

- closed-source project, public-safe evidence;
- engineering seriousness;
- readable documentation;
- limitations shown openly;
- calm confidence without dramatic promises.

The page should filter its audience by being precise and document-like. It should be approachable for engineers and researchers, but not optimized for casual hype-driven readers.

---

## 2. Reference directions

The generated mockups are **inspiration references only**. We should not copy them 1:1.

### Reference A — dark graphite dossier

Suggested asset path after export:

`public_sonata_landing/assets/references/ref_dark_graphite_dossier.png`

What we like:

- dark editorial feeling;
- left sidebar navigation;
- large `Sonata` title;
- evidence cards;
- restrained cyan accents;
- strong “research dossier” mood.

What not to copy directly:

- benchmark/product-like cards that imply external model comparisons;
- any wording that sounds like broad model capability claims;
- too many charts above the fold.

### Reference B — white wiki / lab paper

Suggested asset path after export:

`public_sonata_landing/assets/references/ref_white_wiki_dossier.png`

What we like:

- clean wiki/documentation feeling;
- excellent readability;
- archive/dossier structure;
- metadata panel;
- documentation map blocks;
- good fit for technical readers.

What not to copy directly:

- generic AI evaluation labels;
- overly academic fake metadata;
- anything that makes the project look more institutional than it is.

### Reference C — midnight engineering archive

Suggested asset path after export:

`public_sonata_landing/assets/references/ref_midnight_engineering_archive.png`

What we like:

- colors and contrast;
- engineering archive mood;
- Mamba + Autograd / GPU / Benchmark / Limitations card structure;
- compact sidebar;
- restrained teal highlights.

What not to copy directly:

- exact dashboard layout;
- hardware metrics that do not match our actual evidence;
- overly polished “product dashboard” feeling.

---

## 3. Chosen direction

Use a hybrid approach:

> **White wiki structure + dark engineering archive mood.**

The default reading experience can lean toward the **white wiki/dossier** style because it is readable and feels like documentation. The dark theme can be used as:

- optional theme toggle later;
- hero/cover visual inspiration;
- color source for accents and cards;
- selected sections like evidence highlights or technical archive panels.

Initial implementation recommendation:

- start with a clean static white/wiki layout;
- design dark-mode tokens from the black references at the same time;
- keep both themes structurally identical;
- avoid building two separate sites.

---

## 4. Visual system

### 4.1 Colors

Light theme:

- background: warm off-white / light gray;
- text: graphite / near-black;
- panels: white with thin borders;
- accent: muted teal / blue-green;
- warning/limitations: muted amber or gray, not aggressive red.

Dark theme:

- background: near-black navy / charcoal;
- panels: dark slate;
- text: soft white / pale gray;
- accent: restrained teal/cyan;
- borders: thin low-contrast blue-gray.

Important: no neon cyberpunk overload.

### 4.2 Typography

The generated references showed a good direction:

- large elegant title for `Sonata`;
- calm editorial headings;
- readable body text;
- monospaced labels only for metadata, paths, evidence IDs, logs, and small technical tags.

We can use a similar feeling, but should choose web-safe or easily bundled fonts later.

### 4.3 Layout

Recommended page structure:

1. Header / project status strip.
2. Large `Sonata` title.
3. Short boundary statement: what is public, what remains private.
4. Metadata / project status block.
5. Documentation map.
6. Evidence highlights.
7. Limitations block.
8. How to read this dossier.
9. Footer with integrity note.

---

## 5. Components to design first

Keep the first version small.

Required components:

- sidebar or top navigation;
- document cards;
- metadata panel;
- “What Sonata is / is not” block;
- evidence highlight card;
- limitation card;
- documentation map card;
- reference thumbnail gallery for internal design work.

Optional later:

- theme toggle;
- animated section transitions;
- interactive publication timeline;
- diagram zoom viewer.

---

## 6. Design rules

Do:

- make it look like documentation;
- show limitations early;
- use real evidence only;
- keep diagrams simple;
- keep typography calm;
- use cards and tables for clarity.

Do not:

- copy generated mockups exactly;
- fake benchmark comparisons;
- imply product readiness;
- use “revolution” / “breakthrough” style language;
- overload the page with decorative AI imagery;
- make the landing look like a fundraising pitch.

---

## 7. Immediate decision

The first implementation should be:

> A portable static landing with a **white wiki-style default theme**, designed with a future **dark technical theme** in mind.

Dark reference colors can be borrowed for accents and later theme tokens. The visual identity should remain sober, technical, and document-first.

---

## 8. Next steps

- Export/copy the three generated reference images into `assets/references/`.
- Create a minimal `index.html` using the white wiki layout.
- Add CSS variables for light and dark theme tokens.
- Build the first documentation-map section.
- Keep all content public-safe and evidence-based.
