---
collection: "temp_user"
model: "tempUser"
source_file: "src/models/TempUser.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `temp_user` (Mongo collection)

- **Model**: `tempUser`
- **Source**: [`src/models/TempUser.js`](../../../src/models/TempUser.js)
- **Athena counterpart**: try `processed.wise_app_backend__temp_user` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`tempUserSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `String` |  |  | required |  |  |
| `idType` | `String` |  | PHONE, PHONE_NUMBER, FIREBASE_ID | required |  |  |
| `metadata` | `Object` |  |  |  | {} |  |

## Usage (from backend-api)

_4 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 2
- `.deleteOne` × 1
- `.create` × 1

### Top call sites

- `src/services/loginService.js` × 4

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
