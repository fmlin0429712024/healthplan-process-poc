---
name: inflammatory-bowel
description: >
  Domain verifier for Inflammatory Bowel Disease. Covers biologics for
  Crohn's disease and Ulcerative Colitis (Remicade, Stelara, Entyvio, Skyrizi).
status: stub
version: 0.1.0
parent: guidelines-verifier
---

# Inflammatory Bowel Disease Domain Verifier

> **STATUS: STUB** — Not yet implemented. Follow the same pattern as `ra-biologic/SKILL.md`.

## Treatments Covered
- Anti-TNF: Infliximab (Remicade), Adalimumab (Humira for IBD), Certolizumab (Cimzia)
- Anti-integrin: Vedolizumab (Entyvio)
- Anti-IL-12/23: Ustekinumab (Stelara), Risankizumab (Skyrizi)
- JAK inhibitors: Upadacitinib (Rinvoq for UC), Tofacitinib (Xeljanz for UC)

## Key Criteria to Implement
- Active disease markers: CRP >10 mg/L AND calprotectin >250 mcg/g
- Step therapy: Mesalamine + immunomodulator (azathioprine or 6-MP) before biologic
- Colonoscopy/endoscopy documentation confirming active disease
- Distinction between Crohn's disease and Ulcerative Colitis criteria

## Showcase Case
- Scenario 3: Priya Sharma — Infliximab (Remicade) — DENY (CRP 4.1, calprotectin 180, both below threshold)
