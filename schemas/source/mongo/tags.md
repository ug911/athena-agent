---
collection: "tags"
model: "tags"
source_file: "src/models/tags.js"
field_count: 3
last_synced: "2026-04-28T10:58:23+00:00"
---

# `tags` (Mongo collection)

- **Model**: `tags`
- **Source**: [`src/models/tags.js`](../../../src/models/tags.js)
- **Athena counterpart**: try `processed.wise_app_backend__tags` — verify in `schemas/INDEX.md`.

## Local sub-schemas referenced

`tagsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `type` | `String` |  | language, subject, grades | required |  |  |
| `tag` | `String` |  |  | required |  |  |
| `searchTerm` | `String` |  |  | required, unique |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
