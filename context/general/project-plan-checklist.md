```md
# Open Braille Beacon - V1 Project Checklist

## V1 Definition

V1 is a complete, bench-validated, offline system: a production-oriented Wall Beacon Tag and a functional Receiver Clip prototype. It is an assistive locator for existing tactile/Braille points, never safety-critical indoor navigation.

**V1 excludes:** cloud services, mobile app, UWB, camera features, continuous audio, a custom receiver PCB, and user-pilot certification.

## Phase 0 - Foundation

- [x] Define the product boundary and safety language.
- [x] Freeze v1 UX: silent tags, one-button haptic receiver, single selected destination.
- [x] Freeze tools: Fusion 360 for mechanical source of truth, KiCad for PCB, Zephyr/nRF Connect for firmware.
- [x] Freeze core parts: Raytac MDBT42Q tag module; nRF52840 development board for receiver.
- [ ] Create and maintain a decision log for part availability, fabricator, and bench-test location.

**Exit criteria:** scope, safety limits, hardware platform, and UX are recorded and agreed before PCB design.

## Phase 1 - Wall Beacon Tag

**Dependencies:** Phase 0; see `context/hardware/cad-checklist.md`, `context/hardware/electrical-red-flags.md`, and `protocol/protocol-v0.1.md`.

- [ ] Finalize separate Fusion models for the top cover and backplate.
- [ ] Print and test `0.2 mm`, `0.3 mm`, and `0.4 mm` fit clearances; choose the production clearance.
- [ ] Validate screw bosses, VHB recess, LED window, battery-holder clearance, reed-switch pocket, and antenna keep-out.
- [ ] Create tag BOM and verify MDBT42Q availability; document only electrically compatible approved alternatives.
- [ ] Create KiCad schematic: CR2032 power, module, SWD pads, reed switch, debug LED, `100 nF` decoupling, and `10-47 uF` bulk capacitance.
- [ ] Create PCB layout with antenna keep-out and mechanical mounting constraints.
- [ ] Generate fabrication package: Gerbers, drill files, pick-and-place/BOM where applicable, assembly notes, and enclosure exports.
- [ ] Bench-test current draw, BLE advertising, reed-switch action, battery operation, and enclosure fit.

**Exit criteria:** the tag has a complete fabrication package, verified enclosure fit, and repeatable bench results.

## Phase 2 - Receiver Clip Prototype

**Dependencies:** Phase 0 and a working tag advertisement.

- [ ] Select the exact nRF52840 development board, protected LiPo, USB-C charger, motor, MOSFET/driver, diode, switch, and button.
- [ ] Build the receiver harness; never drive the vibration motor from a GPIO.
- [ ] Create a provisional Fusion clip enclosure with safe board, battery, button, and charging-port access.
- [ ] Validate charging/protection, power-off behavior, motor drive, button reliability, and wearable attachment.

**Exit criteria:** an independently wearable, rechargeable receiver prototype can scan and guide using haptics.

## Phase 3 - Firmware and Protocol

**Dependencies:** selected hardware and `protocol/protocol-v0.1.md`.

- [ ] Create a Zephyr workspace with separate `tag` and `receiver` applications.
- [ ] Implement compact tag advertising using Open Braille Beacon identifiers.
- [ ] Implement receiver scanning and filtering for compatible tags only.
- [ ] Implement one-button UX: short press cycles tags; long press confirms; long press during guide mode cancels.
- [ ] Implement single-target guide mode, RSSI smoothing, and configurable `FAR`, `MEDIUM`, `NEAR`, and `ARRIVED` thresholds.
- [ ] Implement distinct haptic patterns and restart/recovery behavior.
- [ ] Document build, flash, configuration, and threshold-tuning commands.

**Exit criteria:** firmware can be built and flashed reproducibly; the receiver guides only toward its selected tag.

## Phase 4 - Verification and Hardware-Ready Gate

- [ ] CAD: record fit, screw-boss, VHB, and battery-replacement results.
- [ ] Tag: record advertising discovery, CR2032 current budget, reed-switch, and antenna keep-out checks.
- [ ] Receiver: record state-machine, haptic, charger/protection, motor-driver electrical, and thermal checks.
- [ ] System: test several tags in one room, selected-tag isolation, RSSI stability, cancellation, arrival, and restart recovery.
- [ ] Publish bench results, known limitations, BOM revision, fabrication files, and flashing instructions.

**Hardware-ready definition:** verified CAD fit; complete tag fabrication package; functional receiver prototype; repeatable firmware build/flash steps; documented bench results.

## Phase 5 - Future Controlled Accessibility Pilot

- [ ] Define a small indoor test setting and installation rules.
- [ ] Prepare consent, safety language, and observation protocol with blind/low-vision participants.
- [ ] Evaluate haptic clarity, tag selection, mounting consistency, and false/unstable RSSI feedback.
- [ ] Convert findings into prioritized v2 requirements; do not claim navigation safety or certification.

**Exit criteria:** documented participant feedback and an evidence-based v2 backlog.
```