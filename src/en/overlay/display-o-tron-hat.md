<!--
---
name: Display-o-Tron HAT
class: board
type: display
formfactor: HAT
image: 'display-o-tron-hat.png'
manufacturer: Pimoroni
description: A 3-line character LCD with a 6-zone RGB backlight and 6 touch buttons
url: https://github.com/pimoroni/dot3k
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/display-o-tron-hat
pincount: 40
eeprom: yes
power:
  '1':
  '2':
ground:
  '6':
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

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/displayotron | bash
```

And follow the instructions!
