# Appendix: Sonata Public Documentation Map

**Status:** planning appendix  
**Parent document:** `PUBLIC_EVIDENCE_AUDIT_TEMPLATE.md`  
**Purpose:** define the publication map, document structure, illustration plan, and portable landing-page strategy for public-safe Sonata disclosure.  
**Audience:** technically competent readers, reviewers, researchers, engineers, and serious collaborators. This is intentionally not optimized for casual investors or hype-driven readers.

---

## 0. Why this appendix exists

Sonata is a private closed-source research project. The public materials must not expose the repository, source code, or implementation recipes. At the same time, the project needs a credible evidence base: not marketing promises, but documented architecture, logs, limitations, and selected technical results.

This appendix defines a publication map: which public documents should exist, how they should relate to one another, what illustrations must be created separately, and how the final package should be wrapped into a portable landing page.

The intended output is closer to a technical journal issue or research dossier than a startup pitch deck.

---

## 1. Publication philosophy

The public package should deliberately filter its audience.

It should be readable for people who understand at least part of the following:

- low-level runtime design;
- tensor/autograd systems;
- GPU execution and memory constraints;
- sequence modeling and Mamba-style state-space layers;
- quantization and hardware-aware optimization;
- checkpointing, training loops, and failure analysis;
- experimental research documentation.

It should not be optimized for readers who expect a simple promise like “this will change everything in two months.”

Public stance:

> Sonata is a closed-source laboratory AI research platform with selected public evidence. The public documentation exists to show what has been built, what has been tested, what failed, what remains limited, and why the work is technically interesting without exposing the private implementation.

---

## 2. Anti-hype rules for the public package

Public documents must avoid dramatic claims. The strongest posture is calm, technical, and evidence-first.

Do not use:

- “revolution”;
- “breakthrough”;
- “discovery”;
- “AGI”;
- “universal AI”;
- “solved training”;
- “production-ready” unless the exact subsystem is demonstrably hardened;
- “guaranteed” unless the guarantee is formal, narrow, and proven.

Preferred wording:

- “laboratory result”;
- “engineering result”;
- “implementation finding”;
- “validated subsystem”;
- “experimental architecture”;
- “hardware-constrained training run”;
- “public-safe evidence pack”;
- “closed-source research platform.”

---

## 3. Public documentation map

The public documentation should be assembled as a structured technical journal. Each section can be created as a separate Markdown/HTML page and later linked from the portable landing.

### 3.1 Front Matter

**Document:** `00_front_matter.md`  
**Purpose:** set expectations and prevent misreading.

Content:

- what Sonata is;
- what Sonata is not;
- why the code remains closed;
- what evidence is public;
- how to read the dossier;
- hardware and resource context;
- explicit limitation statement.

Target tone:

> This dossier is not a product launch and not a funding promise. It is a technical record of selected results from a private research platform.

Illustrations to create:

- one-page “project boundary” diagram;
- public/private disclosure boundary diagram.

---

### 3.2 Architecture Overview

**Document:** `01_architecture_overview.md`  
**Source base:** `v1/docs/design/Sonata_Design_Book_v1.md`, `README.md`, `docs/SONATA_CAPABILITY_MAP_2026-06-02.md`

Purpose:

- explain Sonata as a compact runtime + training/inference research stack;
- show the high-level system layers without implementation details;
- explain why the project is not “just another wrapper.”

Sections:

- project boundary;
- runtime layer;
- tensor/autograd layer;
- model/checkpoint layer;
- GPU/CPU backend layer;
- training/inference experiments;
- symbolic-control / Logos layer;
- transport foundations.

Illustrations to create:

- layered architecture diagram;
- public-safe component map;
- “closed code / public evidence” split.

Disclosure level:

- L2/L3.

---

### 3.3 Autograd + Mamba Integration Note

**Document:** `02_autograd_mamba_integration.md`  
**Source base:** `README.md`, Mamba-related docs/tests/logs to be located in next audit pass.

Purpose:

- explain why integrating a Mamba-style layer into a custom autograd/training path matters;
- distinguish a forward operator demo from a trainable module;
- show how this became part of training stability work.

Sections:

- why state-space sequence layers were used;
- what “integration with autograd” means at a high level;
- where instability appeared;
- what constraints were used to stabilize observed runs;
- what remains unproven;
- what evidence is available.

Important wording:

> This is presented as an implementation-level training integration result, not as a universal theoretical claim.

Illustrations to create:

- forward/backward flow diagram;
- training-loop placement diagram;
- stability boundary sketch: stable/unstable transition regime;
- loss curve if a clean public-safe run is available.

Disclosure level:

- L3 after exact evidence references are collected.

---

### 3.4 Training Runs Under Laptop-Class Constraints

**Document:** `03_training_laboratory_results.md`  
**Source base:** `v1/docs/benchmark_phase20.md`, `benchmark_phase20.log`, `v1/benchmark_phase20.log`, future training logs.

Purpose:

- describe training results honestly;
- make the hardware context central rather than hidden;
- explain why results are encouraging but still laboratory-level.

Sections:

- hardware context: laptop + mobile RTX 2070 Super;
- VRAM, thermals, and time limits;
- what training path currently demonstrates;
- observed throughput and H2D traffic;
- CPU fallback discipline;
- loss behavior if available;
- failure modes and fixes;
- why this does not imply broad model quality.

Public-safe message:

> The current results are encouraging because they were obtained under constrained hardware, but they remain laboratory results. The project demonstrates trainability and system behavior, not a finished public model.

Illustrations to create:

- hardware constraint diagram;
- throughput table;
- VRAM ceiling chart;
- “what this proves / what this does not prove” panel.

Disclosure level:

- L3/L4 if raw logs and configuration are included.

---

### 3.5 Benchmark Correction and Stability-First Engineering

**Document:** `04_benchmark_correction_stability.md`  
**Source base:** `v1/docs/benchmark_phase20.md`

Purpose:

- show that the project does not chase inflated results;
- explain the correction from unstable higher throughput to stable lower throughput;
- use the failure analysis as credibility evidence.

Sections:

- initial faster result;
- memory leaks / VRAM overflow interpretation;
- post-fix stable result;
- why lower stable throughput is more valuable;
- lessons for future benchmarks.

Illustrations to create:

- before/after benchmark chart;
- stability vs throughput diagram;
- memory safety timeline.

Disclosure level:

- L4 candidate.

Why it matters:

> This may be one of the strongest public trust-building documents because it shows correction, not self-promotion.

---

### 3.6 GPU and Heterogeneous Execution Evidence

**Document:** `05_gpu_heterogeneous_execution.md`  
**Source base:** `docs/SONATA_CAPABILITY_MAP_2026-06-02.md`, benchmark logs.

Purpose:

- show that GPU execution is real and validated in narrow tests;
- explain CPU/GPU split and fallback discipline at a high level;
- avoid exposing backend code.

Sections:

- environment;
- CUDA initialization;
- GPU memory tests;
- MatMul and Conv2D evidence;
- fallback behavior;
- checkpoint / GPU-only discipline;
- current limitations.

Illustrations to create:

- backend dispatch diagram;
- CPU vs GPU table;
- fallback ladder diagram.

Disclosure level:

- L3.

---

### 3.7 Quantization Evidence: INT8 and Future INT4 Direction

**Document:** `06_quantization_evidence.md`  
**Source base:** `v1/docs/benchmark_phase20.md`

Purpose:

- present INT8 correctness/parity/memory evidence;
- explain why speedup comes from fitting larger batches under VRAM limits;
- separate completed evidence from future INT4 work.

Sections:

- INT8 mathematical summary without implementation recipe;
- validation metrics;
- memory footprint;
- speed behavior;
- why small matrices do not always benefit;
- future INT4 direction as roadmap, not result.

Illustrations to create:

- INT8 validation table;
- memory compression chart;
- batch-size feasibility chart;
- future roadmap diagram.

Disclosure level:

- L3/L4.

---

### 3.8 Logos / Symbolic-Control Bridge

**Document:** `07_logos_symbolic_control.md`  
**Source base:** `docs/SONATA_CAPABILITY_MAP_2026-06-02.md`, future Logos-specific docs.

Purpose:

- explain Logos as an early symbolic-control / contradiction-checking layer;
- avoid mature reasoning claims;
- show how it participates in penalties, reflection, and guarded evolution experiments.

Sections:

- what Logos is in the public narrative;
- contradiction traces;
- axiom-guided penalties;
- guarded evolution;
- current fragility;
- missing hardening and packaging.

Illustrations to create:

- neural/symbolic control loop diagram;
- contradiction penalty flow;
- maturity ladder: current / next / not claimed.

Disclosure level:

- L2/L3.

---

### 3.9 LTP / Transport Foundations

**Document:** `08_ltp_transport_foundations.md`  
**Source base:** `docs/SONATA_CAPABILITY_MAP_2026-06-02.md`, `README.md`, LTP docs after audit.

Purpose:

- describe transport/integrity foundations;
- avoid claiming secure distributed operations;
- show tested protocol pieces.

Sections:

- what LTP is;
- tested message types;
- chunk transfer;
- CRC mismatch detection;
- current security limitations;
- what must be added for trust/security.

Illustrations to create:

- protocol frame sketch;
- chunk transfer diagram;
- transport vs security boundary chart.

Disclosure level:

- L3.

---

### 3.10 Limitations and Open Problems

**Document:** `09_limitations_open_problems.md`  
**Source base:** `PUBLIC_EVIDENCE_AUDIT_TEMPLATE.md`, `docs/SONATA_CAPABILITY_MAP_2026-06-02.md`, benchmark docs.

Purpose:

- make limitations a first-class part of the public dossier;
- reduce misinterpretation;
- filter hype-driven readers.

Sections:

- laptop-class hardware;
- mobile GPU limits;
- VRAM ceiling;
- thermals;
- time constraints;
- incomplete training scale;
- incomplete security/trust stack;
- immature packaging for some subsystems;
- no claim of near-term public product readiness.

Illustrations to create:

- limitation matrix;
- “validated / partial / not claimed” table;
- risk register.

Disclosure level:

- L4.

---

### 3.11 Evidence Index

**Document:** `10_evidence_index.md`  
**Source base:** all public-safe logs, tables, screenshots, generated images.

Purpose:

- centralize the evidence;
- let technical readers verify the public claims without seeing source code.

Sections:

- benchmark logs;
- environment summaries;
- test summaries;
- screenshots;
- generated plots;
- limitation notes;
- document-to-claim matrix.

Illustrations to create:

- evidence graph: claim -> artifact -> limitation.

Disclosure level:

- L3/L4.

---

## 4. Journal-style structure

The final public package should feel like a technical journal issue:

```text
Sonata Public Technical Dossier
├── 00 Front Matter
├── 01 Architecture Overview
├── 02 Autograd + Mamba Integration
├── 03 Training Runs Under Laptop-Class Constraints
├── 04 Benchmark Correction and Stability-First Engineering
├── 05 GPU and Heterogeneous Execution Evidence
├── 06 Quantization Evidence
├── 07 Logos / Symbolic-Control Bridge
├── 08 LTP / Transport Foundations
├── 09 Limitations and Open Problems
└── 10 Evidence Index
```

Each document should be readable alone, but the landing page should present them as a connected publication map.

---

## 5. Illustration plan

Illustrations should be created separately and treated as part of the evidence/publication package.

Recommended directory:

```text
public_sonata_landing/
├── assets/
│   ├── diagrams/
│   ├── plots/
│   ├── screenshots/
│   └── thumbnails/
```

Required first illustrations:

| Illustration | Purpose | Source |
|---|---|---|
| Project boundary diagram | Prevent overclaiming | Front matter |
| Public/private disclosure boundary | Explain closed-source evidence model | Front matter |
| Layered architecture | Explain system without source | Architecture overview |
| Autograd + Mamba flow | Show training integration | Mamba note |
| Hardware constraint panel | Explain laptop/mobile GPU limits | Training results |
| Stability vs throughput chart | Show benchmark correction | Benchmark correction |
| CPU/GPU backend ladder | Show heterogeneous execution | GPU evidence |
| INT8 validation table/plot | Show quantization evidence | Quantization doc |
| Logos control loop | Show symbolic-control bridge | Logos doc |
| Claim -> evidence graph | Connect claims to artifacts | Evidence index |

Style:

- sober;
- technical;
- low-hype;
- dark or neutral theme;
- diagrams first, decoration second;
- every chart must include context and caveats.

---

## 6. Portable landing directory plan

We should not build GitHub Pages directly inside the private Sonata repository.

Reason:

- the repository is private;
- the source code will not be disclosed;
- publication artifacts must be portable;
- the landing should later be attached to the main portfolio/vitrine site;
- the same package should be reusable on GitHub Pages, static hosting, local preview, or a project showcase.

Create a new portable directory, likely inside the private repo first, then later copy/export only the safe public package:

```text
public_sonata_landing/
├── README.md
├── index.html
├── pages/
│   ├── 00_front_matter.html
│   ├── 01_architecture_overview.html
│   ├── 02_autograd_mamba_integration.html
│   ├── 03_training_laboratory_results.html
│   ├── 04_benchmark_correction_stability.html
│   ├── 05_gpu_heterogeneous_execution.html
│   ├── 06_quantization_evidence.html
│   ├── 07_logos_symbolic_control.html
│   ├── 08_ltp_transport_foundations.html
│   ├── 09_limitations_open_problems.html
│   └── 10_evidence_index.html
├── docs/
│   ├── 00_front_matter.md
│   ├── 01_architecture_overview.md
│   ├── 02_autograd_mamba_integration.md
│   ├── 03_training_laboratory_results.md
│   ├── 04_benchmark_correction_stability.md
│   ├── 05_gpu_heterogeneous_execution.md
│   ├── 06_quantization_evidence.md
│   ├── 07_logos_symbolic_control.md
│   ├── 08_ltp_transport_foundations.md
│   ├── 09_limitations_open_problems.md
│   └── 10_evidence_index.md
├── assets/
│   ├── diagrams/
│   ├── plots/
│   ├── screenshots/
│   └── thumbnails/
├── data/
│   ├── public_benchmark_summary.json
│   ├── public_claims_matrix.json
│   └── public_limitations_matrix.json
├── styles/
│   └── main.css
└── scripts/
    └── main.js
```

The directory must remain static-first:

- no backend;
- no private API calls;
- no dependency on private repo paths;
- no raw source links;
- no secrets;
- no build system required unless later needed.

Minimum viable version:

```text
public_sonata_landing/
├── index.html
├── docs/
├── assets/
└── styles/main.css
```

---

## 7. Landing page structure

The landing should not be a sales page. It should be a technical entrance to the dossier.

### Sections

1. **Hero / Boundary Statement**
   - one paragraph explaining Sonata as a closed-source laboratory platform;
   - no dramatic claims;
   - direct links to evidence sections.

2. **What is public / what remains private**
   - public: architecture summaries, logs, diagrams, limitations;
   - private: source code, implementation details, exact recipes.

3. **Publication Map**
   - journal-like cards for each document.

4. **Evidence Highlights**
   - GPU execution;
   - training path;
   - benchmark correction;
   - quantization;
   - symbolic-control bridge.

5. **Limitations First**
   - hardware;
   - time;
   - training scale;
   - immature subsystems.

6. **How to read this project**
   - for engineers;
   - for researchers;
   - for collaborators;
   - for non-technical readers: warning that this is intentionally technical.

7. **Integration into main portfolio**
   - link target from main vitrine;
   - project card summary;
   - screenshot thumbnail;
   - “read technical dossier” button.

---

## 8. Main portfolio integration plan

Later, the portable landing can be attached to the main portfolio/vitrine as one project module.

Main portfolio card draft:

> **Sonata** — closed-source low-level AI research platform with public-safe technical evidence: custom runtime, autograd/training experiments, GPU execution, quantization, benchmark correction notes, and documented limitations.

Buttons:

- `Read technical dossier`
- `View evidence index`
- `See limitations`

Do not add:

- “source code” button;
- public repository link;
- claims of finished product readiness;
- investor-focused promises.

---

## 9. Work plan

### Phase A — Audit and selection

- [ ] Continue repository documentation audit.
- [ ] Locate exact Mamba/autograd training documents and logs.
- [ ] Locate exact training result summaries and loss traces.
- [ ] Classify each candidate document as L0-L4.
- [ ] Mark unsafe files as internal-only.

### Phase B — Public dossier drafting

- [ ] Draft `00_front_matter.md`.
- [ ] Draft `01_architecture_overview.md`.
- [ ] Draft `02_autograd_mamba_integration.md`.
- [ ] Draft `03_training_laboratory_results.md`.
- [ ] Draft `04_benchmark_correction_stability.md`.
- [ ] Draft `09_limitations_open_problems.md` early, not last.
- [ ] Draft `10_evidence_index.md`.

### Phase C — Visual evidence

- [ ] Create public-safe diagrams.
- [ ] Generate plots only from validated public-safe metrics.
- [ ] Add caveats to every chart.
- [ ] Avoid decorative charts that imply more evidence than exists.

### Phase D — Portable landing

- [ ] Create `public_sonata_landing/`.
- [ ] Build static `index.html`.
- [ ] Add journal-style document navigation.
- [ ] Add styles and assets.
- [ ] Verify no private paths, code, or secrets are present.
- [ ] Export/copy to main portfolio repository when ready.

### Phase E — Main vitrine integration

- [ ] Add Sonata project card to main portfolio.
- [ ] Link to portable landing.
- [ ] Add thumbnail and technical summary.
- [ ] Keep the private repository disconnected from public routing.

---

## 10. Acceptance criteria

The public package is acceptable only if:

- a technical reader can understand what was built;
- a skeptical reader can see evidence and limitations;
- a casual hype-driven reader is not encouraged to expect impossible timelines;
- the private code remains private;
- no implementation recipe is exposed;
- every strong claim has an evidence pointer;
- every result has a caveat;
- the landing can be moved into another portfolio repository without depending on Sonata’s private repo.

---

## 11. Current decision

Proceed with a two-layer publication model:

1. **Internal private repo:** source code, detailed docs, raw research history, unsafe implementation details.
2. **Portable public landing package:** curated journal-style dossier, diagrams, selected logs, limitations, and evidence index.

This lets Sonata be publicly discussable without turning the private repository into the public artifact.
