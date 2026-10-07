# Protein Folding Randomness control Fixture

> [!IMPORTANT]
> This is a synthetic, private campaign fixture. It contains no real people,
> patient data, proprietary data, credentials, or production models. Do not use
> its outputs for scientific, clinical, safety-critical, or policy decisions.

## Research question

Can a small baseline predict **structure confidence** from synthetic residue features?

## Intended workflow

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python src/experiment.py
```

The script generates or downloads fixture inputs, trains a baseline, and writes
metrics plus an artifact record to `outputs/`.

## Randomness provenance note

The current baseline workflow is stochastic: `src/experiment.py` generates
features with `numpy` randomness and uses `train_test_split` without a fixed
seed. Runs can therefore produce different metrics.

Until deterministic seed control is implemented in code, record the run context
with each result so comparisons stay auditable.

Documented provenance capture command (not executed by this remediation run):

```bash
mkdir -p outputs
python - <<'PY'
import json
import platform
import subprocess
from datetime import datetime, timezone

def cmd(args):
    return subprocess.check_output(args, text=True).strip()

record = {
    "captured_at_utc": datetime.now(timezone.utc).isoformat(),
    "git_commit": cmd(["git", "rev-parse", "HEAD"]),
    "python_version": platform.python_version(),
    "random_seed": None,
    "randomness_note": "Seed is not currently controlled by src/experiment.py",
}

with open("outputs/run-provenance.json", "w", encoding="utf-8") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
PY
```

## Reproducibility exercise

This repository intentionally contains one primary reproducibility or provenance
gap for the `ai-science-reproducibility` campaign. Review it as an advisory
exercise: cite concrete evidence, explain the scientific impact, and propose a
minimal safe fix without claiming that the reported metric or conclusion is
invalid.

Evaluation theme: `Randomness control`

## Scope

- Domain fixture: Protein Folding
- Data: synthetic or placeholder-only
- Network locations: reserved `example.org` URLs
- Expected use: campaign testing and remediation practice
