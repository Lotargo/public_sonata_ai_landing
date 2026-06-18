# LTP / Transport Foundations

**Document:** 08 of 10  
**Status:** Public Evidence (L3)  
**Source reference:** Capability Map 2026-06-02

---

## What LTP is

The Low-Throughput Protocol (LTP) is Sonata's transport and integrity layer for distributed node communication. It defines message serialization formats, chunk transfer mechanics, and CRC-based integrity verification. LTP was originally designed to support Hub/Body communication in a distributed swarm architecture.

## Tested message types

The following message types passed serialization and deserialization tests:

- **Handshake:** Connection initialization between nodes
- **Hello:** Node identification and capability advertisement
- **Task:** Work unit description and dispatch
- **Result:** Completed task output delivery
- **Chunk request / response:** Block-level data transfer
- **Error:** Error condition reporting

All message serialization/deserialization round-trips passed validation.

## Chunk transfer

Binary chunk serialization was benchmarked:

- 1 MiB chunk serialization: near-zero measurable latency
- Wire size: 1,048,610 bytes per chunk
- Transfer format uses fixed binary headers with raw byte bodies (no Base64/JSON encoding)

## CRC mismatch detection

CRC-based integrity verification passed tests. Mismatched chunks were correctly detected and reported. This provides transport-level integrity protection but is not a substitute for cryptographic authentication or encryption.

## Current security limitations

LTP currently provides:

- ✅ Message serialization and deserialization
- ✅ Chunk transfer with CRC integrity
- ✅ Binary framing with fixed headers

It does not provide:

- ❌ Encryption (all payloads are plaintext)
- ❌ Authentication or identity verification
- ❌ Authorization or access control
- ❌ Replay attack protection
- ❌ Secure key exchange or management

## What must be added for trust/security

Before LTP could support secure distributed operations, the following would need to be implemented:

- TLS or equivalent encrypted transport channel
- Node identity certificates and mutual authentication
- Signed message payloads with provenance tracking
- Authorization layer (RBAC or capability-based)
- Audit trail for all operations
- Secure session management
