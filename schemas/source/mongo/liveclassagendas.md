---
collection: "liveclassagendas"
model: "LiveClassAgenda"
source_file: "src/models/LiveClassAgenda.js"
field_count: 0
last_synced: "2026-04-28T10:58:23+00:00"
---

# `liveclassagendas` (Mongo collection)

- **Model**: `LiveClassAgenda`
- **Source**: [`src/models/LiveClassAgenda.js`](../../../src/models/LiveClassAgenda.js)
- **Athena counterpart**: try `processed.wise_app_backend__liveclassagendas` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`AgendaItemSchema`, `LiveClassAgendaSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |

## Usage (from backend-api)

_11 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 5
- `.create` × 2
- `.aggregate` × 1
- `.find` × 1
- `.findOneAndUpdate` × 1
- `.deleteOne` × 1

### Top call sites

- `src/services/lensAgendaService.js` × 8
- `src/controllers/InstituteController.js` × 2
- `src/services/lensAnalyticsService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
