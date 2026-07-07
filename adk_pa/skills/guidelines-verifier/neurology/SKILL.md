---
name: neurology
description: >
  Domain verifier for Neurology conditions. Covers IVIG, MS disease-modifying
  therapies (Ocrevus, Tysabri, Aubagio), and other high-cost neurology agents.
status: stub
version: 0.1.0
parent: guidelines-verifier
---

# Neurology Domain Verifier

> **STATUS: STUB** — Not yet implemented. Follow the same pattern as `ra-biologic/SKILL.md`.

## Treatments Covered
- IVIG (Immune Globulin IV): for MS, CIDP, myasthenia gravis, GBS
- MS DMTs: Ocrelizumab (Ocrevus), Natalizumab (Tysabri), Teriflunomide (Aubagio), Siponimod (Mayzent)
- Epilepsy: Lacosamide (Vimpat), Perampanel (Fycompa)
- Migraine: Erenumab (Aimovig), Fremanezumab (Ajovy)

## Key Criteria to Implement
- IgG level threshold for IVIG authorization (<400 mg/dL for primary immunodeficiency)
- Neurologist specialist attestation requirement
- MRI documentation for MS diagnosis confirmation
- Relapse frequency criteria for escalation DMTs

## Showcase Case
- Scenario 5: James Holloway — IVIG — AWAITING_INFO (missing IgG level + attestation)
