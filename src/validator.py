"""Validator: check a report against the compliance schema.

A tiny 'critic' step — cheap, deterministic, and it makes your output trustworthy, which is
exactly the traceable-results story from your CV. Mostly implemented; extend as your schema grows.
"""
from src.schema import STATUS_VALUES, REQUIRED_ASSESSMENT_FIELDS


def validate_report(report: dict) -> None:
    assert "assessments" in report, "report missing 'assessments'"
    for a in report["assessments"]:
        for field in REQUIRED_ASSESSMENT_FIELDS:
            assert field in a, f"assessment {a.get('id', '?')} missing field '{field}'"
        assert a["status"] in STATUS_VALUES, f"invalid status '{a['status']}' in {a['id']}"
    # TODO(you, optional): add JSON Schema validation with the `jsonschema` package
    # for a stronger, declarative critic.
