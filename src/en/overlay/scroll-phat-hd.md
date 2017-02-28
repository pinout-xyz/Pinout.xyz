<!--
---
name: Scroll pHAT HD
class: board
type: display, led
formfactor: pHAT
manufacturer: Pimoroni
description: A 17 x 7 LED matrix
url: https://github.com/pimoroni/scroll-phat-hd
github: https://github.com/pimoroni/scroll-phat-hd
buy: https://shop.pimoroni.com/products/scroll-phat-hd
image: 'scroll-phat-hd.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x74':
    name: Matrix LED driver
    device: IS31FL3731
-->
#Scroll pHAT HD

Scroll pHAT HD provides a matrix of 119 white LED pixels that is ideal for writing messages, showing graphs, and drawing pictures. Perfect for RPi Zero but works with A+/B+/2 too!

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/scrollphathd | bash
```

Then import it into your Python script and start tinkering:

```bash
import scrollphathd
```
