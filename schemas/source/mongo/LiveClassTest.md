---
collection: "LiveClassTest"
model: "LiveClassTest"
source_file: "src/models/LiveClassTest.js"
field_count: 12
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LiveClassTest` (Mongo collection)

- **Model**: `LiveClassTest`
- **Source**: [`src/models/LiveClassTest.js`](../../../src/models/LiveClassTest.js)
- **Athena counterpart**: try `processed.wise_app_backend__live_class_test` or `processed.wise_app_backend__liveclasstest` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ insightId: 1 }]`

## Local sub-schemas referenced

`LiveClassTestSchema`, `SubmissionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `insightId` | `ObjectId` | `LiveClassInsight` |  | required |  |  |
| `title` | `String` |  |  | required |  |  |
| `tags` | `Array` |  |  |  |  |  |
| `visibleTags` | `Array` |  |  |  |  |  |
| `endsAt` | `Date` |  |  |  |  |  |
| `duration` | `Number` |  |  |  |  |  |
| `submissions[]` | `<SubmissionSchema>` |  |  |  |  |  |
| `submissions[].userId` | `String` |  |  | required |  |  |
| `submissions[].submittedAt` | `Date` |  |  |  |  |  |
| `showResults` | `Boolean` |  |  |  |  |  |
| `questions` | `Array<ObjectId>` | `LiveClassPoll` |  |  |  |  |
| `agendaId` | `ObjectId` | `LiveClassAgenda` |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
