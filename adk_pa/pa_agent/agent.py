from pathlib import Path
from google.adk.agents import Agent, SequentialAgent

MODEL = "gemini-2.5-pro"

# All paths are relative to adk_pa/ — fully self-contained
_SKILLS = Path(__file__).parent.parent / "skills"


def _skill(relative_path: str) -> str:
    return (_SKILLS / relative_path).read_text()


# ---------------------------------------------------------------------------
# Intake — reads scenario files into session state
# ---------------------------------------------------------------------------

def _build_intake_agent() -> Agent:
    from pa_agent.tools import list_scenarios, read_scenario_raw, read_scenario_json

    return Agent(
        model=MODEL,
        name="intake",
        description="Reads a PA scenario's raw document and structured JSON into session state.",
        instruction="""You are the intake agent for the Prior Authorization pipeline.

1. Call list_scenarios() to confirm the scenario exists.
2. Call read_scenario_raw(scenario_name) to load the raw fax/document text.
3. Call read_scenario_json(scenario_name) to load the pre-structured input JSON.
4. Report one line: what was loaded and which sources are available.

Do NOT evaluate or process the content. Load and confirm only.
""",
        tools=[list_scenarios, read_scenario_raw, read_scenario_json],
        output_key="intake_summary",
    )


# ---------------------------------------------------------------------------
# Ingestion — raw text → structured JSON
# ---------------------------------------------------------------------------

def _build_ingestion_agent() -> Agent:
    skill_text = _skill("ingestion/SKILL.md")

    def get_instruction(ctx):
        raw_input = ctx.state.get("raw_input", "")
        return f"""{skill_text}

---
## RAW DOCUMENT TO PROCESS

{raw_input}

---
Extract all fields per the SKILL above and output the structured JSON.
End with one line: "Ready for document-checker" or "Missing fields — provider follow-up required."
"""

    return Agent(
        model=MODEL,
        name="ingestion",
        description="Converts raw PA fax/document text into structured JSON.",
        instruction=get_instruction,
        output_key="ingestion_output",
    )


# ---------------------------------------------------------------------------
# Document Checker — validates completeness
# ---------------------------------------------------------------------------

def _build_document_checker_agent() -> Agent:
    skill_text = _skill("document-checker/SKILL.md")

    def get_instruction(ctx):
        structured = ctx.state.get("ingestion_output") or ctx.state.get("scenario_json", "No input found.")
        return f"""{skill_text}

---
## PA SUBMISSION TO VALIDATE

{structured}

---
Run the completeness check and output the full PA COMPLETENESS REPORT.
"""

    return Agent(
        model=MODEL,
        name="document_checker",
        description="Validates completeness of a PA submission.",
        instruction=get_instruction,
        output_key="document_check_output",
    )


# ---------------------------------------------------------------------------
# Guidelines Verifier — domain router + clinical criteria
# ---------------------------------------------------------------------------

def _build_guidelines_verifier_agent() -> Agent:
    router_skill   = _skill("guidelines-verifier/SKILL.md")
    ra_biologic    = _skill("guidelines-verifier/ra-biologic/SKILL.md")

    def get_instruction(ctx):
        doc_check  = ctx.state.get("document_check_output", "")
        structured = ctx.state.get("ingestion_output") or ctx.state.get("scenario_json", "")
        return f"""## DOMAIN ROUTER
{router_skill}

---
## ACTIVE DOMAIN: ra-biologic
{ra_biologic}

---
## DOCUMENT CHECK RESULT
{doc_check}

## PA SUBMISSION
{structured}

---
If INCOMPLETE → output: "SKIP — returned to provider."
If COMPLETE   → evaluate all criteria and output the CLINICAL GUIDELINES VERIFICATION REPORT
                with decision: APPROVE, DENY, or ESCALATE.
"""

    return Agent(
        model=MODEL,
        name="guidelines_verifier",
        description="Routes to clinical domain and produces APPROVE / DENY / ESCALATE.",
        instruction=get_instruction,
        output_key="guidelines_output",
    )


# ---------------------------------------------------------------------------
# Case Manager — final decision + provider communication
# ---------------------------------------------------------------------------

def _build_case_manager_agent() -> Agent:
    from pa_agent.tools import save_decision
    skill_text = _skill("case-manager/SKILL.md")

    def get_instruction(ctx):
        guidelines_output = ctx.state.get("guidelines_output", "")
        run_name          = ctx.state.get("run_name", "pa-run")
        scenario_name     = ctx.state.get("scenario_name", "unknown")
        return f"""{skill_text}

---
## DECISION FROM GUIDELINES VERIFIER
{guidelines_output}

## RUN: {run_name} | SCENARIO: {scenario_name}

---
1. Draft the appropriate provider communication.
2. Call save_decision(run_name="{run_name}", decision_json=<full output as JSON string>).
3. Print a one-paragraph summary of the decision and what the provider receives.
"""

    return Agent(
        model=MODEL,
        name="case_manager",
        description="Generates provider communications and saves the final PA decision.",
        instruction=get_instruction,
        tools=[save_decision],
        output_key="case_manager_output",
    )


# ---------------------------------------------------------------------------
# Pipeline builder
# ---------------------------------------------------------------------------

def build_pipeline(run_name: str = "pa-run") -> SequentialAgent:
    """Build the full PA pipeline. Call once per run — ADK agents cannot be reused."""
    return SequentialAgent(
        name="pa_pipeline",
        description="PA pipeline: ingestion → completeness check → clinical criteria → decision.",
        sub_agents=[
            _build_intake_agent(),
            _build_ingestion_agent(),
            _build_document_checker_agent(),
            _build_guidelines_verifier_agent(),
            _build_case_manager_agent(),
        ],
    )


# ADK entry point — discovered by `adk run pa_agent` or `adk web`
root_agent = build_pipeline()
