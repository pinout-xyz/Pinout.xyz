<!--
---
name: Drum HAT
class: board
type: cap
formfactor: HAT
manufacturer: Pimoroni
description: An 8 pad finger Drum HAT for your Raspberry Pi
url: http://shop.pimoroni.com/products/drum-hat
github: https://github.com/pimoroni/drum-hat
buy: http://shop.pimoroni.com/products/drum-hat
image: 'drum-hat.png'
pincount: 40
eeprom: yes
power:
  '2':
  '17':
ground:
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '22':
    name: Alert
    mode: input
  '40':
    name: Reset
    mode: output
i2c:
  '0x2c':
    name: Cap Touch
    device: cap1188
-->
#Drum HAT

Drum HAT es la compañía perfecta para Piano HAT. Utiliza el mismo sensor táctical para crear 8 pads del tamaño de un dedo. Utilízalo para hacer música con Python, controlar software musical en tu Pi, controlar instrumentos o que forme parte de un proyecto mayor.

Especificaciones: 8 botones sensibles al tacto y 8 LEDs. Funciona con Piano HAT (usa el chip CAP1188 en una dirección i2c no conflictiva en 0x2c)

Para configurar el HAT puedes utilizar el instalador online de una línea.

```bash
curl -sS get.pimoroni.com/drumhat | bash
```
¡Y sigue las instrucciones!
