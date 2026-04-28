---
collection: "LiveClassLeaderboard"
model: "LiveClassLeaderboard"
source_file: "src/models/LiveClassLeaderboard.js"
field_count: 4
last_synced: "2026-04-28T10:58:23+00:00"
---

# `LiveClassLeaderboard` (Mongo collection)

- **Model**: `LiveClassLeaderboard`
- **Source**: [`src/models/LiveClassLeaderboard.js`](../../../src/models/LiveClassLeaderboard.js)
- **Athena counterpart**: try `processed.wise_app_backend__live_class_leaderboard` or `processed.wise_app_backend__liveclassleaderboard` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ insightId: 1 }, { unique: true }]`

## Local sub-schemas referenced

`LensLeaderboardSchema`, `PointsDistributionSchema`, `UserPointsSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `insightId` | `ObjectId` | `LiveClassInsight` |  | required |  |  |
| `pointsTable[]` | `<UserPointsSchema>` |  |  |  |  |  |
| `pointsTable[].userId` | `String` |  |  | required |  |  |
| `pointsTable[].pointsDistribution` | `<PointsDistributionSchema>` |  |  |  | {} |  |

## Usage (from backend-api)

_8 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOneAndUpdate` × 3
- `.findOne` × 3
- `.create` × 1
- `.updateOne` × 1

### Top call sites

- `src/services/lensLeaderboardService.js` × 6
- `src/services/lensAnalyticsService.js` × 2

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
