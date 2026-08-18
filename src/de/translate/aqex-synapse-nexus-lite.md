<!--
---
name: AQEX Synapse Nexus Lite
class: board
type: io
formfactor: HAT
manufacturer: AQEX
description: AQEX Synapse Nexus Lite - Essential Raspberry Pi IO Module for Simple Tasks
url: https://www.aqex.eu/synapse-nexus-lite-raspberry-pi-io-hat.html
github: https://github.com/aqexhu/piohat
buy: https://lectronz.com/products/aqex-qpio-10lite-io-hat-for-the-pi
image: 'aqex-synapse-nexus-lite.png'
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
  '8':
    name: Relay Output 1
    mode: output
    active: high
  '10':
    name: Relay Output 2
    mode: output
    active: high
  '11':
    name: Input 1
    mode: input
    active: high
  '13':
    name: Input 2
    mode: input
    active: high


-->

# AQEX Synapse Nexus Lite I/O HAT

The Synapse Nexus Lite is a cut-down version of AQEX's industrial I/O boards, with two relay outputs and two isolated inputs on a full-size HAT footprint. It uses four GPIO pins and needs no firmware or driver.

- 2 SPDT relay outputs (COM, NO, NC), 10A at 240V AC / 24V DC
- 2 opto-isolated digital inputs for 3V - 45V DC
- Double isolation on the outputs: optocoupler plus relay galvanic separation
- Push-in spring terminals for field wiring
- Extended pass-through header, only the 4 GPIO pins in use are reserved

## Power
- 5V via the GPIO header

## Relay outputs
- Relay 1: GPIO 14 (pin 8)
- Relay 2: GPIO 15 (pin 10)

Driving a GPIO high energises the corresponding relay.

## Inputs
- Input 1: GPIO 17 (pin 11)
- Input 2: GPIO 27 (pin 13)

An input reads high when voltage is present on its terminal.

## Notes
- The relay control pins are the UART TXD and RXD pins, so the serial console must be disabled to use them as GPIO.
