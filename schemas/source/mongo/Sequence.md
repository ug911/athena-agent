---
collection: "Sequence"
model: "Sequence"
source_file: "src/models/Sequence.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Sequence` (Mongo collection)

- **Model**: `Sequence`
- **Source**: [`src/models/Sequence.js`](../../../src/models/Sequence.js)
- **Athena counterpart**: try `processed.wise_app_backend__sequence` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ scope: 1, sequenceType: 1 }, { unique: true }]`

## Local sub-schemas referenced

`sequenceSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `scope` | `String` |  |  | required |  |  |
| `sequenceType` | `String` |  | INVOICE | required |  |  |
| `value` | `Number` |  |  | required | 0 |  |

## Usage (from backend-api)

_1 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOneAndUpdate` × 1

### Top call sites

- `src/services/feeService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
