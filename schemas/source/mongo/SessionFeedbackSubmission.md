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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
