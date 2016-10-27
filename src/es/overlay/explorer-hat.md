<!--
---
name: Explorer HAT
class: board
type: cap,io,multi
formfactor: HAT
manufacturer: Pimoroni
description: Una placa completa, con luz, entradas, entradas táctiles y salidas.
url: http://shop.pimoroni.com/products/explorer-hat
github: https://github.com/pimoroni/explorer-hat
buy: http://shop.pimoroni.com/products/explorer-hat
image: 'explorer-hat.png'
pincount: 40
eeprom: yes
pin:
  '7':
    name: LED 1
    mode: salida
    active: alto (encendido)
  '11':
    name: LED 2
    mode: salida
    active: alto (encendido)
  '13':
    name: LED 3
    mode: salida
    active: alto (encendido)
  '15':
    name: Entrada 2
    mode: entrada
    active: alto (encendido)
  '16':
    name: Entrada 1
    mode: entrada
    active: alto (encendido)
  '18':
    name: Entrada 3
    mode: entrada
    active: alto (encendido)
  '22':
    name: Entrada 4
    mode: entrada
    active: alto (encendido)
  '29':
    name: LED 4
    mode: salida
    active: alto (encendido)
  '31':
    name: Salida 1
    mode: salida
    active: alto (encendido)
  '32':
    name: Salida 2
    mode: salida
    active: alto (encendido)
  '33':
    name: Salida 3
    mode: salida
    active: alto (encendido)
  '36':
    name: Salida 4
    mode: salida
    active: alto (encendido)
-->
#Explorer HAT

Entradas y salidas de 5V, paneles táctiles y LEDs componen el Explorer HAT.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS get.pimoroni.com/explorerhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
