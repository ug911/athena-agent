---
collection: "InstitutePublicProfile"
model: "InstitutePublicProfile"
source_file: "src/models/InstitutePublicProfile.js"
field_count: 17
last_synced: "2026-04-28T10:58:23+00:00"
---

# `InstitutePublicProfile` (Mongo collection)

- **Model**: `InstitutePublicProfile`
- **Source**: [`src/models/InstitutePublicProfile.js`](../../../src/models/InstitutePublicProfile.js)
- **Athena counterpart**: try `processed.wise_app_backend__institute_public_profile` or `processed.wise_app_backend__institutepublicprofile` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ instituteId: 1 }, { unique: 1 }]`
- `[{ namespace: 1 }]`
- `[{ subdomain: 1 }, { unique: true }]`

## Local sub-schemas referenced

`InstitutePublicProfileSchema`, `sectionSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `instituteId` | `ObjectId` | `Institute` |  | required |  |  |
| `subdomain` | `String` |  |  | required |  |  |
| `namespace` | `String` |  |  | required |  |  |
| `subdomainCreated` | `Number` |  |  |  | 0 |  |
| `isPublic` | `Boolean` |  |  |  | false |  |
| `title` | `String` |  |  | required |  |  |
| `description` | `String` |  |  |  |  |  |
| `textColor` | `String` |  |  |  | '#ffffff' |  |
| `backgroundColor` | `String` |  |  |  | '#101828' |  |
| `ctaText` | `String` |  |  |  | 'Chat now' |  |
| `socialProfile` | `socialProfileSchema` |  |  |  |  |  |
| `instituteCovers` | `Array<coverSchema>` |  |  |  |  |  |
| `sections[]` | `<sectionSchema>` |  |  |  |  |  |
| `sections[].title` | `String` |  |  | required |  |  |
| `sections[].sectionType` | `String` |  | SECTION_TYPE_ALL, SECTION_TYPE_OTHER |  | SECTION_TYPE_OTHER |  |
| `sections[].classIds` | `Array<ObjectId>` | `class` |  |  |  |  |
| `publishedAt` | `Date` |  |  |  |  |  |

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
