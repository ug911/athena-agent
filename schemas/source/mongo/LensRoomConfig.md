---
collection: "LensRoomConfig"
model: "LensRoomConfig"
source_file: "src/models/LensRoomConfig.js"
field_count: 19
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LensRoomConfig` (Mongo collection)

- **Model**: `LensRoomConfig`
- **Source**: [`src/models/LensRoomConfig.js`](../../../src/models/LensRoomConfig.js)
- **Athena counterpart**: try `processed.wise_app_backend__lens_room_config` or `processed.wise_app_backend__lensroomconfig` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`DiscussionConfigSchema`, `LensRoomConfigSchema`, `PollOptionsSchema`, `PollSchema`, `SingleOptionSchema`, `feedbackConfigSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `classes` |  | required |  |  |
| `polls[]` | `<PollSchema>` |  |  |  | undefined |  |
| `polls[].question` | `String` |  |  | required |  |  |
| `polls[].questionType` | `String` |  | <VALID_QUESTION_TYPES> |  | QUESTION_TYPE_SINGLE_CORRECT |  |
| `polls[].options` | `<PollOptionsSchema>` |  |  | required |  |  |
| `polls[].type` | `String` |  | POLL, QUIZ | required |  |  |
| `polls[].correctAnswers` | `Array<String>` |  | <validOptions> |  |  |  |
| `polls[].maxAnswers` | `Number` |  |  |  | 1 |  |
| `polls[].isWordCloud` | `Boolean` |  |  |  | false |  |
| `feedbackConfig` | `<feedbackConfigSchema>` |  |  |  | undefined |  |
| `feedbackConfig.enabled` | `Boolean` |  |  |  | true |  |
| `feedbackConfig.question` | `String` |  |  |  | 'How did the Session go?' |  |
| `leaderboardConfig` | `LeaderboardConfigSchema` |  |  |  | undefined |  |
| `discussionConfig` | `<DiscussionConfigSchema>` |  |  |  | undefined |  |
| `discussionConfig.enabled` | `Boolean` |  |  |  | false |  |
| `discussionConfig.autoApproval` | `Boolean` |  |  |  | false |  |
| `discussionConfig.allowAnonymous` | `Boolean` |  |  |  | false |  |
| `allowZoomForHost` | `Boolean` |  |  |  | false |  |
| `agendaIds` | `Array<ObjectId>` | `LiveClassAgenda` |  |  |  |  |

## Usage (from backend-api)

_13 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 7
- `.updateOne` × 5
- `.find` × 1

### Populated fields (join hints)

Fields commonly hydrated via `.populate(...)` — in Athena, these are the joins worth pre-computing or caching.

- `agendaIds` × 2

### Top call sites

- `src/services/lensAgendaService.js` × 6
- `src/services/lensAnalyticsService.js` × 3
- `src/controllers/UserController.js` × 1
- `src/controllers/LensInMeetingController.js` × 1
- `src/controllers/InstituteController.js` × 1
- `src/controllers/LensController.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
