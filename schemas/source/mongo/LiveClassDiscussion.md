---
collection: "LiveClassDiscussion"
model: "LiveClassDiscussion"
source_file: "src/models/LiveClassDiscussion.js"
field_count: 14
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LiveClassDiscussion` (Mongo collection)

- **Model**: `LiveClassDiscussion`
- **Source**: [`src/models/LiveClassDiscussion.js`](../../../src/models/LiveClassDiscussion.js)
- **Athena counterpart**: try `processed.wise_app_backend__live_class_discussion` or `processed.wise_app_backend__liveclassdiscussion` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ insightId: 1 }]`

## Local sub-schemas referenced

`LiveClassDiscussionSchema`, `repliesSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `question` | `String` |  |  | required |  |  |
| `anonymous` | `Boolean` |  |  |  | false |  |
| `pinned` | `Boolean` |  |  |  |  |  |
| `insightId` | `ObjectId` | `LiveClassInsight` |  | required |  |  |
| `userId` | `String` |  |  | required |  |  |
| `replies[]` | `<repliesSchema>` |  |  |  |  |  |
| `replies[].userId` | `String` |  |  | required |  |  |
| `replies[].edited` | `Boolean` |  |  |  |  |  |
| `replies[].reply` | `String` |  |  |  |  |  |
| `upvoted` | `Array<String>` |  |  |  |  |  |
| `starred` | `Boolean` |  |  |  |  |  |
| `status` | `String` |  | STATUS_CREATED, STATUS_APPROVED, STATUS_RESOLVED |  | STATUS_CREATED |  |
| `edited` | `Boolean` |  |  |  |  |  |
| `editedBy` | `String` |  | PARTICIPANT_TYPE_HOST, PARTICIPANT_TYPE_COHOST, PARTICIPA… |  |  |  |

## Usage (from backend-api)

_12 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOneAndUpdate` × 5
- `.findOne` × 3
- `.create` × 1
- `.updateMany` × 1
- `.deleteOne` × 1
- `.aggregate` × 1

### Top call sites

- `src/services/liveClassDiscussionService.js` × 11
- `src/controllers/LensInMeetingController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
