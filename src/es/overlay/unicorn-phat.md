<!--
---
name: Unicorn pHAT
class: board
type: led
formfactor: pHAT
manufacturer: Pimoroni
description: 32 blindingly bright RGB LEDs on a single pHAT
url: http://shop.pimoroni.com/products/unicorn-phat
github: https://github.com/pimoroni/unicornhat
buy: http://shop.pimoroni.com/products/unicorn-phat
image: 'unicorn-phat.png'
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
  '12':
    name: Data
    direction: output
    mode: pwm
    active: high
    description: WS2812 Data
install:
  'apt':
    - 'python-dev'
    - 'python3-dev'
  'python':
    - 'unicornhat'
  'python3':
    - 'unicornhat'
-->
#Unicorn pHAT

32 LEDs brillantes, cegadores, dentro de un pHAT controlado por una librería C ultrarápida con la que puedes comunicarte mediante Python hacen del Unicorn HAT el hermano mayor, más brillate de PiGlow.

Nota: Unicorn pHAT usa un truco PWM, la misma técnica que hace que tu Pi pueda reproducir sonido a través del jack de audio (sonido analógico) así que no se pueden usar a la vez.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/unicornhat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import unicornhat
unicorn.set_layout(unicorn.PHAT)
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
