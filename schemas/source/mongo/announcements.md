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

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
