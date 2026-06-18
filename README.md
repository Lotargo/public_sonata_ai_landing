# Sonata AI: A Low-Level Research Platform — Public Evidence Dossier

**Sonata** is a private, closed-source research platform that implements a complete tensor computation, automatic differentiation, and neural network training runtime entirely from scratch — not as a wrapper around existing frameworks, but as a ground-up system built in **Free Pascal**, accelerated with **x86-64 Assembly** and a **CUDA C++ GPU backend**. This repository is not the source code; it is a curated public evidence dossier — a portable technical journal documenting selected experimental results, architectural decisions, benchmark data, and validated subsystems.

## Why This Matters

Most contemporary AI research operates within high-level Python ecosystems (PyTorch, JAX, TensorFlow) that abstract away memory management, hardware dispatch, and gradient graph construction. Sonata occupies a different point in the design space: a self-contained runtime where every layer — from tensor layout and autograd graph traversal to GPU kernel invocation and model serialization — is explicitly owned and instrumented. This approach yields unusual visibility into system behaviour and creates different trade-offs than framework-based development.

The dossier is structured for **technically competent readers** — engineers and researchers who may be sceptical of claims made without source access, and who value precise, evidence-supported documentation over narrative promises.

## Key Findings

- **GPU execution is validated** — MatMul 256×256×256 completes in 9 ms (CPU: 63 ms), Conv2D in 1 ms (CPU: 33 ms). Zero CPU fallback in validated configurations.
- **End-to-end training is operational** — A 2-layer Mamba-style language model (182K parameters) trains on TinyStories BPE at approximately 6,800 tok/s sustained, GPU-resident with zero host offload.
- **Benchmark correction published** — An earlier inflated result (7,676 tok/s) was identified as a memory leak artefact, diagnosed, fixed, and replaced with a lower but accurate stable measurement (5,659 tok/s). The correction is documented as a trust-building artefact in [`docs/04_benchmark_correction_stability.md`](docs/04_benchmark_correction_stability.md).
- **INT8 quantisation is validated** — Mean squared error as low as 0.000013, cosine similarity 0.999984, with 2.1× memory compression over FP32.
- **Mamba-style state-space model integrated** — A fully differentiable SSM layer operates within the custom autograd graph, with gradient flow, checkpointing, and numerical stability corrections.
- **Symbolic-control bridge (Logos)** — Validated in narrow experiments: contradiction detection, axiom-guided penalty terms, and guarded evolutionary mutation.
- **Transport protocol (LTP)** — Message serialisation, CRC-based integrity verification, and chunked transfer for distributed node communication.

All measurements were conducted on a single laptop-class system (Intel Core i7-10750H, NVIDIA RTX 2070 Super Mobile, 8 GB VRAM, 32 GB RAM). This hardware-constrained context is integral to interpreting the results.

## Repository Structure

```
├── docs/               # 10 technical dossier documents (00–10)
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
├── data/               # Machine-readable evidence matrices
│   ├── public_claims_matrix.json      # 9 claims with evidence & limitations
│   ├── public_benchmark_summary.json  # 8 benchmarks with configurations
│   └── public_limitations_matrix.json # 14 limitations across 6 categories
├── assets/             # SVG diagrams, plots, and generator
│   ├── diagrams/       # Architecture, boundary, and flow diagrams
│   ├── plots/          # Throughput, VRAM, H2D, and validation plots
│   └── generate_public_assets.py      # Reproducible asset pipeline
├── index.html          # Wiki-style dossier landing page
├── pages/              # Future static HTML pages
├── styles/             # CSS resources
└── scripts/            # JavaScript resources
```

## What This Repository Is Not

- Not the Sonata source code — the runtime remains closed.
- Not a product launch or commercial offering.
- Not a claim of production readiness.
- Not a fundraising pitch or startup deck.

The dossier is explicitly scoped as a **laboratory record**: selected results from a private research platform, published with limitations placed alongside achievements as first-class content.

## Navigating the Dossier

For readers who prefer a structured entry point:

1. **Start with** [`docs/00_front_matter.md`](docs/00_front_matter.md) — scope, hardware context, and limitation statement.
2. **Architecture** → [`docs/01_architecture_overview.md`](docs/01_architecture_overview.md) and the [`assets/diagrams/layered_architecture.svg`](assets/diagrams/layered_architecture.svg).
3. **Key results** → [`docs/03_training_laboratory_results.md`](docs/03_training_laboratory_results.md) and [`docs/05_gpu_heterogeneous_execution.md`](docs/05_gpu_heterogeneous_execution.md).
4. **Evidence audit** → [`docs/10_evidence_index.md`](docs/10_evidence_index.md) for the complete registry of 24 artefacts (E01–E24).
5. **Machine-readable summary** → [`data/public_claims_matrix.json`](data/public_claims_matrix.json) and [`data/public_limitations_matrix.json`](data/public_limitations_matrix.json).

## Asset Pipeline

Diagrams and plots are SVG-first. To regenerate all visual assets:

```bash
python assets/generate_public_assets.py
```

Output is written to `assets/diagrams/*.svg` and `assets/plots/*.svg`. Style conventions are documented in [`assets/ASSET_STYLE_GUIDE.md`](assets/ASSET_STYLE_GUIDE.md).

## Licence and Use

This repository contains public documentation and evidence artefacts only. No proprietary Sonata source code is included. Refer to individual files for their respective licence terms where applicable.
