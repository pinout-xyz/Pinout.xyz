<!--
---
name: Cananka
class: board
type: other
collected: Other
formfactor: HAT
manufacturer: Josip Medved
description: Cananka is Raspberry Pi HAT allowing for CAN bus communication.
url: https://medo64.com/cananka/
github: https://github.com/medo64/cananka/
image: 'medo64-cananka.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
  '4':
  '17':
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
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Interrupt
    mode: input
    active: low
  '23':
    mode: spi
  '24':
    mode: spi
-->
# Cananka

Cananka is Raspberry Pi HAT allowing for CAN bus communication.

Features include up to 1Mbit/s bus speed (125 kbit/s default); fully isolated
(1 kV); does not require CAN bus power supply (on-board DC-to-DC converter);
supports powering Raspberry Pi from CAN bus (up to 24 V, 2 A); automatic
detection via HAT specification; works on Raspberry Pi B+ and above (including
Pi Zero).
