<!--
---
name: Tentacle T3 for Raspberry Pi
class: board
type: sensor
formfactor: Custom
collected: Other
manufacturer: Whitebox Labs
description: A stackable add-on board to host up to 5 Atlas Scientific EZO device to measure PH, Dissolved Oxygen, Electric Conductivity (E.C.), Oxidation-Reduction Potential (ORP) temperature (RTD) and control dosing pumps (EZO-PMP).
url: https://www.whiteboxes.ch/docs/tentacle/t3
github: https://github.com/whitebox-labs/tentacle-raspi-oshw
buy: https://www.whiteboxes.ch/shop/tentacle-t3-for-raspberry-pi
image: 'whitebox-tentacle-t3.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  'dynamic':
    name: Atlas Scientific EZO
    device: multiple
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
# Tentacle T3 for Raspberry Pi

This Raspberry Pi add-on board is stackable. Each Tentacle T3 can host up to 5 EZO-class devices from Atlas Scientific to measure PH, Dissolved Oxygen, Electric Conductivity (E.C.), Oxidation-Reduction Potential (ORP) temperature (RTD) and control dosing pumps (EZO-PMP). The EZO devices must be in I2C mode. All I2C addresses can be set dynamically.

## Features

- 2 fully isolated channels for Atlas Scientific EZO Circuits
- 1 non-isolated channel Atlas Scientific EZO RTD Circuit
- 2 additional I2C channels for EZO 5pin-sensors and 3rd-party I2C devices
  - works with the EZO-PMP embedded dosing pump and EZO-CO2 NDIR Co2 sensor.
I2C only

Built in electrical isolation means that sensors won’t interfere with each other. It also removes outside electrical noise that can interfere with readings.
