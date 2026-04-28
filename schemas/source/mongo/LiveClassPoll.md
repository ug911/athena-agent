---
collection: "LiveClassPoll"
model: "LiveClassPoll"
source_file: "src/models/LiveClassPoll.js"
field_count: 25
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LiveClassPoll` (Mongo collection)

- **Model**: `LiveClassPoll`
- **Source**: [`src/models/LiveClassPoll.js`](../../../src/models/LiveClassPoll.js)
- **Athena counterpart**: try `processed.wise_app_backend__live_class_poll` or `processed.wise_app_backend__liveclasspoll` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ insightId: 1 }]`

## Local sub-schemas referenced

`LiveClassPollSchema`, `PollOptionsSchema`, `SingleOptionSchema`, `VoteSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `insightId` | `ObjectId` | `LiveClassInsight` |  | required |  |  |
| `type` | `String` |  | POLL, QUIZ | required |  |  |
| `question` | `String` |  |  | required |  |  |
| `image` | `String` |  |  |  |  |  |
| `questionType` | `String` |  | <VALID_QUESTION_TYPES> |  | QUESTION_TYPE_SINGLE_CORRECT |  |
| `options` | `<PollOptionsSchema>` |  |  |  |  |  |
| `maxAnswers` | `Number` |  |  |  | 1 |  |
| `correctAnswers` | `Array<String>` |  |  |  |  |  |
| `votes[]` | `<VoteSchema>` |  |  |  | [] |  |
| `votes[].userId` | `String` |  |  | required |  |  |
| `votes[].answers` | `Array<String>` |  |  |  |  |  |
| `votes[].answer` | `String` |  |  |  |  |  |
| `votes[].timeTaken` | `Number` |  |  |  |  |  |
| `votes[].votedCorrect` | `Boolean` |  |  |  |  |  |
| `votes[].createdAt` | `Date` |  |  |  | Date.now |  |
| `votes[].updatedAt` | `Date` |  |  |  | Date.now |  |
| `showResults` | `Boolean` |  |  |  | false |  |
| `isWordCloud` | `Boolean` |  |  |  | false |  |
| `tags` | `Array` |  |  |  |  |  |
| `visibleTags` | `Array` |  |  |  |  |  |
| `endsAt` | `Date` |  |  |  |  |  |
| `duration` | `Number` |  |  |  |  |  |
| `tempVotedUsers` | `Array` |  |  |  |  |  |
| `agendaId` | `ObjectId` | `LiveClassAgenda` |  |  |  |  |
| `testId` | `ObjectId` | `LiveClassTest` |  |  |  |  |

## Usage (from backend-api)

_14 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.updateMany` × 4
- `.create` × 3
- `.findOneAndUpdate` × 3
- `.find` × 2
- `.updateOne` × 1
- `.findOne` × 1

### Top call sites

- `src/services/lensAnalyticsService.js` × 14

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
