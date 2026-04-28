---
collection: "announcements"
model: "announcements"
source_file: "src/models/Discussion.js"
field_count: 26
last_synced: "2026-04-28T10:58:23+00:00"
---

# `announcements` (Mongo collection)

- **Model**: `announcements`
- **Source**: [`src/models/Discussion.js`](../../../src/models/Discussion.js)
- **Athena counterpart**: try `processed.wise_app_backend__announcements` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`announcementsSchema`, `pollSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `title` | `String` |  |  | required |  |  |
| `description` | `String` |  |  |  |  |  |
| `disableCommenting` | `Boolean` |  |  |  | false |  |
| `pinnedDiscussion` | `Boolean` |  |  |  | false |  |
| `canEdit` | `Boolean` |  |  |  |  |  |
| `canDelete` | `Boolean` |  |  |  |  |  |
| `lastCommentedAt` | `Date` |  |  |  |  |  |
| `date` | `String` |  |  | required | dateNow |  |
| `time` | `String` |  |  | required | timeNow |  |
| `userId` | `ObjectId` | `user` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `comments` | `Array<commentsSchema>` |  |  |  |  |  |
| `attachments` | `Array<attachmentSchema>` |  |  |  |  |  |
| `poll` | `Boolean` |  |  |  | false |  |
| `pollData` | `<pollSchema>` |  |  |  | {} |  |
| `pollData.question` | `String` |  |  |  |  |  |
| `pollData.type` | `String` |  | POLL, QUIZ |  |  |  |
| `pollData.options` | `Object` |  |  |  |  |  |
| `pollData.correctAnswer` | `String` |  | A, B, C, D, E |  |  |  |
| `pollData.endsAt` | `Date` |  |  |  |  |  |
| `pollData.showResults` | `Boolean` |  |  |  | false |  |
| `pollData.stats` | `Object` |  |  |  |  |  |
| `pollData.voteCount` | `Number` |  |  |  | 0 |  |
| `public` | `Boolean` |  |  |  |  |  |
| `thumbnail` | `String` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_47 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.aggregate` × 12
- `.findOne` × 12
- `.updateOne` × 6
- `.create` × 5
- `.find` × 4
- `.deleteMany` × 3
- `.deleteOne` × 2
- `.insertMany` × 2
- `.updateMany` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `classId` × 2

### Top call sites

- `src/controllers/UserController.js` × 10
- `src/controllers/TeacherController.js` × 9
- `src/workers/dataTransferWorker.js` × 5
- `src/services/classroomService.js` × 4
- `src/controllers/DiscussionController.js` × 3
- `src/controllers/StudentController.js` × 2
- `src/services/leaderboardService.js` × 2
- `src/services/DemoAccountService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
