<!--
---
name: Display-o-Tron 3000
description: Ein 3-zeiliges LCD mit RGB Hintergrundbeleuchtung und Joystick
pincount: 26
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Joystick Taste
    mode: input
    active: low
  '11':
    name: Joystick links
    mode: input
    active: low
  '13':
    name: Joystick oben
    mode: input
    active: low
  '15':
    name: Joystick rechts
    mode: input
    active: low
  '19':
    mode: spi
  '21':
    name: Joystick unten
    mode: input
    active: low
  '22':
    name: LCD CMD/DATA
    mode: output
    active: high
  '23':
    mode: spi
-->
#Display-o-Tron 3000

Mit diesem Einzeiler installierst Du das Display-o-Tron 3000:

```bash
curl get.pimoroni.com/dot3k | bash
```

...den Rest findest Du in der Anleitung auf Github :-)
