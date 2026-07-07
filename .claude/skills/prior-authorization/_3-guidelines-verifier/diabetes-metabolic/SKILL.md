---
name: diabetes-metabolic
description: >
  Domain verifier for Diabetes & Metabolic conditions. Covers GLP-1 agonists
  (Ozempic, Mounjaro), SGLT-2 inhibitors, DPP-4 inhibitors, and insulin analogs.
status: stub
version: 0.1.0
parent: guidelines-verifier
---

# Diabetes & Metabolic Domain Verifier

> **STATUS: STUB** — Not yet implemented. Follow the same pattern as `ra-biologic/SKILL.md`.

## Treatments Covered
- GLP-1 agonists: Semaglutide (Ozempic, Wegovy), Tirzepatide (Mounjaro), Liraglutide (Victoza)
- SGLT-2 inhibitors: Empagliflozin (Jardiance), Dapagliflozin (Farxiga)
- DPP-4 inhibitors: Sitagliptin (Januvia), Saxagliptin (Onglyza)
- Insulin analogs: Degludec (Tresiba), Glargine (Lantus, Basaglar)

## Key Criteria to Implement
- HbA1c threshold (typically ≥7.5% for GLP-1 authorization)
- Step therapy: Metformin + one second-line agent required before GLP-1
- BMI criteria for weight-management indication
- Cardiovascular risk documentation (for SGLT-2/GLP-1 CV indication)

## Showcase Case
- Scenario 2: Marcus Webb — Semaglutide (Ozempic) — RETURN_TO_PROVIDER (missing labs)
