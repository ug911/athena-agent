---
collection: "PollVote"
model: "PollVote"
source_file: "src/models/PollVote.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `PollVote` (Mongo collection)

- **Model**: `PollVote`
- **Source**: [`src/models/PollVote.js`](../../../src/models/PollVote.js)
- **Athena counterpart**: try `processed.wise_app_backend__poll_vote` or `processed.wise_app_backend__pollvote` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`PollVoteSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `pollId` | `ObjectId` | `announcement` |  | required |  |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `answer` | `String` |  | A, B, C, D, E | required |  |  |

## Usage (from backend-api)

_9 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.deleteMany` × 3
- `.create` × 1
- `.findOne` × 1
- `.aggregate` × 1
- `.insertMany` × 1
- `.exists` × 1
- `.find` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `userId` × 1

### Top call sites

- `src/controllers/UserController.js` × 2
- `src/services/sessionAIDataService.js` × 2
- `src/controllers/StudentController.js` × 1
- `src/controllers/TeacherController.js` × 1
- `src/services/DemoAccountService.js` × 1
- `src/services/classroomService.js` × 1
- `src/services/classroomCleanupService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
