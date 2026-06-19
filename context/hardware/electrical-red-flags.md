# Electrical Red Flags - Open Braille Beacon

- Do not use `2x CR2032` in series for the nRF52 tag. Use `1x CR2032`.
- Do not connect a vibration motor directly to a GPIO pin.
- Do not leave LEDs on continuously in the battery tag.
- Do not place the coin cell, screw heads, or metal shielding over the BLE antenna.
- Do not assume BLE RSSI gives exact distance.
- Do not rely on this system for safety-critical navigation.
- Do not use USB-C charging without correct CC resistor wiring.
- Do not use an unprotected LiPo unless the charger/protection design explicitly covers it.
- Do not expose SWD pads or reset/config controls where the public can easily tamper with them.

## Tag v1 Sanity Targets

- MCU/module: nRF52832 or nRF52-class BLE module.
- Battery: `1x CR2032`, `3 V nominal`.
- Debug LED: normally off.
- Config/reset: reed switch or internal service control.
- Capacitors: local `100 nF` decoupling plus `10-47 uF` bulk near module/battery.
- Programming: SWD pads accessible during assembly.

## Receiver v1 Sanity Targets

- MCU/module: nRF52840 or nRF52-class.
- Battery: protected LiPo, about `150-300 mAh`.
- Charging: USB-C LiPo charger circuit.
- Haptics: coin motor through MOSFET/driver.
- Input: one tactile button plus power switch.
- Audio: omit in v1 unless user testing proves it is necessary.
