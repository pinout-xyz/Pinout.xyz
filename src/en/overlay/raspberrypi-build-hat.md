<!--
---
name: Build HAT
class: board
type: io,motor
formfactor: HAT
manufacturer: Raspberry Pi
description: A HAT for driving LEGO Technic motors and sensors over serial
url: https://www.raspberrypi.com/products/build-hat/
github: https://github.com/RaspberryPiFoundation/python-build-hat
image: 'raspberrypi-build-hat.png'
pincount: 40
eeprom: yes
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
  '7':
    mode: output
    name: Reset
  '8':
    mode: uart
  '10':
    mode: uart
  '11':
    mode: uart
    name: CTS
    description: Reserved, unused
  '36':
    mode: uart
    name: RTS
    description: Reserved, unused
-->
# Build HAT

The Build HAT provides four connectors for LEGO Technic motors and sensors from the SPIKE Portfolio, and was designed with LEGO Education. An on-board RP2040 handles the low-level control of connected devices and is driven from the Raspberry Pi over the serial port, so the serial console must be disabled and the serial port hardware enabled before use.

All of the components sit on the underside of the board, leaving the top free for a breadboard or LEGO elements. Fitting a tall header and 15mm spacers keeps the GPIO pins accessible, but the pins listed here belong to the Build HAT and should be left alone.

Motors and the SPIKE colour and distance sensors need an external 8V supply, delivered through a 5.5mm x 2.1mm centre-positive barrel connector. The board then feeds the Raspberry Pi over the GPIO header, so no separate USB power supply is needed. Reading motor encoders and the SPIKE force sensor works on Raspberry Pi USB power alone.

The Build HAT fits any Raspberry Pi with a 40-pin GPIO header, including Zero-series boards. It cannot power Keyboard-series devices, which do not accept power over the GPIO header.
