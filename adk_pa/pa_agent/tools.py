from pathlib import Path
from google.adk.tools import ToolContext

# All paths are relative to adk_pa/ — fully self-contained
_ROOT = Path(__file__).parent.parent

DATA_DIR      = _ROOT / "data"
OUTPUT_DIR    = _ROOT / "output"
REFERENCE_DIR = _ROOT / "reference"


def list_scenarios() -> dict:
    """List all available PA demo scenarios."""
    scenarios = [d.name for d in sorted(DATA_DIR.iterdir()) if d.is_dir()]
    return {"scenarios": scenarios}


def read_scenario_raw(scenario_name: str, tool_context: ToolContext) -> dict:
    """Read the raw fax/document text for a scenario and store in session state."""
    raw_file = DATA_DIR / scenario_name / "raw-input.txt"
    if not raw_file.exists():
        return {"error": f"raw-input.txt not found: {scenario_name}"}

    content = raw_file.read_text()
    tool_context.state["raw_input"] = content
    tool_context.state["scenario_name"] = scenario_name
    tool_context.state["source_type"] = "raw_fax"
    return {"scenario": scenario_name, "source": "raw-input.txt", "chars": len(content)}


def read_scenario_json(scenario_name: str, tool_context: ToolContext) -> dict:
    """Read the pre-structured JSON input for a scenario and store in session state."""
    json_file = DATA_DIR / scenario_name / "input.json"
    if not json_file.exists():
        return {"error": f"input.json not found: {scenario_name}"}

    content = json_file.read_text()
    tool_context.state["scenario_json"] = content
    tool_context.state["scenario_name"] = scenario_name
    return {"scenario": scenario_name, "source": "input.json", "chars": len(content)}


def save_decision(run_name: str, decision_json: str, tool_context: ToolContext) -> dict:
    """Save the final PA decision to the output directory."""
    scenario_name = tool_context.state.get("scenario_name", "unknown")
    out_dir = OUTPUT_DIR / run_name
    out_dir.mkdir(parents=True, exist_ok=True)

    out_file = out_dir / f"{scenario_name}.json"
    out_file.write_text(decision_json)
    return {"saved": str(out_file), "run": run_name, "scenario": scenario_name}
