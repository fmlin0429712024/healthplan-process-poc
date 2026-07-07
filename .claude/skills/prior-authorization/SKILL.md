---
name: prior-authorization
description: >
  AI-powered Prior Authorization pipeline for a regional health plan. Orchestrates
  three sub-skills to reduce turnaround from 4.2 days to 2.5 days and auto-adjudicate
  70-80% of routine cases without increasing headcount. Trigger on any PA-related
  request: document validation, clinical criteria evaluation, case status, queue
  management, or provider communications.
status: development
version: 0.1.0
---

# Prior Authorization — AI Pipeline Orchestrator

## What this plugin does

Automates the regional health plan's prior authorization (PA) workflow through two
coordinated flows: a forward pipeline and an evaluation layer.

### Forward Pipeline (~80% deterministic, ~10% autonomous)

```
Fax / PDF / Portal / Provider Upload
         │
         ▼
┌─────────────────────┐
│  _1 Ingestion       │  ← OCR text → structured JSON
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  _2 Doc Checker     │  ← completeness validation
└──────────┬──────────┘
           │ COMPLETE
           ▼
┌─────────────────────┐
│  _3 Guidelines      │  ← clinical criteria → decision
│     Verifier        │
└──────────┬──────────┘
           │
    ┌──────┴──────┬──────────┐
    ▼             ▼          ▼
APPROVE        DENY      ESCALATE
(auto ~45%)  (auto ~35%) (~10% → nurse)
    │             │          │
    └──────┬───────┘          │
           ▼                  ▼
┌─────────────────────┐  ┌──────────────────────┐
│  _4 Case Manager    │  │  Nurse Review (human) │
│ (status, SLA,       │  └──────────────────────┘
│  comms, queue)      │
└─────────────────────┘
```

### Eval Flow — Teaching Assistant

```
  AI Decision (from forward pipeline)
         │
         ▼
┌─────────────────────────────────────┐
│  _5 Eval                            │
│                                     │
│  Golden Set ──► Grader              │
│  (answer key)   (compare & score)   │
└──────────┬──────────────────────────┘
           │
    ┌──────┴──────┬──────────┐
    ▼             ▼          ▼
✅ MATCH    ⚠️ BORDERLINE  ❌ MISMATCH
  log done   HITL review   HITL urgent
                  │              │
                  └──────┬───────┘
                         ▼
              ┌─────────────────────┐
              │  Human Reviewer     │
              │  (HITL — arbitrate) │
              └─────────────────────┘
```

## Sub-skills

### Forward Pipeline

| Sub-skill | Location | Invoke when... |
|-----------|----------|----------------|
| **Ingestion** | `_1-ingestion/SKILL.md` | Raw text arrives (fax, PDF, portal) — convert to structured JSON |
| **Document Checker** | `_2-document-checker/SKILL.md` | Structured JSON ready — validate completeness |
| **Guidelines Verifier** | `_3-guidelines-verifier/SKILL.md` | Complete PA — evaluate clinical criteria → APPROVE / DENY / ESCALATE |
| **Case Manager** | `_4-case-manager/SKILL.md` | Case status, queue summary, SLA tracking, provider communications |

### Eval Flow

| Sub-skill | Location | Invoke when... |
|-----------|----------|----------------|
| **Eval** | `_5-eval/SKILL.md` | An AI decision needs grading against the golden set; or running batch quality review |

## Reference data (this plugin)

All reference data lives inside this plugin directory — the plugin is self-contained.

| File | Used by | Contents |
|------|---------|----------|
| `reference/pa-requests.json` | _2, _3, _4 | 20 synthetic PA cases across all pipeline stages |
| `reference/clinical-guidelines.json` | _3 | 10 clinical guideline sets (RA biologics, GLP-1s, imaging, oncology, etc.) |
| `reference/providers.json` | _2, _4 | 10 provider profiles with NPI, specialty, contact info, PA quality metrics |
| `reference/pa-status-history.json` | _4 | Case event timelines, daily queue metrics, monthly trends |
| `reference/golden-set.json` | _5 | Expert-labeled ground truth decisions for eval grading |

Sub-skills reference these as `reference/<file>.json` relative to this plugin root.

## Run outputs

Test and showcase run outputs go in `runs/<run-name>/`. Never inside the sub-skill folders.

```
runs/
└── showcase-set-1/          ← demo scenarios for stakeholder presentation
    ├── README.md            ← what scenarios are covered and how to run them
    ├── document-checker/    ← completeness check outputs
    ├── guidelines-verifier/ ← adjudication outputs
    └── case-manager/ ← status and comms outputs
```

## Business context

| Metric | Current | Goal |
|--------|---------|------|
| Monthly PA volume | ~15,000 | ~15,000 (no change) |
| Avg turnaround | 4.2 days | 2.5 days (−40%) |
| Rework rate | 22% | <5% |
| Auto-adjudication | 0% | 70-80% |
| Nurse focus | Data gathering + clinical judgment | Clinical judgment only |

## How to invoke a sub-skill

Read the relevant `SKILL.md` before starting:

```
# Full pipeline from raw fax text:
Read .claude/skills/prior-authorization/_1-ingestion/SKILL.md, then extract this fax:
[paste raw-input.txt content]

# Check a structured submission for completeness:
Read .claude/skills/prior-authorization/_2-document-checker/SKILL.md, then check case PA-2026-09012.

# Auto-adjudicate a complete PA:
Read .claude/skills/prior-authorization/_3-guidelines-verifier/SKILL.md, then evaluate PA-2026-08847.

# Get queue status or draft a provider letter:
Read .claude/skills/prior-authorization/_4-case-manager/SKILL.md, then show today's queue summary.
```

## Agent roles

| Agent | Layer | Role |
|-------|-------|------|
| **Ingestion** | Forward | Converter — raw text → structured JSON, never fabricates |
| **Document Checker** | Forward | Validator — finds what is missing, never guesses |
| **Guidelines Verifier** | Forward | Adjudicator — applies written criteria → APPROVE / DENY / ESCALATE |
| **Case Manager** | Forward | Communicator — status, SLA, provider comms, queue |
| **Eval** | Eval | Teaching Assistant — grades AI decisions against golden set |
| **Nurse (human)** | HITL | Clinical judgment — ESCALATE cases + eval conflicts |

Clinical judgment for ambiguous cases always goes to a human nurse. The AI adjudicates only cases where the criteria are deterministic.
