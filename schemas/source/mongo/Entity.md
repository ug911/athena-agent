---
collection: "Entity"
model: "Entity"
source_file: "src/models/Entity.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `Entity` (Mongo collection)

- **Model**: `Entity`
- **Source**: [`src/models/Entity.js`](../../../src/models/Entity.js)
- **Athena counterpart**: try `processed.wise_app_backend__entity` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ entityId: 1 }, { unique: true }]`
- `[{ classId: 1 }]`

## Local sub-schemas referenced

`entitySchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `entityId` | `ObjectId` |  |  | required |  |  |
| `entitySecondaryId` | `String` |  |  |  |  |  |
| `entityType` | `String` |  | <ALL_ENTITIES> | required |  |  |
| `entitySubtype` | `String` |  | POLL, DISCUSSION, FILE, LINK, FOLDER, AD_HOC, SCHEDULED, … |  |  |  |
| `createdAt` | `Date` |  |  |  | Date.now |  |
| `sortKey` | `Date` |  |  |  | Date.now |  |
| `metadata` | `Object` |  |  |  |  |  |
| `archived` | `Boolean` |  |  |  | false |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
