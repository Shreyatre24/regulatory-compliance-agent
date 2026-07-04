"""Versioned, reproducible run storage.

Every run is written to runs/<timestamp>-<shorthash>/ with its inputs and output. This is the
'versionierte Runs' idea from your thesis, made concrete — and it's a satisfying first win:
it works with the stubs, today.
"""
from pathlib import Path
from datetime import datetime, timezone
import json
import hashlib

RUNS_DIR = Path("runs")


def save_run(report: dict, inputs: dict) -> str:
    RUNS_DIR.mkdir(exist_ok=True)
    ts = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    short = hashlib.sha1(json.dumps(report, sort_keys=True).encode()).hexdigest()[:8]
    run_id = f"{ts}-{short}"
    run_dir = RUNS_DIR / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    (run_dir / "inputs.json").write_text(json.dumps(inputs, indent=2), encoding="utf-8")
    (run_dir / "report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return run_id
