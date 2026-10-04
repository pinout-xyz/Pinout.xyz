<!--
---
name: DI6acDQ6rly I2C-HAT
class: board
type: io, relay
formfactor: Custom
manufacturer: Raspihats
description: I/O module with 6 isolated inputs and 6 PWM-driven relays, watchdog-backed safety states and CiA 401-aligned firmware
url: https://raspihats.com/shop/di6acdq6rly-i2c-hat/
github: https://github.com/raspihats/raspihats
buy: https://raspihats.com/shop/di6acdq6rly-i2c-hat/
image: 'raspihats-i2c-hat-di6acdq6rly.png'
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
  '40':
    name: IRQ
    mode: input
    active: low
i2c:
  '0x60-0x6F':
    name: DI6acDQ6rly I2C-HAT
    device: raspihats
-->
# DI6acDQ6rly I2C-HAT

The DI6acDQ6rly I2C-HAT is a combined I/O module for the Raspberry Pi with 6 isolated digital inputs and 6 power relays, designed for control cabinets and unattended installations. It is not a GPIO expander: an on-board microcontroller filters and counts the inputs, runs the relays, enforces their configured states and talks to the Pi over a CRC-protected I2C protocol.

Each input accepts sink or source wiring and switches on from +3V to +30V, behind 2000 VAC isolation. Each relay is a Form A (normally open) contact rated 5A @ 250VAC/30VDC.

## Defined relay states, from power-up to failure

Every relay has a defined state at every stage, stored on the board and enforced by its own firmware rather than by the host:

* **Power-up:** the PowerOnValue is applied within milliseconds of power-up, long before Linux has booted, so no relay moves unexpectedly while the Pi starts.
* **Host failure:** if the Pi stops communicating (application crash, kernel hang, bus fault) for longer than the communication watchdog period, each relay goes to its SafetyValue or holds its last state, selected per channel with the SafetyMask.
* **Firmware supervision:** an independent system watchdog supervises the board's own microcontroller.

## PWM coil drive

After pull-in, each relay coil is held by a PWM drive, cutting average coil power by up to 75%. This is what keeps a full stack of 16 boards within the budget of the official Raspberry Pi power supply.

## Signal processing on the inputs

* **Filtering:** per-channel digital filter from 1 to 65535 ms and per-channel polarity inversion
* **Counting:** two 32-bit counters per channel, rising and falling edges, up to 100 Hz; pulses keep being counted while the host is busy or its application restarts
* **Interrupts:** per-channel rising and falling edge masks and a capture queue that records each change together with a snapshot of all input states, so no event is lost between reads. The IRQ line stays asserted while captures are pending, and the engine is armed and disarmed in a single write

The interrupt line is open-drain and active-low: enable the Pi's pull-up on GPIO21 to use it. GPIO21 is connected by default; GPIO20, GPIO22 or GPIO23 can be selected with solder jumpers instead.

## Firmware aligned with CiA 301 and CiA 401

The firmware follows the CANopen device model: its configuration objects are aligned with CiA 301 and its I/O objects with CiA 401, the profile for generic I/O modules.

* Output polarity, per-channel safety mask and bulk-write mask
* When the communication watchdog trips, the interrupt engine is also disarmed: pending captures are cleared and the IRQ line is released, so a restarted application starts from a clean state instead of acting on stale events
* Restore factory defaults and a configuration signature that confirms, in a single read, that the stored configuration is still exactly as commissioned
* CRC-16 protected I2C frames, echoed writes and automatic retries
* Status word reporting power-on, reset and watchdog events
* Firmware updates in place over I2C: no jumper, no removal from the panel

## Specifications

* 6 isolated inputs, sink or source, on from +3V to +30V
* 6 relays, Form A (normally open), 5A @ 250VAC/30VDC
* LED indicator on every input and relay
* Detachable screw terminals
* 2000 VAC isolation
* Operating temperature -25 to +75°C
* Stackable up to 16 boards, I2C addresses 0x60 to 0x6F
* DIN rail mounting with a [DIN Pi Case Extension](https://raspihats.com/shop/din-pi-case-extension/), one per HAT, stacked on the [DIN Pi Case](https://raspihats.com/shop/din-pi-case/) that holds the Raspberry Pi

## Example

```python
from raspihats.i2c_hats import DI6acDQ6rly

hat = DI6acDQ6rly(address=0x60)
hat.dq.power_on_value = 0x00  # all open at power-up
hat.dq.safety_value = 0x00    # all open on watchdog trip
hat.cwdt.period = 1.0         # watchdog period, seconds
print(hat.di.value)           # all 6 inputs as a bitmask
hat.dq.channels[0] = True     # energize relay 0
```

## Software

* [Python](https://pypi.org/project/raspihats/) - `pip install raspihats`, full API reference in the [README](https://github.com/raspihats/raspihats#readme)
* [Node.js](https://www.npmjs.com/package/raspihats)
* [Node-RED](https://www.npmjs.com/package/node-red-contrib-raspihats) - flow-based programming
* [Robot Framework](https://github.com/raspihats/raspihats/blob/master/raspihats/i2c_hats/robot.py) - keyword library for test automation
