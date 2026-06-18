# Evidence Index

**Document:** 10 of 10  
**Status:** Public Dossier (L3/L4)

---

This index centralizes the public evidence references for claims made throughout this dossier. Each entry maps a claim to its evidence source, type, and known limitations.

## Evidence artifacts

| ID | Artifact | Type | Source | Documents |
|----|----------|------|--------|-----------|
| E01 | GPU/CPU MatMul benchmark (256x256x256) | Raw metric | test_runner execution | 01, 05 |
| E02 | Conv2D benchmark (4x8x16x16) | Raw metric | test_runner execution | 01, 05 |
| E03 | TinyStories BPE sustained training (~6,800 tok/s, 30 steps) | Raw metric | Live run 2026-06-18 | 03 |
| E04 | INT8 validation metrics (MSE, cosine similarity) | Test summary | benchmark_phase20.md | 06 |
| E05 | INT8 memory compression ratio (2.1x) | Raw metric | benchmark_phase20.md | 06 |
| E06 | Zero CPU fallback across sustained training run | Test pass/fail | Live run 2026-06-18 | 03 |
| E07 | Benchmark correction (7,676 → 5,659 tok/s, Phase 20) | Narrative + metrics | benchmark_phase20.md | 04 |
| E08 | INT8 stress benchmark (10,832 tok/s at Batch=8, Phase 20) | Raw metric | benchmark_phase20.md | 06 |
| E09 | Checkpoint round-trip pass | Test pass/fail | Capability Map 2026-06-02 | 01 |
| E10 | Training resume with matching loss | Test pass/fail | Capability Map 2026-06-02 | 01, 03 |
| E11 | GPU-only checkpoint pass | Test pass/fail | Capability Map 2026-06-02 | 01 |
| E12 | Phase 20 throughput baseline (~5,700 tok/s) | Raw metric | benchmark_phase20.md | 03, 04 |
| E13 | Contradiction detection in reflection mode | Test pass/fail | Capability Map 2026-06-02 | 07 |
| E14 | Axiom-guided penalty test pass | Test pass/fail | Capability Map 2026-06-02 | 07 |
| E15 | Guarded evolution test pass | Test pass/fail | Capability Map 2026-06-02 | 07 |
| E16 | LTP message serialization tests pass | Test pass/fail | Capability Map 2026-06-02 | 08 |
| E17 | CRC mismatch detection pass | Test pass/fail | Capability Map 2026-06-02 | 08 |
| E18 | LTP binary chunk benchmark | Raw metric | Capability Map 2026-06-02 | 08 |
| E19 | CUDA initialization and device query pass | Test pass/fail | Capability Map 2026-06-02 | 05 |
| E20 | GPU memory allocation and transfer tests pass | Test pass/fail | Capability Map 2026-06-02 | 05 |
| E21 | Self-play fitness change (5.98 → 6.10) | Raw metric | Capability Map 2026-06-02 | 01 |
| E22 | Evolution competition with latency measurement | Raw metric | Capability Map 2026-06-02 | 01 |
| E23 | TinyStories INT8 peak micro-benchmark (17,803 tok/s at Batch=320) | Raw metric | Live run 2026-06-18 | 03, 06 |
| E24 | TinyStories sustained training throughput (6,802 tok/s, 30 steps) | Raw metric | Live run 2026-06-18 | 03 |

## Document-to-claim matrix

| Claim | Primary documents | Supporting evidence | Limitation references |
|-------|------------------|-------------------|---------------------|
| Sonata is a working low-level research platform | 01 | E01, E02, E09, E10, E11, E21, E22 | 09 |
| GPU execution is validated | 05 | E01, E02, E19, E20 | 09 — mobile GPU, 8 GB VRAM |
| Training path exists and runs | 03 | E03, E06, E09, E10, E12, E23, E24 | 09 — laptop hardware, limited scale |
| Benchmark correction demonstrates stability-first discipline | 04 | E07 | 09 — single hardware context |
| INT8 quantization is validated with high fidelity | 06 | E04, E05, E08, E23 | 09 — performance benefit is model-scale dependent |
| Mamba-style sequence modeling is integrated | 02 | E03 (training context) | 02 — stability constraint is implementation-specific |
| Logos symbolic-control bridge exists | 07 | E13, E14, E15 | 09 — partially fragile, not turnkey |
| LTP transport foundations exist | 08 | E16, E17, E18 | 09 — no security layer |

## Evidence quality notes

- All test pass/fail evidence (E09–E20) comes from a single execution of the project's integration test runner
- Raw metrics (E01–E08) are environment-specific and may not generalize
- No evidence in this index has been independently verified by a third party
- All evidence is self-reported from the private repository
