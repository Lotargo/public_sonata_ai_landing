# Sonata Landing Sprint Plan

**Status:** active sprint plan  
**Location:** `public_sonata_landing/`  
**Purpose:** track creation of the portable Sonata public landing package.  
**Scope:** planning, layout, static page skeleton, assets, public-safe content, and export readiness.

---

## 0. Sprint rule

This document is a checklist and coordination map. It should stay short.

Detailed reasoning belongs in the supporting documents listed below.

---

## 1. Supporting documents

| Document | Purpose | Status |
|---|---|---|
| `docs_tmp/PUBLIC_EVIDENCE_AUDIT_TEMPLATE.md` | Evidence rules, public-safe claims, disclosure levels | Ready |
| `docs_tmp/PUBLIC_DOCUMENTATION_MAP_APPENDIX.md` | Publication map and dossier structure | Ready |
| `docs_tmp/LANDING_DESIGN_BRIEF.md` | Visual direction, references, light/dark design decision | Ready |
| `README.md` | Directory purpose and public package rule | Ready |

---

## 2. Current directory target

```text
public_sonata_landing/
├── index.html
├── docs/
├── docs_tmp/
├── pages/
├── assets/
│   ├── references/
│   ├── diagrams/
│   ├── plots/
│   ├── screenshots/
│   └── thumbnails/
├── data/
├── styles/
└── scripts/
```

Notes:

- `docs_tmp/` is temporary planning storage.
- `docs/` will contain final public-safe dossier pages.
- `assets/references/` should hold generated design references after export.
- No private code or implementation recipes go into this directory.

---

## 3. Sprint goals

### Goal A — Prepare landing skeleton

- [ ] Create `index.html`.
- [ ] Create `styles/main.css`.
- [ ] Create optional `scripts/main.js` only if needed.
- [ ] Add CSS variables for light and dark themes.
- [ ] Use white wiki-style layout as default.
- [ ] Borrow dark archive colors as future dark-theme tokens.

### Goal B — Prepare design assets

- [ ] Create `assets/references/`.
- [ ] Add three generated reference images.
- [ ] Add short `assets/references/README.md` explaining that references are inspiration only.
- [ ] Prepare first public-safe diagrams later.

### Goal C — Prepare landing content

- [ ] Add boundary hero text.
- [ ] Add “What Sonata is / is not”.
- [ ] Add documentation map section.
- [ ] Add evidence highlights section.
- [ ] Add limitations section.
- [ ] Add “How to read this dossier”.
- [ ] Add footer integrity note.

### Goal D — Prepare dossier pages

- [ ] Draft `docs/00_front_matter.md`.
- [ ] Draft `docs/01_architecture_overview.md`.
- [ ] Draft `docs/02_autograd_mamba_integration.md`.
- [ ] Draft `docs/03_training_laboratory_results.md`.
- [ ] Draft `docs/04_benchmark_correction_stability.md`.
- [ ] Draft `docs/09_limitations_open_problems.md`.
- [ ] Draft `docs/10_evidence_index.md`.

### Goal E — Public-safety check

- [ ] Verify no private source code is included.
- [ ] Verify no secrets or local paths are included.
- [ ] Verify no exact implementation recipe is exposed.
- [ ] Verify every strong claim links to evidence or a limitation note.
- [ ] Verify no hype terms are used.

### Goal F — Export readiness

- [ ] Ensure landing works as static files.
- [ ] Ensure relative links work after copying to another repository.
- [ ] Ensure images/assets are local and public-safe.
- [ ] Prepare copy instructions for main portfolio integration.

---

## 4. Current status

| Area | Status | Notes |
|---|---|---|
| Evidence planning | Done | See evidence audit template |
| Publication map | Done | See documentation map appendix |
| Design direction | Done | See landing design brief |
| Directory skeleton | In progress | Core folders exist; `assets/references/` still needed |
| Static landing implementation | Not started | Next main task |
| Final public dossier pages | Not started | Start after skeleton |
| Public-safety pass | Not started | Run before export |

---

## 5. Suggested task order

1. Add `assets/references/` and place generated references.
2. Build minimal `index.html` with static sections.
3. Build `styles/main.css` with light theme and dark tokens.
4. Add first content blocks from existing planning docs.
5. Create first final dossier pages in `docs/`.
6. Run public-safety check.
7. Prepare package for portfolio integration.

---

## 6. Definition of done

The sprint is complete when:

- `public_sonata_landing/index.html` opens locally without build tools;
- the landing uses public-safe content only;
- the visual style follows the design brief;
- the dossier links point to local public-safe documents;
- the package can be copied into another public portfolio repository;
- the private Sonata repository remains undisclosed.
