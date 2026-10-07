# Provenance record

| Field | Value |
|---|---|
| Domain | Protein Folding |
| Input description | synthetic residue features |
| Random seed | Not recorded |
| Data snapshot | `synthetic-v1` (from `config.yaml` `data.version`) |
| Model artifact digest | Not recorded by default; capture from `outputs/model.joblib` after each run |
| Intended use | Synthetic campaign evaluation only |

## Review note

This fixture's primary incomplete record concerns **The workflow does not fully record or apply random seeds.** Remediation
should preserve the synthetic-only scope and avoid overstating scientific impact.

## Artifact digest capture (documented, not executed here)

After generating `outputs/model.joblib`, record an immutable checksum for audit
traceability:

```bash
sha256sum outputs/model.joblib > outputs/model.joblib.sha256
```
