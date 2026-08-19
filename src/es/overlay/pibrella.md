<!--
---
name: Pibrella
class: board
type: multi,io
formfactor: Custom
manufacturer: Cyntech
collected: Other
description: Luz, sonido, entradas y salidas en una placa.
url: http://pibrella.com
github: https://github.com/pimoroni/pibrella
buy: https://shop.cyntech.co.uk/products/pibrella?variant=581387897
image: 'pibrella.png'
pincount: 26
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
pin:
  '7':
    name: LED Verde
    direction: output
    active: high
  '11':
    name: LED Amarillo
    direction: output
    active: high
  '12':
    name: Zumbador
    direction: output
    active: high
  '13':
    name: LED Rojo
    direction: output
    active: high
  '15':
    name: Salida E
    direction: output
    active: high
  '16':
    name: Salida F
    direction: output
    active: high
  '18':
    name: Salida G
    direction: output
    active: high
  '19':
    name: Entrada D
    direction: output
    active: high
  '21':
    name: Entrada A
    direction: input
    active: high
  '22':
    name: Salida H
    direction: output
    active: high
  '23':
    name: Botón
    direction: input
    active: high
  '24':
    name: Entrada C
    direction: input
    active: high
  '26':
    name: Entrada B
    direction: input
    active: high
-->
# Pibrella

La placa todo en uno con luz, sonido, entradas y salidas de Pimoroni vs Cyntech usa un montón de pines de entrada/salida en la Pi, pero deja tanto el puerto Serial como el I2c libres, dejando un montón de espacio por si te pones creativo.

Pibrella es fácil de usar, primero debes instalar el módulo usando LXTerminal/línea de comandos:

```bash
curl -sS https://get.pimoroni.com/pibrella | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import pibrella
pibrella.light.red.on()
```
