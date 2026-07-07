# AI-Powered Prior Authorization — PoC

A rapid AI prototype demonstrating how Claude + Google ADK can automate prior authorization (PA) processing for a regional health plan.

**Built for:** 15-minute innovation briefing · July 2026

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

## Three AI Opportunities

### 1. Intelligent Auto-Adjudication ← *Prototype built*
Raw fax/PDF → AI extracts fields → completeness check → clinical guidelines → APPROVE / DENY / ESCALATE.
Targets 80% of cases decided same-day without nurse touch.

### 2. Clinical Knowledge Intelligence
AI-maintained guideline wiki. Clinical staff edit plain-English files; AI validates consistency and propagates changes to the decision pipeline instantly — no retraining, no deployment.

### 3. Predictive Denial Prevention
Before submission, AI scores approval likelihood and surfaces specific missing fields — so providers fix the submission before the plan ever sees it.

---

## Prototype — Claude PA Pipeline

End-to-end pipeline implemented as both a **Claude Skills plugin** and a **Google ADK project**.

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

```bash
cd adk_pa
pip install -e .
python run_pa.py scenario-1-auto-approve demo-run-01
```

---

## Extensibility (Designed & Built — Not Yet Connected)

Three capabilities are architecturally complete but not yet wired to live systems:

### ① Knowledge Wiki — Engineering Project Context
SKILL.md files are plain-English business rules readable by non-engineers. Clinical staff propose updates; engineers version-control them; AI agents inject them at runtime. No model retraining required. Designed to extend to a live internal wiki with payer policy sync.

### ② Eval Loop with Human-in-the-Loop
Teaching Assistant pattern: **Golden Set** (answer key) → **Grader agent** (marks decisions) → **HITL escalation** (nurse review for conflicts).
- 80% deterministic: zero tolerance, exact match required
- 10% autonomous: scored on 3 dimensions (conclusion / reasoning / escalation quality)
- 10% already escalated by clinical complexity

### ③ Google ADK — Enterprise Deployment Path
The same pipeline runs locally (Claude) and on Google Cloud (ADK + Gemini 2.5 Pro on Vertex AI). Switching is an infrastructure decision — no business logic changes. Enterprise features: IAM auth, Cloud Logging, auto-scaling, HIPAA-eligible BAA.

---

## Project Structure

```
healthplan-process-poc/
│
├── adk_pa/                          # Google ADK implementation (self-contained)
│   ├── pa_agent/
│   │   ├── agent.py                 # SequentialAgent pipeline
│   │   └── tools.py                 # I/O tools (read scenario, save decision)
│   ├── skills/                      # SKILL.md copies (no external references)
│   │   ├── ingestion/
│   │   ├── document-checker/
│   │   ├── guidelines-verifier/
│   │   │   ├── ra-biologic/         # Fully implemented
│   │   │   ├── diabetes-metabolic/  # Stub
│   │   │   ├── oncology-immuno/     # Stub
│   │   │   ├── neurology/           # Stub
│   │   │   └── inflammatory-bowel/  # Stub
│   │   └── case-manager/
│   ├── data/                        # 6 demo scenarios (raw-input.txt + input.json)
│   ├── reference/                   # clinical-guidelines.json, providers.json
│   ├── output/                      # Runtime decisions written here
│   ├── run_pa.py                    # Demo runner
│   ├── pyproject.toml
│   └── .env                         # Vertex AI config
│
├── .claude/skills/prior-authorization/   # Claude Skills plugin
│   ├── SKILL.md                     # Orchestrator + flow diagrams
│   ├── _1-ingestion/
│   ├── _2-document-checker/
│   ├── _3-guidelines-verifier/      # Domain router + 5 domain subfolders
│   ├── _4-case-manager/
│   ├── _5-eval/                     # Eval loop + HITL (designed, not connected)
│   ├── reference/                   # golden-set.json, clinical-guidelines.json, etc.
│   └── runs/showcase-set-1/         # 6 scenario input files
│
├── deliverables/                    # Stakeholder documents
│   ├── pa-ai-pitch.html             # 15-min presentation (12 slides)
│   ├── prior-authorization-ai-solution.html
│   ├── prior-authorization-ai-solution.pdf
│   └── prior-authorization-ai-solution.md
│
├── raw/                             # Source materials
│   ├── sources/                     # Original problem docs
│   └── references/                  # Reference documents
│
├── wiki/                            # Knowledge base
│   ├── entities/
│   ├── concepts/
│   └── queries/
│
└── README.md
```

---

## Tech Stack

| Layer | Prototype | Production Path |
|-------|-----------|-----------------|
| AI Model | Claude Sonnet (Vertex AI) | Gemini 2.5 Pro (Vertex AI) |
| Orchestration | Google ADK SequentialAgent | Google ADK (same) |
| Business Rules | SKILL.md (plain English) | SKILL.md → internal wiki |
| State | InMemorySessionService | Cloud Firestore |
| Auth | Local ADC | Google Cloud IAM + VPC |
| Compliance | — | HIPAA BAA (Google Cloud) |

---

**Interview Assignment · July 2026**
