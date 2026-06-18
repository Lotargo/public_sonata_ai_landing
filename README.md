# Sonata AI — Public Evidence Dossier

Sonata is a private research platform that implements a complete tensor computation, automatic differentiation, and neural network training runtime from scratch — not as a wrapper around existing frameworks, but as a ground-up system built in **Free Pascal**, accelerated with **x86-64 Assembly** and a **CUDA C++ GPU backend**.

This repository is not the source code. It is a curated public evidence dossier: a portable technical journal documenting selected experimental results, architectural decisions, benchmark data, and validated subsystems. The source code remains in a private repository and is not currently available for public access.

## Why This Exists

Most contemporary AI research operates within high-level Python ecosystems (PyTorch, JAX, TensorFlow) that abstract away memory management, hardware dispatch, and gradient graph construction. Sonata occupies a different point in the design space: a self-contained runtime where every layer — from tensor layout and autograd graph traversal to GPU kernel invocation and model serialization — is explicitly owned and instrumented.

This dossier is structured for technically competent readers — engineers and researchers who value precise, evidence-supported documentation over narrative promises. All measurements were conducted on a single laptop-class system (Intel Core i7-10750H, NVIDIA RTX 2070 Super Mobile, 8 GB VRAM, 32 GB RAM).

## Repository Layout

```
docs/
├── 00_front_matter.md                 Scope, hardware context, and limitation statement
├── 01_architecture_overview.md        System-level design and layered architecture
├── 02_autograd_mamba_integration.md   Custom autograd engine and SSM integration
├── 03_training_laboratory_results.md  End-to-end training benchmarks
├── 04_benchmark_correction_stability.md  Benchmark correction: inflated result, diagnosis, fix
├── 05_gpu_heterogeneous_execution.md  GPU kernel dispatch and heterogeneous compute
├── 06_quantization_evidence.md        INT8 quantization validation
├── 07_logos_symbolic_control.md       Symbolic-control bridge experiments
├── 08_ltp_transport_foundations.md    Transport framing and integrity foundations
├── 09_limitations_open_problems.md    Known limitations and open research questions
├── 10_evidence_index.md               Claim-to-evidence index
├── assets/                            SVG diagrams and plots
│   ├── diagrams/                      Architecture, boundary, and flow diagrams
│   └── plots/                         Throughput, VRAM, and validation plots
├── data/                              Machine-readable evidence matrices
│   ├── public_claims_matrix.json      9 claims with evidence and limitations
│   ├── public_benchmark_summary.json  8 benchmarks with configurations
│   └── public_limitations_matrix.json 14 limitations across 6 categories
└── index.html                         Public landing page
```

## Key Subsystems

**Tensor Runtime & Autograd** — Custom autograd engine operating on Pascal arrays with automatic differentiation through arbitrary computation graphs. Includes gradient checkpointing, numerical stability corrections, and seamless CPU/GPU tensor migration.

**GPU Execution** — CUDA C++ backend with custom kernel dispatch. MatMul 256×256×256 completes in 9 ms (CPU: 63 ms), Conv2D in 1 ms (CPU: 33 ms). Zero CPU fallback in validated configurations.

**Mamba-style SSM** — State-space model layer fully integrated into the custom autograd graph. A 2-layer Mamba-style language model (182K parameters) trains on TinyStories BPE at approximately 6,800 tok/s sustained, GPU-resident with zero host offload.

**INT8 Quantization** — Mean squared error as low as 0.000013, cosine similarity 0.999984, with 2.1× memory compression over FP32.

**Logos (Symbolic Control)** — Experimental bridge between symbolic logic and tensor computation. Validated in narrow experiments: contradiction detection, axiom-guided penalty terms, and guarded evolutionary mutation.

**LTP (Transport Framing & Integrity)** — Binary message serialization, CRC-based corruption detection, and chunked transfer for distributed node communication experiments. LTP is not presented as a secure networking layer.

## Navigating the Dossier

1. **Start with** [`docs/00_front_matter.md`](docs/00_front_matter.md) — defines scope, hardware context, and explicit limitation statement.
2. **Architecture** → [`docs/01_architecture_overview.md`](docs/01_architecture_overview.md) — layered design and subsystem relationships.
3. **Key results** → [`docs/03_training_laboratory_results.md`](docs/03_training_laboratory_results.md) and [`docs/05_gpu_heterogeneous_execution.md`](docs/05_gpu_heterogeneous_execution.md).
4. **Trust artifact** → [`docs/04_benchmark_correction_stability.md`](docs/04_benchmark_correction_stability.md) — an earlier inflated result was identified, diagnosed, fixed, and documented. The correction itself is evidence of methodology.
5. **Transport foundations** → [`docs/08_ltp_transport_foundations.md`](docs/08_ltp_transport_foundations.md) — documents LTP as framing and integrity infrastructure, not a secure distributed protocol.
6. **Evidence index** → [`docs/10_evidence_index.md`](docs/10_evidence_index.md) — maps claims to public evidence artifacts and limitations.
7. **Machine-readable data** → [`docs/data/public_claims_matrix.json`](docs/data/public_claims_matrix.json) and [`docs/data/public_limitations_matrix.json`](docs/data/public_limitations_matrix.json).

## What This Repository Is Not

- Not the Sonata source code — the runtime remains closed.
- Not a product launch or commercial offering.
- Not a claim of production readiness.
- Not a fundraising pitch or startup deck.

This is a laboratory record: selected results from a private research platform, published with limitations placed alongside achievements as first-class content.
