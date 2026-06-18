# Autograd + Mamba Integration

**Document:** 02 of 10  
**Status:** Public Evidence (L3)  
**Source reference:** Capability Map 2026-06-02, benchmark_phase20.md, TinyStories BPE live run 2026-06-18

---

## Why state-space sequence layers were used

Mamba-style state-space models (SSMs) offer O(1) memory scaling with respect to sequence length, unlike quadratic self-attention. For a project targeting constrained hardware, this characteristic makes long-context experiments feasible within limited VRAM. Sonata integrated a Mamba-style recurrent/state-space layer as an experimental alternative to attention-based sequence modeling.

## What integration with autograd means

Integrating a sequence module into a custom autograd engine requires:

- Defining forward and backward passes for the SSM scan operation
- Ensuring gradient flow through the state recurrence
- Maintaining checkpoint compatibility (serializing SSM parameters)
- Preserving GPU execution discipline (no CPU fallback during scan operations)
- Supporting mixed-precision paths

This is substantially harder than running a standalone forward pass. The module participates in the full training loop — gradient computation, optimizer updates, checkpointing, and stability management.

## Where instability appeared

During stacked Mamba-style scaling experiments with direct parameterization of the state transition, training diverged within approximately 100 steps under higher learning rates. The divergence manifested as activation explosion to NaN values.

The cause was identified as the optimizer pushing the state transition parameter into a regime where the discrete system becomes expanding rather than contracting. In a discrete state-space model:

$$h_t = \bar{A} h_{t-1} + \bar{B} x_t, \quad \bar{A} = \exp(\Delta \cdot A)$$

For asymptotic stability, the discrete transition eigenvalues must remain within the unit circle ($|\bar{A}| < 1$). With direct parameterization, the optimizer can push $A$ above zero, causing $|\bar{A}| > 1$.

## Constraints used to stabilize observed runs

The current implementation applies a post-step constraint on the state transition parameter for the directly-parameterized path:

- A strict upper bound is enforced on the parameter to maintain contraction
- FPU exception masking prevents numerical issues at the boundary
- Training proceeds stably with monotonically decreasing loss past the previously divergent step

This is presented as an implementation-level training integration result, not as a universal theoretical claim.

## What remains unproven

- The constraint approach has not been tested across diverse model scales
- No evidence that this constraint generalizes beyond the specific training configuration
- The interaction with alternative parameterizations (e.g., log-space) was not explored in the same controlled experiment
- Long training runs beyond early stabilization are not yet documented

## Evidence available

- Training divergence was reproducible and documented within the project's internal records
- Post-constraint training runs show stable convergence past the previous failure point
- Test execution logs confirm that Mamba-related tests (forward, backward, training integration) pass in the current implementation

This section will be updated as additional evidence is collected.
