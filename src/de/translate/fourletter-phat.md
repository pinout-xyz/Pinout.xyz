<!--
---
name: Four Letter pHAT
class: board
type: display
formfactor: pHAT
manufacturer: Pimoroni
description: A four 14-segment displays for the Raspberry Pi
url: https://shop.pimoroni.com/products/four-letter-phat
github: https://github.com/pimoroni/fourletter-phat
buy: https://shop.pimoroni.com/products/four-letter-phat
image: 'fourletter-phat.png'
pincount: 40
eeprom: yes
power:
  '2':
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
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x70':
    name: Matrix Driver
    device: HT16K33
-->
# Four Letter pHAT

Four Letter pHAT is a four 14-segment display that can be used to display text, numbers, and a host of other characters. Its Matrices are a retro-style green, similar to old digital alarm clock and are driven by the HT16K33 chip over I2C.

Features:

* Four 14-segment displays
* HT16K33 driver chip
* Compatible with Raspberry Pi A+/B+, 2, 3 and Zero/Zero W

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl https://get.pimoroni.com/fourletterphat | bash
```
