# Quantization Evidence: INT8 and Future INT4 Direction

**Document:** 06 of 10  
**Status:** Public Evidence (L3/L4)  
**Source reference:** benchmark_phase20.md, TinyStories BPE live run 2026-06-18

---

## INT8 summary

Sonata implements an INT8 GPU quantization path that reduces model memory footprint while maintaining numerical fidelity. The quantization uses per-row dynamic scaling for activations and per-column static scaling for weights, with cuBLAS INT8 tensor core GEMM for the matrix multiplication and a custom dequantization kernel.

## Validation metrics

All INT8 validation tests passed with high numerical fidelity:

| Test | Result | Threshold | Status |
|------|--------|-----------|--------|
| GPU INT8 MatMul correctness | MSE: 0.000013, Cosine: 0.999984 | MSE ≤ 0.01, Cosine ≥ 0.99 | PASS |
| Tensor evaluate GPU dispatch | MSE: 0.000035, Cosine: 0.999980 | MSE ≤ 0.01, Cosine ≥ 0.99 | PASS |
| GPU vs CPU INT8 parity | MSE: 0.000495 | MSE ≤ 0.001 | PASS |
| INT8 serialization round-trip | MSE: 0.000002 | MSE ≤ 0.01 | PASS |
| Large matrix stress test (512x1024) | MSE: 0.000220, Cosine: 0.999985 | MSE ≤ 0.05, Cosine ≥ 0.98 | PASS |
| Autograd with frozen weights | Weight grad = 0.0, Bias grad = 0.23 | Weight grad = 0.0, Bias > 0.0 | PASS |

## Memory footprint

INT8 weights measured at **2.1x smaller** than the FP32 baseline. The raw data compression is 4x (1 byte vs 4 bytes per weight), but total model-level savings include quantization scale overhead and internal bookkeeping, resulting in the measured 2.1x reduction.

## Speed behavior

On the current TinyStories BPE sustained training (small 182K-parameter model, Batch=8), INT8 and FP32 exhibit similar throughput (~7,000-8,500 tok/s). In peak micro-benchmark conditions (Batch=320), both precisions reach ~18,000 tok/s. This is expected because:

- The model is small enough that compute is not the bottleneck for either precision
- The Mamba training memory footprint is modest at profile-default batch sizes
- INT8's benefit is primarily in weight memory compression, not raw throughput, at this model scale

On larger models where weight memory dominates, INT8 would be expected to show a throughput advantage by enabling larger batch sizes within the same VRAM budget.

**Historical reference (Phase 20 synthetic benchmark, larger model):**

| Configuration | Throughput | VRAM |
|---------------|-----------|------|
| FP32, Batch=4, Seq=256 | ~5,750 tok/s | ~4.2 GB |
| INT8, Batch=8, Seq=256 | ~10,832 tok/s | ~6.9 GB |

The 1.88x speedup in that benchmark came from INT8's memory savings allowing batch size doubling within the 8 GB VRAM limit.

## Why small matrices do not always benefit

On small matrix configurations (e.g., 256x256), INT8 and FP32 exhibit similar per-iteration latency. The cuBLAS INT8 GEMM requires matrix dimensions that are multiples of 4 for tensor core operation, and small sizes do not fully utilize the INT8 compute path. In the current TinyStories model, the LM head shape (96x94) does not satisfy the multiples-of-4 requirement and remains in FP32.

## Future INT4 direction

INT4 block quantization is planned as a future phase. The expected benefits:

- ~8x theoretical weight compression vs FP32
- Enabling larger batch sizes and longer sequences on 8 GB VRAM
- Estimated throughput target: ~12,000+ tok/s on current hardware

This is a roadmap direction, not a completed result. INT4 quantization has not been validated or benchmarked.

## Important caveats

- INT8 performance on this hardware is not yet production-trustworthy for all configurations; a speed benchmark assertion test remains below target threshold for small matrix sizes
- The main benefit currently comes from VRAM savings enabling larger batches, not from raw INT8 compute speed
- Quantization quality has been validated on specific test configurations but not across diverse model architectures and datasets
