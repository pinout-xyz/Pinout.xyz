<!--
---
name: AQEX qUPS-P-SC
class: board
type: power
formfactor: Custom
manufacturer: AQEX
description: The qUPS-P-SC is a supercapacitor-based UPS HAT for the Raspberry Pi designed for durability and harsh environments. It features a 100-120F supercapacitor providing approximately 30 seconds of backup time for a Raspberry Pi 4 under max load, allowing for a graceful shutdown during power outages.
url: https://www.aqex.eu/qups-p-sc-raspberry-pi-ups-hat-with-supercapacitor.html
github: https://github.com/aqexhu/qups-guard
buy: https://lectronz.com/products/aqex-qups-p-sc-13-supercap-ups-hat-raspberry-pi
image: 'AQEX-qUPS-P-SC.png'
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
    name: Power Good - Setup#1
    mode: input
    active: high
  '13':
    name: Limit Low - Setup#1
    mode: input
    active: high
  '15':
    name: Shutdown - Setup#1
    mode: output
    active: high
  '16':
    name: Power Good - Setup#2
    mode: input
    active: high
  '18':
    name: Limit Low - Setup#2
    mode: input
    active: high
  '22':
    name: Shutdown - Setup#2
    mode: output
    active: high
  '29':
    name: Power Good - Setup#3
    mode: input
    active: high
  '31':
    name: Limit Low - Setup#3
    mode: input
    active: high
  '37':
    name: Shutdown - Setup#3
    mode: output
    active: high
-->
# AQEX qUPS-P-SC Supercapacitor based UPS HAT

The qUPS-P-SC is a supercapacitor-based UPS HAT for the Raspberry Pi designed for durability and harsh environments. It features a 100-120F supercapacitor providing approximately 30 seconds of backup time for a Raspberry Pi 4 under max load, allowing for a graceful shutdown during power outages.

The board uses 3 GPIO pins for communication, with three selectable hardware configurations via DIP switches to avoid conflicts with other HATs.

- 100-120F Supercapacitor (500,000+ charge cycles)
- 5V/2.5A Output
- Offline topology for high efficiency
- USB-C and Auxiliary 5V power inputs
- Stackable 40-pin header
- Hardware-based "Zero Firmware" logic

## Power
- 5V via USB-C or Auxiliary 5V input
- 5V via GPIO header (powers the Pi)

## Features
- Adjustable energy threshold for safe boot
- Adjustable input voltage threshold
- 3-LED supercapacitor level indicator
- Manual Mode Switch: AUTO / ON / OFF

## Notes
- **Power Good**: High when external power is present.
- **Limit Low**: Signals when supercapacitor energy is dropping below the threshold.
- **Shutdown**: Used to signal the Pi to initiate a graceful shutdown.
- All GPIO communication can be disabled by setting DIP switches to OFF-OFF.
