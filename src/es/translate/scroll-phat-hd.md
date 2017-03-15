<!--
---
name: Scroll pHAT HD
class: board
type: display, led
formfactor: pHAT
manufacturer: Pimoroni
description: A 17 x 7 LED matrix
url: https://github.com/pimoroni/scroll-phat-hd
github: https://github.com/pimoroni/scroll-phat-hd
buy: https://shop.pimoroni.com/products/scroll-phat-hd
image: 'scroll-phat-hd.png'
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
  '0x74':
    name: Matrix LED driver
    device: IS31FL3731
-->
#Scroll pHAT HD

Scroll pHAT HD proporciona una matriz de 119 píxeles LED blancos, ideal para escribir mensajes, mostrar gráficas o hacer dibujos. Es perfecto para RPi Zero pero también funciona con A+/B+/2.

Para poner el pHAT en funcionamiento puedes utilizar nuestro código de una línea:

```bash
curl -sS https://get.pimoroni.com/scrollphathd | bash
```
Luego impórtalo en tu script Python y comienza a desarrollar:

```bash
import scrollphathd
```
