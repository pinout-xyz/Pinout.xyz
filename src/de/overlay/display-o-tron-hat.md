<!--
---
name: Display-o-Tron HAT
class: board
type: display
formfactor: HAT
manufacturer: Pimoroni
description: Ein 3-zeiliges LCD mit einer 6-Zonen RGB Hintergrundbeleuchtung und 6 Tasten
url: https://shop.pimoroni.com/products/display-o-tron-hat
github: https://github.com/pimoroni/displayotron
buy: https://shop.pimoroni.com/products/display-o-tron-hat
image: 'display-o-tron-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
  '2':
ground:
  '6':
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  22:
    name: LCD CMD/DATA
    mode: output
    active: high
  19:
    mode: spi
  22:
    name: LCD Register Select
    mode: output
  23:
    mode: spi
  24:
    name: LCD Chip Select
    mode: chipselect
    active: high
  32:
    name: LCD Reset
    mode: output
    active: low
-->
#Display-o-Tron HAT

Der Display-o-Tron HAT benutzt den SPI- und I2C-Bus um das LC-Display, die Hintergrundbeleuchtung und die Tasten zu steuern bzw. abzufragen.
Beide Busse können aber weiterhin noch mit anderen Komponenten genutzt werden.

Mit diesem Einzeiler installierst Du den Display-o-Tron HAT:

```bash
curl -sS https://get.pimoroni.com/dot3k | bash
```

...den Rest findest Du in der Anleitung auf Github :-)
