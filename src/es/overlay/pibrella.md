<!--
---
name: Pibrella
class: board
type: io,multi
formfactor: Otro
manufacturer: Cyntech
description: Luz, sonido, entradas y salidas en una placa.
url: http://pibrella.com
github: https://github.com/pimoroni/pibrella
buy: https://shop.cyntech.co.uk/products/pibrella?variant=581387897
image: 'pibrella.png'
pincount: 26
eeprom: no
pin:
  '7':
    name: LED Verde
    direction: salida
    active: alto (encendido)
  '11':
    name: LED Amarillo
    direction: salida
    active: alto (encendido)
  '12':
    name: Zumbador
    direction: salida
    active: alto (encendido)
  '13':
    name: LED Rojo
    direction: salida
    active: alto (encendido)
  '15':
    name: Salida A
    direction: salida
    active: alto (encendido)
  '16':
    name: Salida B
    direction: salida
    active: alto (encendido)
  '18':
    name: Salida C
    direction: salida
    active: alto (encendido)
  '19':
    name: Entrada D
    direction: salida
    active: alto (encendido)
  '21':
    name: Entrada A
    direction: input
    active: alto (encendido)
  '22':
    name: Salida D
    direction: salida
    active: alto (encendido)
  '23':
    name: Botón
    direction: input
    active: alto (encendido)
  '24':
    name: Entrada C
    direction: input
    active: alto (encendido)
  '26':
    name: Entrada B
    direction: input
    active: alto (encendido)
-->
#Pibrella

La placa todo en uno con luz, sonido, entradas y salidas de Pimoroni vs Cyntech usa un montón de pines de entrada/salida en la Pi, pero deja tanto el puerto Serial como el I2c libres, dejando un montón de espacio por si te pones creativo.

Pibrella es fácil de usar, primero debes instalar el módulo usando LXTerminal/línea de comandos:

```bash
curl -sS get.pimoroni.com/pibrella | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import pibrella
pibrella.light.red.on()
```
