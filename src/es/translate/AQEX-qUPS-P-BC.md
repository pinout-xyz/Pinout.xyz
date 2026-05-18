<!--
---
name: AQEX qUPS-P-BC
class: board
type: power
formfactor: Custom
manufacturer: AQEX
description: The AQEX qUPS-P-BC is the reliable multi-chemistry battery-powered UPS HAT that delivers when you need more than just a quick backup. It handles a range of Li-Ion, LiFePo4, and Sodium-Ion options to ensure your Raspberry Pi project stays on for hours, not just minutes.
url: https://www.aqex.eu/qups-p-bc-raspberry-pi-ups-hat-with-battery.html
github: https://github.com/aqexhu/qups-guard
buy: https://lectronz.com/products/aqex-qups-p-bc-20-multichem-ups-hat-for-the-pi
image: 'AQEX-qUPS-P-BC.png'
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
# AQEX qUPS-P-BC multi-chemsitry battery based UPS HAT

The qUPS-P-BC is a versatile battery-powered UPS HAT for the Raspberry Pi. Unlike the supercapacitor version, this model supports various battery chemistries (Li-Ion, LiFePo4, and Sodium-Ion), making it suitable for long-term backup power (ranging from 30 minutes to several hours depending on the battery used).

It features an offline topology for high efficiency and wide-range auxiliary power input (6-28V), allowing it to be powered by 12V or 24V industrial power sources.

- Supports Li-Ion, LiFePo4, and Sodium-Ion batteries
- 5V/3.5A Maximum load current
- Wide Aux Input: 6V - 28V
- USB PD (RPi5) compatible
- NTC connector for battery thermal protection
- Hardware-based "Zero Firmware" logic

## Power
- 5V via USB-C
- 6V - 28V via Auxiliary input
- 5V via GPIO header (powers the Pi)

## Features
- - Charging current: 2A
- Reverse polarity protection for battery and auxiliary input
- 4-LED battery level indicator
- Manual Mode Switch: AUTO / ON / OFF
- Adjustable energy threshold and input voltage threshold

## Notes
- **Power Good**: High when external power is present.
- **Limit Low**: Signals when battery energy is dropping below the threshold.
- **Shutdown**: Used to signal the Pi to initiate a graceful shutdown.
- **Battery Type**: Must be configured correctly via DIP switches to match the chemistry (Li-Ion vs LiFePo4 vs Sodium-Ion) to ensure safe charging voltages.
