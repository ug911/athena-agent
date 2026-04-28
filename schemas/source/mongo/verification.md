---
collection: "verification"
model: "verification"
source_file: "src/models/Verification.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `verification` (Mongo collection)

- **Model**: `verification`
- **Source**: [`src/models/Verification.js`](../../../src/models/Verification.js)
- **Athena counterpart**: try `processed.wise_app_backend__verification` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ identifier: 1 }]`
- `[{ createdAt: 1 }, { expireAfterSeconds: 604800 }]`

## Local sub-schemas referenced

`verificationSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `identifier` | `String` |  |  | required |  |  |
| `idType` | `String` |  | PHONE_NUMBER, EMAIL |  | 'PHONE_NUMBER' |  |
| `resendWindow` | `Date` |  |  |  | getResendWindow |  |
| `expiryTime` | `Date` |  |  |  | getExpiryTime |  |
| `attempts` | `Number` |  |  |  | 0 |  |
| `resendCount` | `Number` |  |  |  | 0 |  |
| `code` | `String` |  |  |  |  |  |
| `ip` | `String` |  |  |  |  |  |
| `verified` | `Boolean` |  |  |  | false |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
