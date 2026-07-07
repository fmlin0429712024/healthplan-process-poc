#!/usr/bin/env python3
"""
PA Pipeline — Dry Run Demo

Usage:
  python run_pa.py <scenario_name> [run_name]

Examples:
  python run_pa.py scenario-1-auto-approve
  python run_pa.py scenario-1-auto-approve demo-run-01
  python run_pa.py scenario-2-incomplete    demo-run-02
"""
import asyncio
import sys
from dotenv import load_dotenv

load_dotenv()

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types as genai_types

from pa_agent.agent import build_pipeline

DIVIDER = "=" * 60


async def run(scenario: str, run_name: str) -> None:
    pipeline = build_pipeline(run_name=run_name)
    session_service = InMemorySessionService()
    runner = Runner(
        agent=pipeline,
        session_service=session_service,
        app_name="pa_pipeline",
    )

    session = await session_service.create_session(
        app_name="pa_pipeline",
        user_id="demo",
        state={"run_name": run_name},
    )

    print(f"\n{DIVIDER}")
    print("PA PIPELINE — DRY RUN")
    print(f"Scenario : {scenario}")
    print(f"Run name : {run_name}")
    print(f"{DIVIDER}\n")

    message = genai_types.Content(
        role="user",
        parts=[genai_types.Part(
            text=f"Process PA scenario '{scenario}'. Save findings with run_name '{run_name}'."
        )],
    )

    async for event in runner.run_async(
        user_id="demo",
        session_id=session.id,
        new_message=message,
    ):
        if event.content and event.content.parts:
            for part in event.content.parts:
                if hasattr(part, "text") and part.text:
                    print(part.text)
        if hasattr(event, "tool_call") and event.tool_call:
            print(f"\n[Tool] {event.tool_call.name}({event.tool_call.args})\n")

    print(f"\n{DIVIDER}")
    print(f"Done. Output saved to: output/{run_name}/")
    print(f"{DIVIDER}\n")


if __name__ == "__main__":
    scenario = sys.argv[1] if len(sys.argv) > 1 else "scenario-1-auto-approve"
    run_name = sys.argv[2] if len(sys.argv) > 2 else "pa-demo-01"
    asyncio.run(run(scenario, run_name))
