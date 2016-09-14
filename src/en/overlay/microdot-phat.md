<!--
---
name: Micro Dot pHAT
class: board
type: display, led
formfactor: pHAT
manufacturer: Pimoroni
description: An LED matrix display board for the Raspberry Pi
url: http://blog.pimoroni.com/micro-dot-phat/
github: https://github.com/pimoroni/microdot-phat
buy: https://shop.pimoroni.com/products/microdot-phat
image: 'microdot-phat.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x63':
    name: LED matrix 1-2
    device: IS31FL3730
  '0x62':
    name: LED matrix 3-4
    device: IS31FL3730
  '0x61':
    name: LED matrix 5-6
    device: IS31FL3730
-->
#Micro Dot pHAT

An unashamedly old school LED matrix display board, with up to 30x7 pixels, using Lite-On LTP-305 matrices (or any similar matrices). Perfect for building a retro scrolling message display, a tiny 30-band spectrum analyser, or a retro clock.

The board uses three IS31FL3730 matrix driver chips, each driving two of the matrix displays. The board and supporting software was designed to use these driver chips in an efficient manner, in effect round-robin-ing them and updating them extremely quickly one after the other to drive two displays at once.

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/microdotphat | bash
```

Then import it into your Python script and start tinkering:

```bash
import microdotphat
```
