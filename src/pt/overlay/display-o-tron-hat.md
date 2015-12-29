<!--
---
name: Display-o-Tron HAT
description: A 3-line character LCD with a 6-zone RGB backlight and 6 touch buttons
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '19':
    mode: spi
  '22':
    name: LCD Register Select
    mode: output
    active: high
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

You can use the one-line product installer to get Display-o-Tron HAT set up and ready to go, just:

```bash
curl get.pimoroni.com/dot3k | bash
```

And follow the instructions!
