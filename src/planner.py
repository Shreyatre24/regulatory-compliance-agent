"""Planner: decompose a regulation + product description into discrete, checkable requirements.

This is the agentic brain of v0.1 — where you decide HOW to break a regulation into an
actionable checklist. In your thesis this was the Planner in the Planner/Executor split;
here it's public and yours to show off. Make this file good and the repo tells your story.

TODO(you): replace the stub with a real LLM call that returns a list of requirement dicts.
Prompt idea: give the model the regulation text + product, ask for a JSON list of
{id, requirement, source_hint}. Keep the return shape identical so the pipeline keeps running.
"""
from typing import List, Dict


def plan_requirements(regulation_text: str, product_text: str) -> List[Dict]:
    # --- STUB: returns mock requirements so the pipeline runs green from day one ---
    return [
        {"id": "R-001", "requirement": "Example requirement extracted from the regulation.",
         "source_hint": "Article 1"},
        {"id": "R-002", "requirement": "Second example requirement.",
         "source_hint": "Article 2"},
    ]
