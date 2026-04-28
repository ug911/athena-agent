---
collection: "userPreference"
model: "userPreference"
source_file: "src/models/userPreference.js"
field_count: 5
last_synced: "2026-04-28T10:58:23+00:00"
---

# `userPreference` (Mongo collection)

- **Model**: `userPreference`
- **Source**: [`src/models/userPreference.js`](../../../src/models/userPreference.js)
- **Athena counterpart**: try `processed.wise_app_backend__user_preference` or `processed.wise_app_backend__userpreference` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`postsSchema`, `userPreferenceSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `userId` | `ObjectId` | `user` |  | required, unique |  |  |
| `registration` | `Object` |  |  |  |  |  |
| `posts[]` | `<postsSchema>` |  |  |  | [] |  |
| `posts[].entityId` | `String` |  |  | required |  |  |
| `posts[].entityType` | `String` |  | assessment, discussion, session, resource, test | required |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
