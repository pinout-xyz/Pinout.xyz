<!--
---
description: Una placa completa, con luz, entradas, entradas táctiles y salidas.
pin:
  '15':
    name: Entrada 2
  '16':
    name: Entrada 1
  '18':
    name: Entrada 3
  '22':
    name: Entrada 4
  '31':
    name: Salida 1
  '32':
    name: Salida 2
  '33':
    name: Salida 3
  '36':
    name: Salida 4
-->
# Explorer HAT

Entradas y salidas de 5V, paneles táctiles y LEDs componen el Explorer HAT.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
