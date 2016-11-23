<!--
---
name: Skywriter HAT
class: board
type: gestos
formfactor: HAT
manufacturer: Pimoroni
description: Un sensor posicional y de gestos 3D
url: http://shop.pimoroni.com/products/skywriter-hat
github: https://github.com/pimoroni/skywriter-hat
buy: http://shop.pimoroni.com/products/skywriter-hat
image: 'skywriter-hat.png'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transferencia
i2c:
  '0x42':
    name: Gesture sensor
    device: mgc3130
-->
#Skywriter HAT

El Skywriter HAT detecta la posición de tu dedo en 3 dimensiones, retornando X, Y y Z, que puedes usar en
tus programas de Python.

También reconoce gestos, incluyendo swipes y más.

Para instalar este HAT y dejarlo preparado para el uso, ejecuta:

```bash
curl -sS https://get.pimoroni.com/skywriter | bash
```

¡Y sigue las instrucciones!
