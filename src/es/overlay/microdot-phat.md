<!--
---
name: Micro Dot pHAT
class: board
type: led
formfactor: pHAT
manufacturer: Pimoroni
description: An LED matrix display board for the Raspberry Pi
url: http://blog.pimoroni.com/micro-dot-phat/
github: https://github.com/pimoroni/microdot-phat
buy: https://shop.pimoroni.com/products/microdot-phat
image: 'microdot-phat.png'
pincount: 40
eeprom: no
power:
  '2':
ground:
  '6':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x63':
    name: LED matrix 1-2
    device: IS31FL3730
  '0x62':
    name: LED matrix 3-4
    device: IS31FL3730
  '0x61':
    name: LED matrix 5-6
    device: IS31FL3730
-->
#Micro Dot pHAT

Una placa con una matriz LED descarada, de vieja escuela, con hasta 30x7 pixels utilizando las matrices Lite-On LTP-305 (o cualquiera similar). Perfecta para construir un mensaje en movimiento retro, un pequeño analizador de espectro de 30 bandas o un reloj retro.

La placa utiliza tres chip IS31FL3730 para controlar la matriz, cada  uno controla dos matrices. La placa y el software fuero diseñados para trabajar de manera eficiente, actualizando realmente rápido.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/microdotphat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import microdotphat
```
