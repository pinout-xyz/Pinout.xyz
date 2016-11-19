<!--
---
name: Display-o-Tron 3000
class: board
type: alle
formfactor: Andere
manufacturer: Pimoroni
description: Ein 3-zeiliges LCD mit RGB Hintergrundbeleuchtung und Joystick
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
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  7:
    name: Joystick Taste
    mode: input
    active: low
  11:
    name: Joystick links
    mode: input
    active: low
  13:
    name: Joystick oben
    mode: input
    active: low
  15:
    name: Joystick rechts
    mode: input
    active: low
  19:
    mode: spi
  21:
    name: Joystick unten
    mode: input
    active: low
  22:
    name: LCD CMD/DATA
    mode: output
    active: high
  23:
    mode: spi
-->
#Display-o-Tron 3000

Mit diesem Einzeiler installierst Du das Display-o-Tron 3000:

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```

...den Rest findest Du in der Anleitung auf Github :-)
