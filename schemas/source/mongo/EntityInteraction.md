---
collection: "EntityInteraction"
model: "EntityInteraction"
source_file: "src/models/EntityInteraction.js"
field_count: 9
last_synced: "2026-04-28T10:58:23+00:00"
---

# `EntityInteraction` (Mongo collection)

- **Model**: `EntityInteraction`
- **Source**: [`src/models/EntityInteraction.js`](../../../src/models/EntityInteraction.js)
- **Athena counterpart**: try `processed.wise_app_backend__entity_interaction` or `processed.wise_app_backend__entityinteraction` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1, userId: 1 }]`
- `[{ userId: 1, entityId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`EntityInteractionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `entityId` | `ObjectId` |  |  | required |  |  |
| `markedCompleted` | `Boolean` |  |  |  | false |  |
| `markedCovered` | `Boolean` |  |  |  | false |  |
| `markedCompletedOn` | `Date` |  |  |  |  |  |
| `views` | `Number` |  |  |  | 0 |  |
| `profile` | `String` |  | teacher, student |  | 'student' |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_8 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.insertMany` × 3
- `.find` × 2
- `.findOneAndUpdate` × 1
- `.deleteMany` × 1
- `.updateOne` × 1

### Top call sites

- `src/services/DemoAccountService.js` × 3
- `src/services/classroomService.js` × 2
- `src/workers/dataTransferWorker.js` × 2
- `src/services/classroomCleanupService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
