<!--
---
description: Luz, sonido, entradas y salidas en una placa.
pin:
  '7':
    name: LED Verde
  '11':
    name: LED Amarillo
  '12':
    name: Zumbador
  '13':
    name: LED Rojo
  '15':
    name: Salida E
  '16':
    name: Salida F
  '18':
    name: Salida G
  '19':
    name: Entrada D
  '21':
    name: Entrada A
  '22':
    name: Salida H
  '23':
    name: Botón
  '24':
    name: Entrada C
  '26':
    name: Entrada B
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
