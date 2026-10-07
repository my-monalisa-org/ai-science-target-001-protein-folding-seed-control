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

The script generates fixture inputs locally in `src/experiment.py` (see
`load_fixture()`), trains a baseline, and writes metrics plus an artifact
record to `outputs/`.

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
