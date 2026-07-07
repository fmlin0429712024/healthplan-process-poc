---
name: oncology-immuno
description: >
  Domain verifier for Oncology immunotherapy and targeted therapy. Covers
  checkpoint inhibitors (Keytruda, Opdivo), targeted agents, and high-cost
  oncology biologics requiring biomarker-driven authorization.
status: stub
version: 0.1.0
parent: guidelines-verifier
---

# Oncology Immunotherapy Domain Verifier

> **STATUS: STUB** — Not yet implemented. Follow the same pattern as `ra-biologic/SKILL.md`.

## Treatments Covered
- Checkpoint inhibitors: Pembrolizumab (Keytruda), Nivolumab (Opdivo), Atezolizumab (Tecentriq)
- Targeted therapy: Osimertinib (Tagrisso), Alectinib (Alecensa), Lorlatinib (Lorbrena)
- ADC: Trastuzumab deruxtecan (Enhertu), Sacituzumab govitecan (Trodelvy)

## Key Criteria to Implement
- Biomarker thresholds: PD-L1 TPS, TMB, MSI-H, EGFR/ALK/ROS1 mutation status
- Line of therapy determination (1L vs 2L vs later) — primary source of ESCALATE
- ECOG performance status requirement
- Prior platinum-based chemotherapy documentation

## Showcase Case
- Scenario 4: David Fontaine — Pembrolizumab (Keytruda) — ESCALATE (PD-L1 TPS 45%, ambiguous line)
