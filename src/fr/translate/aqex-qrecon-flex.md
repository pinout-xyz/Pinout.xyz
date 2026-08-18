<!--
---
name: AQEX qReCon Flex
class: board
type: relay
formfactor: HAT
manufacturer: AQEX
description: qRecon Flex - Raspberry Pi HAT with Variable & Replaceable Relay Type
url: https://aqex.eu/qrecon-flex-raspberry-pi-relay-module-with-4-output.html
github: https://github.com/aqexhu/qReCon
buy: https://lectronz.com/products/aqex-qrecon-flex-variable-relay-hat-raspberry-pi
image: 'aqex-qrecon-flex.png'
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
  '29':
    name: Relay 4 - Bank 1
    mode: output
    active: high,low
  '31':
    name: Relay 4 - Bank 2
    mode: output
    active: high,low
  '33':
    name: Relay 3 - Bank 2
    mode: output
    active: high,low
  '35':
    name: Relay 2 - Bank 2
    mode: output
    active: high,low
  '36':
    name: Relay 3 - Bank 1
    mode: output
    active: high,low
  '37':
    name: Relay 1 - Bank 2
    mode: output
    active: high,low
  '38':
    name: Relay 2 - Bank 1
    mode: output
    active: high,low
  '40':
    name: Relay 1 - Bank 1
    mode: output
    active: high,low

-->

# AQEX qReCon Flex socketed relay HAT

The qReCon Flex is a 4-channel relay HAT with socketed relays, so each channel can be fitted with a relay to suit the load, or swapped out without soldering. Like the qReCon it is opto-isolated, with DIP switch selection of control pins and trigger polarity.

- 4 independent relay sockets, mixable per channel
- Takes standard industrial relays with a 5V coil
- Double isolation: opto-isolators plus the relay contacts
- Control logic works at 3.3V or 5V
- Screw terminals and an extended pass-through header for stacking

## Power
- 5V via the GPIO header

## GPIO selection
A DIP switch picks one of two GPIO banks per relay, to avoid clashes with other HATs:

- Relay 1: GPIO 21 (pin 40) in bank 1, GPIO 26 (pin 37) in bank 2
- Relay 2: GPIO 20 (pin 38) in bank 1, GPIO 19 (pin 35) in bank 2
- Relay 3: GPIO 16 (pin 36) in bank 1, GPIO 13 (pin 33) in bank 2
- Relay 4: GPIO 5 (pin 29) in bank 1, GPIO 6 (pin 31) in bank 2

## Trigger polarity
A second DIP switch selects the level that energises the relay:

- Active high: GPIO low connects COM-NC, GPIO high connects COM-NO
- Active low: GPIO low connects COM-NO, GPIO high connects COM-NC

## Compatible relays
Tested with, among others:

- Schrack RT1 (RT314005) and RT2 (RT424005)
- Finder 40.51.9.005, 40.52.9.005, 40.61.9.005
- Omron G2RL-1A-E, G2RL-1A4-E, G2RL-1-E, G2RL-14-E, G2RL-2A, G2RL-2
- Omron G5RL-1A-E-LN, G5RL-1A-E-HR, G5RL-1A-E-TV8

Other relays with the same footprint may work, but the coil must be 5V DC.

## Notes
- Fitting a relay with a coil voltage other than 5V may damage the HAT or the Pi.
- With AC loads the terminals can carry up to 250V. The high voltage side of the PCB is outlined and labelled.
- Relay 4 (GPIO 5 / GPIO 6) may energise at boot because of the Pi's internal pull-ups. Set the pin state in `/boot/firmware/config.txt` with `gpio=X=mode,state` to avoid this.
- Utilities and the user manual are in the [GitHub repository](https://github.com/aqexhu/qReCon).
