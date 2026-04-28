---
collection: "SavedCommunication"
model: "SavedCommunication"
source_file: "src/models/SavedCommunication.js"
field_count: 11
last_synced: "2026-04-28T10:58:23+00:00"
---

# `SavedCommunication` (Mongo collection)

- **Model**: `SavedCommunication`
- **Source**: [`src/models/SavedCommunication.js`](../../../src/models/SavedCommunication.js)
- **Athena counterpart**: try `processed.wise_app_backend__saved_communication` or `processed.wise_app_backend__savedcommunication` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ createdAt: 1 }, { expireAfterSeconds: 15552000 }]`
- `[{ userId: 1 }]`
- `[{ notificationId: 1 }]`

## Local sub-schemas referenced

`SavedCommunicationsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `ownerId` | `ObjectId` | `user` |  |  |  |  |
| `instituteId` | `ObjectId` | `Institute` |  |  |  |  |
| `classId` | `ObjectId` | `class` |  |  |  |  |
| `notificationId` | `String` |  |  |  |  |  |
| `creditsUsed` | `Number` |  |  | required |  |  |
| `type` | `String` |  | COMMS_EMAIL, COMMS_WHATSAPP | required |  |  |
| `category` | `String` |  |  | required |  |  |
| `customIntegration` | `Boolean` |  |  |  |  |  |
| `title` | `String` |  |  |  |  |  |
| `statusMetadata` | `<inline-schema>` |  |  |  |  |  |

## Usage (from backend-api)

_6 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.aggregate` × 2
- `.findOne` × 1
- `.updateOne` × 1
- `.find` × 1
- `.create` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `classId` × 1

### Top call sites

- `src/services/communications/commCreditService.js` × 3
- `src/controllers/AWSWebhookController.js` × 2
- `src/controllers/InstituteController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
