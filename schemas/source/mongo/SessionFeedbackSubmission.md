---
collection: "SessionFeedbackSubmission"
model: "SessionFeedbackSubmission"
source_file: "src/models/SessionFeedbackSubmission.js"
field_count: 16
last_synced: "2026-04-28T10:58:23+00:00"
---

# `SessionFeedbackSubmission` (Mongo collection)

- **Model**: `SessionFeedbackSubmission`
- **Source**: [`src/models/SessionFeedbackSubmission.js`](../../../src/models/SessionFeedbackSubmission.js)
- **Athena counterpart**: try `processed.wise_app_backend__session_feedback_submission` or `processed.wise_app_backend__sessionfeedbacksubmission` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ sessionId: 1, userId: 1, unauthUserId: 1 }, { unique: true }]`
- `[{ classId: 1 }]`

## Local sub-schemas referenced

`answerSchema`, `sessionFeedbackSubmissionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  |  |  |  |
| `unauthUserId` | `String` |  |  |  |  |  |
| `sessionId` | `ObjectId` | `zoom` |  | required |  |  |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `profile` | `String` |  | teacher, student | required |  |  |
| `answers[]` | `<answerSchema>` |  |  |  |  |  |
| `answers[].questionText` | `String` |  |  |  |  |  |
| `answers[].type` | `String` |  | TYPE_LONG_ANSWER, TYPE_SHORT_ANSWER, TYPE_POLL | required |  |  |
| `answers[].options` | `Object` |  |  |  |  |  |
| `answers[].answer` | `String` |  |  |  |  |  |
| `rating` | `Number` |  |  |  |  |  |
| `sessionStatus` | `String` |  | <VALID_SESSION_STATUSES> |  |  |  |
| `commentText` | `String` |  |  |  |  |  |
| `comment` | `String` |  |  |  |  |  |
| `creditsConsumed` | `Number` |  |  |  |  |  |
| `metadata` | `Object` |  |  |  |  |  |

## Usage (from backend-api)

_21 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 7
- `.findOne` × 4
- `.aggregate` × 3
- `.findOneAndUpdate` × 2
- `.deleteMany` × 2
- `.insertMany` × 1
- `.deleteOne` × 1
- `.updateOne` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `sessionId` × 2
- `userId` × 1

### Top call sites

- `src/services/instituteService.js` × 6
- `src/services/sessionCreditService.js` × 4
- `src/controllers/LensInMeetingController.js` × 2
- `src/services/instituteAnalyticsService.js` × 2
- `src/workers/dataTransferWorker.js` × 2
- `src/services/lensAnalyticsService.js` × 1
- `src/services/DemoAccountService.js` × 1
- `src/services/classroomCleanupService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
