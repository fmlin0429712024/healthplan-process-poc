# CLAUDE.md — Prior Authorization AI PoC

## What This Is
End-to-end PA pipeline: raw fax/PDF → structured data → completeness check → clinical guidelines → APPROVE / DENY / ESCALATE.

## Two Implementations (keep in sync)

| | Claude Skills Plugin | Google ADK Project |
|---|---|---|
| Location | `.claude/skills/prior-authorization/` | `adk_pa/` |
| Purpose | AI co-working / prototyping | Enterprise deployment |
| Business rules | `_1-ingestion/` … `_5-eval/` SKILL.md files | `skills/` (same files, no `_1-` prefixes) |
| Test data | `runs/showcase-set-1/` | `data/` |

## Architecture Rules
- `adk_pa/` is **fully self-contained** — never reference `../.claude/` from inside it
- When updating a SKILL.md, update the copy in **both** locations
- `adk_pa/output/` = runtime decisions; `deliverables/` = stakeholder PDFs/HTML — do not mix

## Run the Demo
```bash
cd adk_pa
pip install -e .
python run_pa.py scenario-1-auto-approve demo-run-01
```

## 6 Test Scenarios
| Scenario | Decision |
|----------|----------|
| scenario-1-auto-approve | APPROVE (Humira, all criteria pass) |
| scenario-2-incomplete | RETURN to provider (labs missing) |
| scenario-3-auto-deny | DENY (Remicade, CRP too low) |
| scenario-4-escalate | ESCALATE (Keytruda, PD-L1 ambiguous) |
| scenario-5-sla-risk | AT RISK (IVIG, 25h SLA remaining) |
| scenario-6-queue-summary | Queue dashboard |

## Extensibility (designed, not yet wired)
- `_5-eval/` — Eval loop: Golden Set → Grader → HITL escalation
- `guidelines-verifier/ra-biologic/` implemented; 4 domain stubs remain
- ADK ready for Vertex AI (Gemini 2.5 Pro) production deploy

## Start Here
1. `README.md`
2. `.claude/skills/prior-authorization/SKILL.md`
3. `adk_pa/pa_agent/agent.py`
