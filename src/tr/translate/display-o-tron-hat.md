<!--
---
name: Display-o-Tron HAT
class: board
type: display
formfactor: HAT
manufacturer: Pimoroni
description: A 3-line character LCD with a 6-zone RGB backlight and 6 touch buttons
url: https://shop.pimoroni.com/products/display-o-tron-hat
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/display-o-tron-hat
image: 'display-o-tron-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '39':
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
i2c:
  '0x54':
    name: Backlight
    device: sn3218
  '0x2c':
    name: Cap Touch
    device: cap1166
-->
#Display-o-Tron HAT

Display-o-Tron HAT uses both SPI and I2c to drive the LCD display, backlight and touch. However both of these busses can be shared with other devices.

To get the HAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/displayotron | bash
```

And follow the instructions!
