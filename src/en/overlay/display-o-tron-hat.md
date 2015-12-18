<!--
---
name: Display-o-Tron HAT
manufacturer: Pimoroni
url: https://github.com/pimoroni/dot3k
description: A 3-line character LCD with a 6-zone RGB backlight and 6 touch buttons
pincount: 40
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '19':
    mode: spi
  '22':
    name: LCD Register Select
    mode: output
  '23':
    mode: spi
  '24':
    name: LCD Chip Select
    mode: chipselect
    active: high
  '32':
    name: LCD Reset
    mode: output
    active: low
-->
#Display-o-Tron HAT

Display-o-Tron HAT uses both SPI and I2c to drive the LCD display, backlight and touch. 
However both of these busses can be shared with other devices.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

And follow the instructions!
