<!--
---
name: DI16ac I2C-HAT
class: board
type: io
formfactor: Custom
manufacturer: Raspihats
description: Isolated input module with 16 channels, 32-bit counters, input filters, interrupt engine and CiA 401-aligned firmware
url: https://raspihats.com/shop/di16ac-i2c-hat/
github: https://github.com/raspihats/raspihats
buy: https://raspihats.com/shop/di16ac-i2c-hat/
image: 'raspihats-i2c-hat-di16ac.png'
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
  '0x40-0x4F':
    name: DI16ac I2C-HAT
    device: raspihats
-->
# DI16ac I2C-HAT

The DI16ac I2C-HAT is a 16-channel isolated digital input module for the Raspberry Pi, built for 24V industrial signals. It is not a GPIO expander: an on-board microcontroller filters and counts every input, records input changes in an interrupt queue and talks to the Pi over a CRC-protected I2C protocol.

Each input accepts sink or source wiring and switches on from +3V to +30V, behind 2000 VAC isolation. The inputs are arranged in four groups of four, each with its own common, on two detachable 3.81mm screw terminals.

## Signal processing on the board

* **Filtering:** per-channel digital filter from 1 to 65535 ms and per-channel polarity inversion
* **Counting:** two 32-bit counters per channel, rising and falling edges, up to 100 Hz; pulses keep being counted while the host is busy or its application restarts
* **Interrupts:** per-channel rising and falling edge masks and a capture queue that records each change together with a snapshot of all input states, so no event is lost between reads. The IRQ line stays asserted while captures are pending, and the engine is armed and disarmed in a single write

The interrupt line is open-drain and active-low: enable the Pi's pull-up on GPIO21 to use it. GPIO21 is connected by default; GPIO20, GPIO22 or GPIO23 can be selected with solder jumpers instead.

## Firmware aligned with CiA 301 and CiA 401

The firmware follows the CANopen device model: its configuration objects are aligned with CiA 301 and its input objects with CiA 401, the profile for generic I/O modules.

* Communication and system watchdogs. When the communication watchdog trips, the interrupt engine is disarmed: pending captures are cleared and the IRQ line is released, so a restarted application starts from a clean state instead of acting on stale events
* Restore factory defaults and a configuration signature that confirms, in a single read, that the stored configuration is still exactly as commissioned
* CRC-16 protected I2C frames, echoed writes and automatic retries
* Status word reporting power-on, reset and watchdog events
* Firmware updates in place over I2C: no jumper, no removal from the panel

## Specifications

* 16 isolated inputs, sink or source, on from +3V to +30V, LED indicator per channel
* 2000 VAC isolation
* Operating temperature -25 to +75°C
* Stackable up to 16 boards, I2C addresses 0x40 to 0x4F
* DIN rail mounting with a [DIN Pi Case Extension](https://raspihats.com/shop/din-pi-case-extension/), one per HAT, stacked on the [DIN Pi Case](https://raspihats.com/shop/din-pi-case/) that holds the Raspberry Pi

## Example

```python
from raspihats.i2c_hats import DI16ac

hat = DI16ac(address=0x40)
hat.di.filters[0] = 10       # 10 ms filter on input 0
print(hat.di.value)          # all 16 inputs as a bitmask
print(hat.di.r_counters[0])  # rising edges on input 0
```

## Software

* [Python](https://pypi.org/project/raspihats/) - `pip install raspihats`, full API reference in the [README](https://github.com/raspihats/raspihats#readme)
* [Node.js](https://www.npmjs.com/package/raspihats)
* [Node-RED](https://www.npmjs.com/package/node-red-contrib-raspihats) - flow-based programming
* [Robot Framework](https://github.com/raspihats/raspihats/blob/master/raspihats/i2c_hats/robot.py) - keyword library for test automation
