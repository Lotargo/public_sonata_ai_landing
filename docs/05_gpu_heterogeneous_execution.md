# GPU and Heterogeneous Execution Evidence

**Document:** 05 of 10  
**Status:** Public Evidence (L3)  
**Source reference:** Capability Map 2026-06-02, TinyStories BPE live run 2026-06-18

---

## Environment

GPU execution was validated on a system with an NVIDIA GeForce RTX 2070 Super (8 GB VRAM, compute capability 7.5 / Turing). The GPU backend is implemented through a dynamically-loaded CUDA C++ shared library that interfaces with the main runtime via a Foreign Function Interface (FFI).

## CUDA initialization

CUDA initialization succeeded with correct device identification, driver version compatibility, and memory query. The runtime dynamically detects GPU availability and selects the execution backend accordingly.

## GPU memory tests

GPU memory allocation, deallocation, and host-to-device / device-to-host transfer operations passed validation. Memory pressure handling was tested with emergency allocator guard behavior confirmed at the VRAM ceiling boundary.

## MatMul evidence

Matrix multiplication on GPU was validated against CPU reference results:

| Configuration | CPU (multithreaded) | GPU (CUDA) |
|---------------|---------------------|------------|
| 256x256x256 | 63 ms | 9 ms |

GPU MatMul uses cuBLAS-backed execution with support for FP32, FP16 (Tensor Cores), and INT8 (Tensor Cores with cuBLAS INT8 GEMM) precision paths.

## Conv2D evidence

2D convolution was validated:

| Configuration | CPU (multithreaded) | GPU (CUDA kernel) |
|---------------|---------------------|-------------------|
| 4x8x16x16 | 33 ms | 1 ms |

The convolution operation uses a custom CUDA kernel with dynamic batch and channel processing.

## Fallback behavior

The hardware abstraction layer implements a multi-level dispatch chain:

```
GPU (CUDA) → Multithreaded CPU → Assembly SIMD → Pascal Reference
```

If the GPU driver is unavailable, a specific operation is unsupported, or memory pressure requires fallback, execution moves down the chain automatically. Fallback behavior was validated with zero execution errors or memory leaks during transition tests.

## Current limitations

- GPU backend requires NVIDIA hardware with CUDA support
- AMD GPU support uses an experimental Vulkan backend that is not yet validated at the same level
- Small matrix sizes (< 256) do not benefit from Tensor Cores
- The FP16 backward path is partially integrated; gradient accumulation remains FP32 for some operations
- No multi-GPU support
