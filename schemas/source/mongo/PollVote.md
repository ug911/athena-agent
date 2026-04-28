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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
