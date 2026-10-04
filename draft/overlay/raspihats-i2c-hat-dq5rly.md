<!--
---
name: DQ5rly I2C-HAT
class: board
type: relay
formfactor: Custom
manufacturer: Raspihats
description: Relay module with 5 PWM-driven 10A changeover relays, watchdog-backed safety and power-on states and CiA 401-aligned firmware
url: https://raspihats.com/shop/dq5rly-i2c-hat/
github: https://github.com/raspihats/raspihats
buy: https://raspihats.com/shop/dq5rly-i2c-hat/
image: 'raspihats-i2c-hat-dq5rly.png'
pincount: 40
eeprom: no
power:
  '2':
  '4':
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
  '0x50-0x5F':
    name: DQ5rly I2C-HAT
    device: raspihats
-->
# DQ5rly I2C-HAT

The DQ5rly I2C-HAT is a 5-channel relay output module for the Raspberry Pi, designed for control cabinets and unattended installations. It is not a GPIO expander driving relays: an on-board microcontroller runs the outputs, enforces their configured states and talks to the Pi over a CRC-protected I2C protocol, using only SDA and SCL.

## Defined relay states, from power-up to failure

Every relay has a defined state at every stage, stored on the board and enforced by its own firmware rather than by the host:

* **Power-up:** the PowerOnValue is applied within milliseconds of power-up, long before Linux has booted, so no relay moves unexpectedly while the Pi starts.
* **Host failure:** if the Pi stops communicating (application crash, kernel hang, bus fault) for longer than the communication watchdog period, each relay goes to its SafetyValue or holds its last state, selected per channel with the SafetyMask.
* **Firmware supervision:** an independent system watchdog supervises the board's own microcontroller.

## PWM coil drive

After pull-in, each relay coil is held by a PWM drive, cutting average coil power by up to 75%. This is what keeps a full stack of 16 boards within the budget of the official Raspberry Pi power supply.

## Firmware aligned with CiA 301 and CiA 401

The firmware follows the CANopen device model: its configuration objects are aligned with CiA 301 and its output objects with CiA 401, the profile for generic I/O modules.

* Output polarity, per-channel safety mask and bulk-write mask
* Restore factory defaults and a configuration signature that confirms, in a single read, that the stored configuration is still exactly as commissioned
* CRC-16 protected I2C frames, echoed writes and automatic retries
* Status word reporting power-on, reset and watchdog events
* Firmware updates in place over I2C: no jumper, no removal from the panel

## Specifications

* 5 relays, Form C (changeover), 10A @ 250VAC/30VDC, LED indicator per channel
* Detachable screw terminals
* 2000 VAC isolation
* Operating temperature -25 to +75°C
* Stackable up to 16 boards, I2C addresses 0x50 to 0x5F (shared by the Raspihats relay boards, so give each one a unique address)
* DIN rail mounting with a [DIN Pi Case Extension](https://raspihats.com/shop/din-pi-case-extension/), one per HAT, stacked on the [DIN Pi Case](https://raspihats.com/shop/din-pi-case/) that holds the Raspberry Pi

## Example

```python
from raspihats.i2c_hats import DQ5rly

hat = DQ5rly(address=0x50)
hat.dq.power_on_value = 0x00  # all open at power-up
hat.dq.safety_value = 0x00    # all open on watchdog trip
hat.cwdt.period = 1.0         # watchdog period, seconds
hat.dq.channels[0] = True     # energize relay 0
```

## Software

* [Python](https://pypi.org/project/raspihats/) - `pip install raspihats`, full API reference in the [README](https://github.com/raspihats/raspihats#readme)
* [Node.js](https://www.npmjs.com/package/raspihats)
* [Node-RED](https://www.npmjs.com/package/node-red-contrib-raspihats) - flow-based programming
* [Robot Framework](https://github.com/raspihats/raspihats/blob/master/raspihats/i2c_hats/robot.py) - keyword library for test automation
