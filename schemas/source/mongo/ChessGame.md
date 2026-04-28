---
collection: "ChessGame"
model: "ChessGame"
source_file: "src/models/ChessGame.js"
field_count: 28
last_synced: "2026-04-28T10:58:23+00:00"
---

# `ChessGame` (Mongo collection)

- **Model**: `ChessGame`
- **Source**: [`src/models/ChessGame.js`](../../../src/models/ChessGame.js)
- **Athena counterpart**: try `processed.wise_app_backend__chess_game` or `processed.wise_app_backend__chessgame` — verify in `schemas/INDEX.md`.

## Indexes

- `[{ classId: 1 }]`
- `[{ player1Token: 1 }, { unique: 1 }]`
- `[{ player2Token: 1 }, { unique: 1 }]`
- `[{ viewToken: 1 }, { unique: 1 }]`

## Local sub-schemas referenced

`ChessGameSchema`, `MoveSchema`, `PlayerSchema`

## Fields

| Path | Type | Ref | Enum | Required | Default | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `classId` | `ObjectId` | `class` |  | required |  |  |
| `status` | `String` |  | GAME_STATUS_CREATED, GAME_STATUS_STARTED, GAME_STATUS_ENDED |  | GAME_STATUS_CREATED |  |
| `userId` | `String` |  |  | required |  |  |
| `player1` | `<PlayerSchema>` |  |  | required |  |  |
| `player1.playerId` | `String` |  |  | required |  |  |
| `player1.name` | `String` |  |  | required |  |  |
| `player2` | `<PlayerSchema>` |  |  | required |  |  |
| `player2.playerId` | `String` |  |  | required |  |  |
| `player2.name` | `String` |  |  | required |  |  |
| `player1Token` | `String` |  |  |  | () => `p1${hexadecimal(16)}` |  |
| `player2Token` | `String` |  |  |  | () => `p2${hexadecimal(16)}` |  |
| `viewToken` | `String` |  |  |  | () => `v${hexadecimal(16)}` |  |
| `startFEN` | `String` |  |  |  |  |  |
| `duration` | `Number` |  |  |  |  |  |
| `startTime` | `Date` |  |  |  |  |  |
| `endTime` | `Date` |  |  |  |  |  |
| `history[]` | `<MoveSchema>` |  |  |  |  |  |
| `history[].color` | `String` |  |  | required |  |  |
| `history[].piece` | `String` |  |  | required |  |  |
| `history[].from` | `String` |  |  | required |  |  |
| `history[].to` | `String` |  |  | required |  |  |
| `history[].san` | `String` |  |  | required |  |  |
| `history[].flags` | `String` |  |  | required |  |  |
| `history[].lan` | `String` |  |  | required |  |  |
| `history[].before` | `String` |  |  | required |  |  |
| `history[].after` | `String` |  |  | required |  |  |
| `endReason` | `String` |  |  |  |  |  |
| `winner` | `String` |  |  |  |  |  |

## Usage (from backend-api)

_11 call site(s) found across `controllers/`, `services/`, `repositories/`, `workers/`, `helpers/`._

### Query methods

- `.findOne` × 5
- `.findOneAndUpdate` × 4
- `.create` × 1
- `.updateOne` × 1

### Top call sites

- `src/services/chessGameService.js` × 11

<!-- HUMAN NOTES BELOW -->

<!-- Add human notes (descriptions, gotchas) below this line. -->
