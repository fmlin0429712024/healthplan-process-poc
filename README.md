# AI-Powered Prior Authorization — PoC

A rapid AI prototype demonstrating how Claude + Google ADK can automate prior authorization (PA) processing for a regional health plan.

---

## Problem

A regional health plan processes 15,000 PA requests per month through manual nurse review. Clinical documentation arrives via fax, PDF, portals, and uploads — creating a 4.2-day average turnaround and 22% rework rate due to missing information.

| Metric | Current | Goal |
|--------|---------|------|
| Average turnaround | 4.2 days | **2.5 days** (−40%) |
| Rework rate | 22% | **< 5%** |
| Auto-adjudication | 0% | **70–80%** |
| Provider status calls | Frequent | **Eliminated** |

---

## Four AI Opportunities

### 1. Ingestion — Unstructured → Structured ← *Prototype built*
Multi-channel documentation (fax, PDF, portal, uploads) arrives in any format. AI extracts and normalizes all fields into structured JSON — eliminating manual data entry and enabling downstream automation.

### 2. Document Completeness Checker ← *Prototype built*
22% rework rate stems from missing information. AI validates each submission against treatment tier requirements and identifies missing fields with specific provider guidance — before clinical review begins.

### 3. Clinical Guidelines Verification Engine ← *Prototype built*
Manual guideline verification for 15,000 cases/month is deterministic work for routine cases. AI loads clinical guidelines, evaluates patient data, applies decision logic, and produces APPROVE / DENY / ESCALATE with a full audit trail.

Domain router pattern — each clinical specialty is a **parallel sub-agent**. Add a domain = add a folder.

| Domain | Status |
|--------|--------|
| RA Biologic | ✅ Implemented |
| Oncology / Immuno | Stub |
| Neurology | Stub |
| Diabetes / Metabolic | Stub |
| Inflammatory Bowel | Stub |

### 4. Case Manager — Workflow Automation ← *Prototype built*
Frequent provider status calls consume nurse time. AI tracks PA status through all stages, sends automated updates, handles routine inquiries, and escalates complex ones to the nurse queue.

### How the Four Opportunities Connect

```mermaid
flowchart LR
    A[📄 Incoming Request\nFax · PDF · Portal] --> B[① Ingestion\nExtract & Structure]
    B --> C[② Document Checker\nValidate Completeness]
    C -->|Incomplete| R[↩ Return to Provider]
    C -->|Complete| D[③ Guidelines Verifier\nClinical Decision]
    D -->|APPROVE / DENY| E[④ Case Manager\nNotify & Close]
    D -->|ESCALATE| N[👩‍⚕️ Nurse Review] --> E
```

---

## Prototype — Claude PA Pipeline

End-to-end pipeline implemented as both a **Claude Cowork Skills plugin** (runs in Claude desktop or web — no local setup required) and a **Google ADK project** (enterprise deployment path).

### Pipeline Stages

```
Raw Fax / PDF / Portal
        ↓
[1] Intake Agent        — loads scenario files into session state
        ↓
[2] Ingestion Agent     — unstructured text → structured JSON
        ↓
[3] Document Checker    — completeness validation (✅ / ⚠️ / ❌)
        ↓
[4] Guidelines Verifier — domain router → clinical criteria → decision
        ↓
[5] Case Manager        — provider letter + decision saved to output/
```

### Demo Scenarios (6 cases)

| Scenario | Patient | Drug | Expected Decision |
|----------|---------|------|-------------------|
| scenario-1-auto-approve | Sandra Whitfield | Humira | APPROVE |
| scenario-2-incomplete   | Marcus Webb      | Ozempic | INCOMPLETE → return to provider |
| scenario-3-auto-deny    | Priya Sharma     | Remicade | DENY (CRP below threshold) |
| scenario-4-escalate     | David Fontaine   | Keytruda | ESCALATE (PD-L1 ambiguous) |
| scenario-5-sla-risk     | James Holloway   | IVIG | AT RISK (25h remaining) |
| scenario-6-queue-summary | — | — | Queue dashboard |

### Run the Demo

**Claude Cowork (recommended):** Open the `pa-poc` project in Claude desktop or claude.ai → switch to Cowork → paste any prompt from [`DEMO-PROMPTS.md`](.claude/skills/prior-authorization/runs/DEMO-PROMPTS.md)

**ADK (Python):**
```bash
cd adk_pa && pip install -e . && python run_pa.py scenario-1-auto-approve demo-run-01
```

---

## Extensibility

### ① Eval Loop with Human-in-the-Loop
Teaching Assistant pattern: **Golden Set** (answer key) → **Grader agent** (marks decisions) → **HITL escalation** (nurse review for conflicts).
- 80% deterministic: zero tolerance, exact match required
- 10% autonomous: scored on 3 dimensions (conclusion / reasoning / escalation quality)
- Status: designed + built, not yet connected to live systems

### ② Knowledge Wiki — Engineering Project Context
SKILL.md files are plain-English business rules readable by non-engineers. CLAUDE.md provides agent onboarding context. Clinical staff propose updates; engineers version-control; AI agents inject at runtime. No model retraining required.
- Status: designed + built, not yet connected to live wiki

### ③ Plugin Marketplace — Shareable & Discoverable
PA pipeline registered in the [AI-PDLC Marketplace](https://github.com/fmlin0429712024/ai-pdlc-marketplace) following Anthropic's plugin registry pattern. Live on GitHub Pages. Any team can discover and install via one prompt.
- Status: **live** — published at https://fmlin0429712024.github.io/ai-pdlc-marketplace/

### ④ Google ADK — Enterprise Deployment Path *(only one outside Claude Code)*
Same pipeline mirrored as a Google ADK project using Gemini 2.5 Pro on Vertex AI. SKILL.md files are identical in both. Switching is an infrastructure decision — no business logic changes. Enterprise features: IAM auth, Cloud Logging, auto-scaling, HIPAA-eligible BAA.
- Status: designed + built, not yet deployed to cloud

---


## Tech Stack

| Layer | Prototype | Production Path |
|-------|-----------|-----------------|
| AI Model | Claude Sonnet (Anthropic API) | Gemini 2.5 Pro (Vertex AI) |
| Orchestration | Google ADK SequentialAgent | Google ADK (same) |
| Business Rules | SKILL.md (plain English) | SKILL.md → internal wiki |
| State | InMemorySessionService | Cloud Firestore |
| Auth | Local ADC | Google Cloud IAM + VPC |
| Compliance | — | HIPAA BAA (Google Cloud) |

---