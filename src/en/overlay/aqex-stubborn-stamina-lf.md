<!--
---
name: AQEX Stubborn Stamina LF
class: board
type: power
formfactor: HAT
manufacturer: AQEX
description: High-reliability LiFePO4 UPS engineered for long-term Raspberry Pi deployments. Zero-configuration design (no jumpers or settings) ensuring relentless uptime with superior thermal stability and extended cycle life over standard Li-ion.
url: https://www.aqex.eu/stubborn-stamina-lf-raspberry-pi-lfp-ups-hat.html
github: https://github.com/aqexhu/qups-guard
buy: https://lectronz.com/products/aqex-stubborn-stamina-lf-ups-hat-for-the-pi
image: 'aqex-stubborn-stamina-lf.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '16':
    name: Power Good
    mode: input
    active: high
  '18':
    name: Limit Low
    mode: input
    active: high
  '22':
    name: Shutdown
    mode: output
    active: high
-->

# AQEX Stubborn Stamina LF LiFePO4 UPS HAT

The Stubborn Stamina LF is a single-cell LiFePO4 UPS HAT for the Raspberry Pi, aimed at long-running deployments where cell life and thermal stability matter more than energy density. It is sold with or without a cell, and the holder accepts 18650, 26650 or 32700 LiFePO4 cells.

- 5V output at up to 3.5A continuous, enough for a Pi 5 with peripherals
- 2A charge current, 7.5A maximum battery discharge
- Offline topology, with a 100 - 300 microsecond switchover on power loss
- Deep discharge, overcharge and reverse polarity protection
- Optional NTC connector for temperature-aware charging
- AUTO / ON / OFF mode switch and a potentiometer for input threshold tuning

## Power
- 5V via USB-C, 5.0V - 5.2V
- 5V via the GPIO header (powers the Pi)

## Modes
- OFF: power cut
- ON: powers up as soon as external or battery power is available
- AUTO: only boots the Pi once the cell reaches the "Min" level, to avoid brown-out loops

## Notes
- **Power Good** (pin 16): high while external power is present.
- **Limit Low** (pin 18): signals that stored energy has dropped below the threshold.
- **Shutdown** (pin 22): handshake to the UPS, which cuts power once the OS has halted.
- LiFePO4 cells only. A 3.7V Li-ion cell will not charge correctly on this board.
- The [qups-guard](https://github.com/aqexhu/qups-guard) daemon handles monitoring and safe shutdown.

## Estimated runtime
With a 4000mAh LiFePO4 cell, no load and 100% load:

- Raspberry Pi 2: 535 min idle, 285 min at full load
- Raspberry Pi 3: 428 min idle, 172 min at full load
- Raspberry Pi 4: 413 min idle, 124 min at full load
- Raspberry Pi 5: 261 min idle, 109 min at full load
