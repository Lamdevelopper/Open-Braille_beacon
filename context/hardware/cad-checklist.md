# CAD Checklist - Wall Beacon Tag v1

## Exterior

- Overall target: `40 x 35 x ~12 mm`.
- Use soft exterior corners: `R6` plan corners and about `R2` top edge fillet.
- Keep the LED window small, flush, and only for setup/debug.
- Avoid sharp external edges that snag clothing or collect dirt.

## Top Cover

- Wall thickness target: `2.0 mm`.
- Leave the bottom open so PCB and battery mount to the backplate.
- Add a simple lower alignment lip with about `0.3 mm` clearance per side for 3D printing.
- Prefer screws for v1; avoid fragile snap-fits until dimensions are tested.
- If using internal bosses, add pilot holes and fillets at the base.

## Backplate

- Thickness target: `2.2-3.0 mm`; current parametric target is `2.5 mm`.
- Include a flat/recessed VHB pad area: about `30 x 25 x 0.3 mm`.
- Add optional screw holes, but do not make screws mandatory for installation.
- Keep PCB supports on the backplate, not the top cover.
- Provide enough clearance for a real CR2032 holder, not only the coin cell.
- Place the reed switch near a side wall, close enough for magnet activation.

## Electronics Clearance

- Reserve a PCB placeholder around `32 x 26 x 1.6 mm`.
- Reserve a CR2032 holder placeholder around `24 x 22 x 5 mm`.
- Keep the BLE antenna area away from metal, battery, screw heads, and dense copper.
- Do not put metal directly above the antenna.
- Make sure the LED aligns with the light pipe/window only if the PCB orientation is fixed.

## Prototype Checks

- Print one top cover and one backplate before adding complex features.
- Test fit with `0.2 mm`, `0.3 mm`, and `0.4 mm` clearances if the printer is unknown.
- Check screw boss cracking with the actual screw size.
- Check magnet activation through the wall with the selected reed switch.
- Check that VHB recess does not warp the backplate.
- Verify the enclosure can be opened for battery replacement.
