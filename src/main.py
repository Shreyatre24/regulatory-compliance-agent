"""
Regulatory Compliance Agent — run entrypoint.

Pipeline (see ARCHITECTURE.md):
    plan -> retrieve -> write -> validate -> store versioned run

v0.1 goal: this runs end-to-end with stubbed components so you always have a
green pipeline. Replace one stub at a time (see MILESTONES.md).
"""
from pathlib import Path
import argparse

from src.planner import plan_requirements
from src.retriever import Retriever
from src.writer import write_assessment
from src.validator import validate_report
from src.run_store import save_run


def run(regulation_path: str, product_path: str) -> dict:
    regulation_text = Path(regulation_path).read_text(encoding="utf-8", errors="ignore")
    product_text = Path(product_path).read_text(encoding="utf-8", errors="ignore")

    # 1. Planner: decompose the regulation + product into checkable requirements.
    requirements = plan_requirements(regulation_text, product_text)

    # 2. Retriever: for each requirement, pull the relevant regulation clauses.
    retriever = Retriever(regulation_text)

    assessments = []
    for req in requirements:
        clauses = retriever.retrieve(req)
        # 3. Writer: draft a compliance statement / gap for this requirement.
        assessments.append(write_assessment(req, clauses, product_text))

    report = {
        "regulation": Path(regulation_path).name,
        "product": Path(product_path).name,
        "assessments": assessments,
    }

    # 4. Validator: check the report against the schema.
    validate_report(report)

    # 5. Persist a versioned, reproducible run.
    run_id = save_run(report, inputs={"regulation": regulation_path, "product": product_path})
    print(f"Run complete: {run_id}  ({len(assessments)} requirements assessed)")
    print(f"  -> runs/{run_id}/report.json")
    return report


if __name__ == "__main__":
    ap = argparse.ArgumentParser(
        description="Run the regulatory compliance agent on one regulation + one product description."
    )
    ap.add_argument("--regulation", default="data/sample_regulation.txt")
    ap.add_argument("--product", default="data/sample_product.txt")
    args = ap.parse_args()
    run(args.regulation, args.product)
