<!--
---
name: Monarco HAT
class: board
type: adc, dac, io, led, com, rtc, power, motor
formfactor: HAT
manufacturer: Monarco
collected: Other
description: Industrial I/O for the Raspberry Pi
url: https://monarco.io
github: https://github.com/monarco
schematic: http://www.monarco.io/docs/Monarco-HAT-Hardware-Reference-Manual.pdf
buy: https://www.monarco.io/#buy-monarco-hat
image: 'monarco-hat.png'
pincount: 40
eeprom: yes
power:
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    name: RS-485, can be disabled
    mode: uart
  '10':
    name: RS-485, can be disabled
    mode: uart
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '37':
    name: ID EEPROM write enable
    mode: output
    active: low
  '38':
    name: MCU bootloader enable
    mode: output
    active: high
  '40':
    name: MCU RESETn
    mode: output
    active: low
i2c:
  '0x18':
    name: Real Time Clock Module
    device: MCP79410
  '0x6f':
    name: 1-Wire Interface Controller
    device: DS2482-100
-->
# Monarco HAT

Manufactured by Monarco Solutions Group / REX Controls s.r.o., the Monarco HAT is is an all-in-one solution for using Raspberry Pi in industrial automation. It provides analog and digital inputs and outputs as well as RS-485 and 1-Wire communication interfaces. In fact, it turns the Raspberry Pi into a PLC or a mini industrial PC (IPC) ready for use in your automation project.

All the inputs and outputs are designed to directly interface standard industrial sensors and devices, eliminating the need for additional hardware. 

## Features

- **Power supply: 10-30 VDC**, powers also the Raspberry Pi
- **4x digital IN, 3.5-30 VDC**, optical isolation, common GND
    - 2x counter (pulse/DIR) or 2x encoder (A/B), up to 200 kHz
    - Counter values retention during power off
- **4x digital OUT**, open-drain, max 40 VDC, 1 A per channel continuous
    - All with up to 100 kHz PWM
    - Short-circuit protection (continuous)
- **2x analog IN**, 0-10 V / 0-20 mA, 12-bit
    - Electronic switching of voltage/current sensing mode
    - Protected against over-voltage and reverse polarity
    - 500 Hz bandwidth, configurable filter
- **2x analog OUT**, 0-10 V, 0.5 ms settling time, 12-bit
- **1x RS-485 bus** with ESD protection
- **1x 1-Wire bus** with ESD protection
- **9x LED indicator**, by default mapped as indicators for digital inputs and outputs and system status, user controllable
- **High quality push-in terminals**, detachable connector
- **Battery-backed RTC chip** for keeping the track of time
- **Hardware watchdog** for power-cycling the Raspberry Pi in case of failure
- Compatible with the **Raspberry Pi 7“ official touchscreen** (on-board connector for powering the display)
- **EMC tested, CE marked**