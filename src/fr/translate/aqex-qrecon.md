<!--
---
name: AQEX qReCon
class: board
type: relay
formfactor: HAT
manufacturer: AQEX
description: qRecon - Configurable 4-Channel Relay HAT for Raspberry Pi IO Expansion. 
url: https://www.aqex.eu/qrecon-raspberry-pi-relay-module-with-4-output.html
github: https://github.com/aqexhu/qReCon
buy: https://lectronz.com/products/aqex-qrecon-quality-relay-hat-raspberry-pi
image: 'aqex-qrecon.png'
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

# AQEX qReCon 4-channel relay HAT

The qReCon is a 4-channel relay HAT for the Raspberry Pi using Schrack relays, with opto-isolation between the Pi and the relay coils. Control pins and trigger polarity are both selected in hardware with DIP switches, so no driver or firmware is needed.

- 4 independent SPDT relay circuits (COM, NC, NO)
- 250V AC / 28V DC rating, 10A through NO, 3A through NC
- Double isolation: opto-isolators plus the relay contacts
- Control logic works at 3.3V or 5V
- Status LED per channel
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

## Notes
- The relay outputs can carry up to 250V AC. The high voltage side of the PCB is outlined and labelled.
- Relay 4 (GPIO 5 / GPIO 6) may energise at boot because of the Pi's internal pull-ups. Set the pin state in `/boot/firmware/config.txt` with `gpio=X=mode,state` to avoid this.
- A C++ example and the user manual are in the [GitHub repository](https://github.com/aqexhu/qReCon).
