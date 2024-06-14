<!--
---
name: Display-o-Tron 3000
class: board
type: display
formfactor: Custom
manufacturer: Pimoroni
description: A 3-line character LCD with an RGB backlight and joystick
url: https://shop.pimoroni.com/products/displayotron-3000
github: https://github.com/pimoroni/dot3k
buy: https://shop.pimoroni.com/products/displayotron-3000
image: 'display-o-tron.png'
pincount: 26
eeprom: no
power:
  '2':
  '17':
ground:
  '6':
  '9':
  '14':
  '25':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Joystick Button
    mode: input
    active: low
  '11':
    name: Joystick Left
    mode: input
    active: low
  '13':
    name: Joystick Up
    mode: input
    active: low
  '15':
    name: Joystick Right
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick Down
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
i2c:
  '0x54':
    name: Backlight
    device: sn3218
-->
# Display-o-Tron 3000

The Display-o-Tron 3000 is a 3-line character LCD with an RGB back-light and joystick

To get the module set up and ready to go you can use the one-line product installer:

```bash
curl -sS https://get.pimoroni.com/displayotron | bash
```

And follow the instructions!
