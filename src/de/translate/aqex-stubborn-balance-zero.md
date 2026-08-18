<!--
---
name: AQEX Stubborn Balance Zero
class: board
type: power
formfactor: pHAT
manufacturer: AQEX
description: Stubborn Balance Zero - The Hybrid Supercap UPS for Raspberry Pi Zero. The Perfect Balance of Power Density and Endurance. 
url: https://www.aqex.eu/stubborn-balance-zero-raspberry-pi-zero-ups-hat-hybrid-supercap.html
github: https://github.com/aqexhu/qups-guard
buy: https://lectronz.com/products/aqex-stubborn-balance-zero-ups-hat-rpi-zero-2-wh
image: 'aqex-stubborn-balance-zero.png'
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

# AQEX Stubborn Balance Zero supercapacitor UPS

The Stubborn Balance Zero is a hybrid supercapacitor UPS sized for the Raspberry Pi Zero. Storing energy in hybrid supercapacitors rather than a cell trades some capacity for a claimed 50,000 charge cycles and no chemical ageing, which suits sealed or hard-to-reach installations.

- 5V output at up to 3.5A continuous
- Hybrid supercapacitor storage in 450F, 850F and 1100F options
- Offline topology, with a 100 - 300 microsecond switchover on power loss
- Over-discharge and input fluctuation protection
- AUTO / ON / OFF mode switch and a potentiometer for input threshold tuning
- Pass-through 40-pin header

## Power
- 5V via USB-C, 5.0V - 5.2V, 2A - 3A supply recommended
- 5V via the GPIO header (powers the Pi)

## Modes
- OFF: power cut
- ON: powers up as soon as external or stored power is available
- AUTO: only boots the Pi once the store reaches the "Min" level, to avoid brown-out loops

## Notes
- **Power Good** (pin 16): high while external power is present.
- **Limit Low** (pin 18): signals that stored energy has dropped below the threshold.
- **Shutdown** (pin 22): handshake to the UPS, which cuts power once the OS has halted.
- The [qups-guard](https://github.com/aqexhu/qups-guard) daemon handles monitoring and safe shutdown.

## Estimated runtime
With a Raspberry Pi Zero 2 WH, no load and 100% load:

- 450F: 46 min idle, 13 min at full load
- 850F: 90 min idle, 22 min at full load
- 1100F: 105 min idle, 28 min at full load
