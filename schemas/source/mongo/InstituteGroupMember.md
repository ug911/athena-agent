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

## Usage (from backend-api)

_13 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.find` × 5
- `.findOne` × 2
- `.create` × 2
- `.deleteOne` × 2
- `.deleteMany` × 1
- `.aggregate` × 1

### Top call sites

- `src/services/instituteGroupService.js` × 9
- `src/controllers/TeacherController.js` × 1
- `src/services/classroomService.js` × 1
- `src/services/instituteService.js` × 1
- `src/services/instituteAdmissionService.js` × 1

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
