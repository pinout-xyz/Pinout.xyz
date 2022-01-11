<!--
---
name: 'Mote pHAT'
class: board
type: led
formfactor: pHAT
manufacturer: Pimoroni
description: 4 channel multiplexed APA102 driver
url: http://shop.pimoroni.com/products/mote-phat
github: https://github.com/pimoroni/mote-phat
buy: https://shop.pimoroni.com/products/mote-phat
image: 'mote-phat.png'
pincount: 40
eeprom: no
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
  '19':
    name: Data
    mode: output
    active: high
  '23':
    name: Clock
    mode: output
    active: high
  '24':
    name: Channel 1
    mode: output
    active: low
  '26':
    name: Channel 2
    mode: output
    active: low
  '22':
    name: Channel 3
    mode: output
    active: low
  '18':
    name: Channel 4
    mode: output
    active: low
-->

# Mote pHAT

Sports four Mote channels with microUSB connectors that can drive up to 64 RGB LEDs using four 16 pixel Mote strips.

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/motephat | bash
```
