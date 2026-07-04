"""The shape of a compliance report — the single source of truth for output structure."""

STATUS_VALUES = {"compliant", "gap", "needs_review"}

REQUIRED_ASSESSMENT_FIELDS = ("id", "requirement", "status", "rationale", "evidence")

# Reference shape of one assessment (documentation for readers of your repo):
ASSESSMENT_EXAMPLE = {
    "id": "R-001",
    "requirement": "The system shall provide documentation of its limitations.",
    "status": "compliant",           # compliant | gap | needs_review
    "rationale": "Why this status was assigned.",
    "evidence": ["Relevant clause text ..."],
}
