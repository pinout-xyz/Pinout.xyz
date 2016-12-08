<!--
---
name: Pan Tilt HAT
class: board
type: motor,led
formfactor: HAT
manufacturer: Pimoroni
description: A camera pan/tilt and lighting driver
url: https://shop.pimoroni.com/products/pan-tilt-hat
github: https://github.com/pimoroni/pantilt-hat
docs: https://docs.pimoroni.com/pantilthat
buy: https://shop.pimoroni.com/products/pan-tilt-hat
image: 'pantilthat.png'
pincount: 40
eeprom: yes
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
  '0x15':
    name: Servo And Light Driver
    device: PIC16F1503
-->
#Pan Tilt HAT

Pan Tilt HAT es un controlador servo de dos canales diseñado para controlar un pequeño montaje Pan/Tilt controlado por un servo. Además controla luces por PWM o píxels WS2812; hasta 24 RGB o 18 RGBW.

Pan Tilt HAT usa un PIC16F1503 con un firmware personalizado, funciona con i2c.

Para configurar el HAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/pantilthat | bash
```
Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import pantilthat
```
