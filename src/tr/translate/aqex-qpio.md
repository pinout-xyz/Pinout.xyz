<!--
---
name: AQEX qPIO
class: board
type: io
formfactor: HAT
manufacturer: AQEX
description: qPIO HAT - 4 Relays, 8 Isolated Inputs - The Raspberry Pi I/O Solution. 
url: https://aqex.eu/qpio-raspberry-pi-io-module-with-8-input-4-output.html
buy: https://lectronz.com/products/aqex-qpio-4-relays-8-input-hat-raspberry-pi
image: 'aqex-qpio.png'
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
  '11':
    name: Input 2
    mode: input
    active: high
  '13':
    name: Input 1
    mode: input
    active: high
  '15':
    name: Input 3
    mode: input
    active: high
  '29':
    name: Input 4
    mode: input
    active: high
  '31':
    name: Input 8
    mode: input
    active: high
  '32':
    name: Input 7
    mode: input
    active: high
  '33':
    name: Input 6
    mode: input
    active: high
  '35':
    name: Relay 1
    mode: output
    active: high
  '36':
    name: Input 5
    mode: input
    active: high
  '37':
    name: Relay 2
    mode: output
    active: high
  '38':
    name: Relay 3
    mode: output
    active: high
  '40':
    name: Relay 4
    mode: output
    active: high

-->

# AQEX qPIO industrial I/O HAT

The qPIO is a 4-relay, 8-input expansion HAT for the Raspberry Pi, intended for interfacing 3.3V logic with mains and 24V industrial equipment. All twelve channels are opto-isolated and driven straight from GPIO, so there is no firmware or I2C layer in the way.

- 4 changeover relay outputs (COM, NO, NC) using OMRON relays, 10A at 250V AC
- 8 opto-isolated digital inputs, each factory-set to voltage level (3V - 45V) or dry contact sensing
- Double isolation on the outputs: optocoupler plus relay galvanic separation
- Status LED per relay channel
- Push-in spring terminals for field wiring
- Extended pass-through header, only the 12 GPIO pins in use are reserved

## Power
- 5V via the GPIO header

## Relay outputs
- Relay 1: GPIO 19 (pin 35)
- Relay 2: GPIO 26 (pin 37)
- Relay 3: GPIO 20 (pin 38)
- Relay 4: GPIO 21 (pin 40)

Driving a GPIO high energises the corresponding relay.

## Inputs
- Input 1: GPIO 27 (pin 13)
- Input 2: GPIO 17 (pin 11)
- Input 3: GPIO 22 (pin 15)
- Input 4: GPIO 5 (pin 29)
- Input 5: GPIO 16 (pin 36)
- Input 6: GPIO 13 (pin 33)
- Input 7: GPIO 12 (pin 32)
- Input 8: GPIO 6 (pin 31)

An input reads high when voltage is present on its terminal, or when the contact is closed on channels configured for dry contact sensing.
