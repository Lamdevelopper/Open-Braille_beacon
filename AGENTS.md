# Repository Guidelines

## Project Purpose

Open Braille Beacon is an open-source, low-cost, offline system that helps blind and low-vision people locate existing Braille or tactile signage inside public buildings. Typical locations include doors, exits, stairs, elevators, information points, schools, hospitals, museums, and libraries.

It is an assistive location cue, not certified indoor navigation. It must never replace a white cane, orientation and mobility training, physical tactile signage, or a user's safety judgment.

## How It Works

The system has two devices:

- **Wall Beacon Tag:** a silent BLE tag installed beside a tactile point of interest. It advertises a compact identifier and minimal metadata; it has no cloud connection and does not emit sound.
- **Receiver Clip:** a wearable receiver that scans nearby tags, lets the user select one destination, and gives haptic feedback as the selected tag becomes stronger.

BLE RSSI is deliberately treated as approximate proximity only. Firmware should smooth it and map it to `FAR`, `MEDIUM`, `NEAR`, and `ARRIVED`; do not calculate or promise exact distance, direction, alignment, or safe passage.

## UX Principles

The central UX rule is: many tags must not create many alerts. The receiver scans a space, presents/selects destinations, and enters guide mode for **one selected tag** only.

Expected flow: `OFF -> ROOM SCAN -> TAG SELECTION -> GUIDE MODE -> ARRIVED/STANDBY`.

Haptics are the v1 default: slow vibration when far, faster when near, and a distinct arrival pattern. Keep interaction simple: short press advances through detected tags; long press confirms, and long press during guidance cancels. Avoid constant speech or audio in v1.

## Repository Layout

- `cad/cadquery/`: parametric enclosure models (`top_cover.py`, `backplate.py`, `assembly.py`).
- `cad/exports/`: generated STEP/STL artifacts; regenerate rather than hand-edit.
- `docs/`: CAD, accessibility, installation, electrical, and test documentation.
- `protocol/`: BLE advertisement and tag-type specifications.
- Future directories: `hardware/`, `firmware/`, `app/`, and `tests/` follow the same device-oriented separation.

## Contribution Rules

Prefer an MVP: offline, open-source, practical, low-power, and low-cost. Keep CAD parametric and dimensions in millimeters. Respect BLE antenna keep-out zones. The tag uses **one CR2032**, never two in series. A receiver vibration motor must use a MOSFET/driver, never a GPIO directly.

Use descriptive lowercase file names such as `backplate.py` and concise Markdown documents such as `protocol-v0.1.md`. Test CAD exports and document physical-fit assumptions before treating a design as production-ready.
