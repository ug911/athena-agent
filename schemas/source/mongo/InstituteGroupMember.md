---
collection: "InstituteGroupMember"
model: "InstituteGroupMember"
source_file: "src/models/InstituteGroupMember.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstituteGroupMember` (Mongo collection)

- **Model**: `InstituteGroupMember`
- **Source**: [`src/models/InstituteGroupMember.js`](../../../src/models/InstituteGroupMember.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_group_member` or `processed.wise_app_backend__institutegroupmember` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ groupId: 1, memberId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`instituteGroupMemberSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `groupId` | `ObjectId` | `InstituteGroup` |  | required |  |  |
| `type` | `String` |  | <MEMBER_TYPES> | required |  |  |
| `memberId` | `ObjectId` |  |  | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
