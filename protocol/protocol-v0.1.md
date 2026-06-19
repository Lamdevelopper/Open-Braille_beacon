# Open Braille Beacon Protocol v0.1

This protocol is a compact BLE advertising format for silent wall beacon tags.
It is intentionally approximate and offline-first.

## Goals

- Identify Open Braille Beacon tags.
- Let a receiver filter tags by project/protocol.
- Carry enough metadata to select a destination.
- Support rough proximity states using smoothed RSSI.
- Avoid claims of exact distance or safety-critical navigation.

## Conceptual Fields

- `project_id`
- `protocol_version`
- `tag_id`
- `room_id_hash`
- `type`
- `zone`
- `pair_id`
- `pair_role`
- `battery_level`

## Tag Types

- `BRAILLE_SIGN`
- `EXIT`
- `DOOR`
- `STAIRS`
- `ELEVATOR`
- `INFO_POINT`
- `DOOR_LEFT`
- `DOOR_RIGHT`
- `STAIRS_LEFT`
- `STAIRS_RIGHT`

## Paired Tags

Paired tags can mark a doorway, stair opening, or portal.

Example:

```txt
PAIR_ID = STAIRS_A
PAIR_ROLE = LEFT
```

The receiver may compare relative signal strength between paired tags, but must not promise exact alignment, width, or safety guarantees.

## Receiver Behavior

1. Scan BLE advertisements.
2. Filter for Open Braille Beacon project/protocol.
3. Group detected tags by room/building context if available.
4. Let the user select one destination.
5. Ignore non-selected tags during guide mode.
6. Smooth RSSI over time.
7. Convert RSSI to approximate states: `FAR`, `MEDIUM`, `NEAR`, `ARRIVED`.
8. Drive haptic feedback from the selected tag state.
9. Allow fast cancel.

## RSSI Smoothing

```txt
rssi_smoothed = 0.8 * previous + 0.2 * current
```

RSSI thresholds must be tuned in physical tests. Start with conservative defaults and expose them as firmware constants.
