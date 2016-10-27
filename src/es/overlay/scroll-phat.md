<!--
---
name: Scroll pHAT
class: board
type: display, led
formfactor: pHAT
manufacturer: Pimoroni
description: A 11 x 5 LED matrix
url: https://github.com/pimoroni/scroll-phat
github: https://github.com/pimoroni/scroll-phat
buy: https://shop.pimoroni.com/products/scroll-phat
image: 'scroll-phat.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x60':
    name: Matrix LED driver
    device: IS31FL3730
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
  'python':
    - 'scrollphat'
  'python3':
    - 'scrollphat'
-->
#Scroll pHAT

Scroll pHAT proporciona una matriz de 55 LED blancos en formato píxel que es ideal para escribir mensajes, mostrar gráficas y dibujar. Perfecto para RPi Zero pero también funciona con A+/B+/2.


Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/scrollphat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import scrollphat
```
