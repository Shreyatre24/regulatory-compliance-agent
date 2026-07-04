"""Writer: draft a compliance assessment for one requirement.

Produces one assessment dict conforming to the schema (see src/schema.py). This echoes the
schema-oriented generation from your thesis.

TODO(you): replace the stub with an LLM call that, given the requirement + retrieved clauses
+ product description, returns {id, requirement, status, rationale, evidence}. Keep the return
shape aligned with the schema so the validator passes.
"""
from typing import List, Dict


def write_assessment(requirement: Dict, clauses: List[str], product_text: str) -> Dict:
    # --- STUB: deterministic placeholder so the pipeline runs green ---
    return {
        "id": requirement["id"],
        "requirement": requirement["requirement"],
        "status": "needs_review",          # one of: compliant | gap | needs_review
        "rationale": "Stub rationale — replace write_assessment() with a real model call.",
        "evidence": clauses,
    }
