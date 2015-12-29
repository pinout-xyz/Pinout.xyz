<!--
---
name: Display-o-Tron 3000
manufacturer: Pimoroni
github: https://github.com/pimoroni/dot3k
url: https://github.com/pimoroni/dot3k
description: Un LCD de 3 líneas con luz RGB de fondo y un joystick
install:
  'devices':
    - 'i2c'
    - 'spi'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'dot3k'
  'examples': 'python/examples/'
pincount: 26
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Botón del Joystick
    mode: entrada
    active: bajo (apagado)
  '11':
    name: Joystick Izquierda
    mode: entrada
    active: bajo (apagado)
  '13':
    name: Joystick Arriba
    mode: entrada
    active: bajo (apagado)
  '15':
    name: Joystick Derecha
    mode: entrada
    active: bajo (apagado)
  '19':
    mode: spi
  '21':
    name: Joystick Abajo
    mode: entrada
    active: bajo (apagado)
  '22':
    name: LCD CMD/DATA
    mode: salida
    active: alto (encendido)
  '23':
    mode: spi
-->
#Display-o-Tron 3000

Puedes usar la siguiente línea para instalar, preparar y dejar listo para el uso el Display-o-Tron 3000:

```bash
curl -sS get.pimoroni.com/dot3k | bash
```

¡Y sigue las instrucciones!
