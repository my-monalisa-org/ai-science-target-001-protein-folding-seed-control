# Provenance record

| Field | Value |
|---|---|
| Domain | Protein Folding |
| Input description | synthetic residue features generated in `src/experiment.py` via `load_fixture()` |
| Data source attribution | No external dataset; `numpy.random.normal` generates fixture features at runtime |
| Random seed | Not recorded |
| Data snapshot | Generated at runtime; no immutable snapshot file is recorded |
| Model artifact digest | n/a |
| Intended use | Synthetic campaign evaluation only |

## Review note

This fixture's primary incomplete record concerns **The workflow does not fully record or apply random seeds.** Remediation
should preserve the synthetic-only scope and avoid overstating scientific impact.
