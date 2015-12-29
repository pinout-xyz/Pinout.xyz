<!--
---
name: Skywriter HAT
description: Un sensor posicional y de gestos 3D
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transferencia
-->
#Skywriter HAT

El Skywriter HAT detecta la posición de tu dedo en 3 dimensiones, retornando X, Y y Z, que puedes usar en
tus programas de Python.

También reconoce gestos, incluyendo swipes y más.

Para instalar este HAT y dejarlo preparado para el uso, ejecuta:

```bash
curl -sS get.pimoroni.com/skywriter | bash
```

¡Y sigue las instrucciones!
