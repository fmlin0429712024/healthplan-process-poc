# Showcase Set 1 — Prior Authorization AI Pipeline Demo

Demonstration scenarios for the prior authorization AI pipeline. Each scenario exercises
a different branch of the pipeline using cases from `reference/pa-requests.json`.

## How to run a scenario

Tell Claude Code:
> "Read `.claude/skills/prior-authorization/document-checker/SKILL.md`, then check case PA-2026-09012."

Or use the orchestrator to route automatically:
> "Read `.claude/skills/prior-authorization/SKILL.md`. Adjudicate PA-2026-08847."

Run outputs go in the relevant subfolder here (e.g., `document-checker/`, `guidelines-verifier/`).

---

## Scenario 1: Fast Auto-Approve (PA-2026-08847)
**Sub-skill:** guidelines-verifier
**Case:** Sandra Whitfield — Adalimumab (Humira) for Rheumatoid Arthritis
**Story:** Textbook complete submission. All 14 criteria pass. Should APPROVE in under 1 minute.
**What to show:** Speed of auto-adjudication vs. 4.2-day manual baseline. No nurse time.

## Scenario 2: Incomplete Submission — Missing Labs (PA-2026-09012)
**Sub-skill:** document-checker
**Case:** Marcus Webb — Semaglutide (Ozempic) for Type 2 Diabetes
**Story:** Submission missing HbA1c, fasting glucose, and second-line step therapy agent.
**What to show:** Immediate, specific feedback to provider vs. discovering the gap days later.

## Scenario 3: Auto-Deny — Criteria Not Met (PA-2026-09201)
**Sub-skill:** guidelines-verifier
**Case:** Priya Sharma — Infliximab (Remicade) for Crohn's Disease
**Story:** CRP and calprotectin both below active-disease thresholds. Incomplete step therapy.
**What to show:** Deterministic denial with exact policy citation. No subjectivity.

## Scenario 4: Escalate to Nurse — Ambiguous Oncology Case (PA-2026-09318)
**Sub-skill:** guidelines-verifier
**Case:** David Fontaine — Pembrolizumab (Keytruda) for NSCLC
**Story:** PD-L1 TPS 45% — between 1L and 2L thresholds. Line of therapy ambiguous.
**What to show:** AI routes to nurse with pre-loaded context. Nurse gets a 25-min case instead of starting from scratch.

## Scenario 5: SLA-at-Risk Status + Call Script (PA-2026-09124)
**Sub-skill:** workflow-orchestrator
**Case:** James Holloway — IVIG for Multiple Sclerosis
**Story:** 47 hours elapsed in AWAITING_INFO. Provider has not responded. 25 hours left.
**What to show:** Automated SLA tracking + ready-to-use call script. No manual monitoring needed.

## Scenario 6: Queue Summary — Today's Dashboard
**Sub-skill:** workflow-orchestrator
**Input:** "Show today's queue summary"
**Story:** Pulls from `reference/pa-status-history.json` daily_metrics. Surfaces the 3 breached cases and 6 at-risk nurse cases immediately.
**What to show:** Command-center view for PA manager. Replaces spreadsheet-based status tracking.

---

## Expected outputs

Save run outputs here:
```
showcase-set-1/
├── README.md                    ← this file
├── document-checker/
│   ├── PA-2026-09012-report.md  ← completeness report for Marcus Webb case
│   └── ...
├── guidelines-verifier/
│   ├── PA-2026-08847-approve.md ← approval decision + audit trail
│   ├── PA-2026-09201-deny.md    ← denial decision + policy cite
│   ├── PA-2026-09318-escalate.md ← escalation + nurse context packet
│   └── ...
└── workflow-orchestrator/
    ├── PA-2026-09124-status.md  ← case status + call script
    └── queue-summary-2026-07-07.md ← daily queue dashboard
```
