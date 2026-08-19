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
i2c:
  '0x28':
    name: Sensor capacitivo
  '0x48':
    name: Entrada Analógica
-->
# Explorer HAT Pro

Entradas y salidas de 5V, paneles táctiles, LEDs, entradas analógicas y un Puente-H para controlar motores componen el Explorer HAT Pro.

Para preparar e instalar el HAT utiliza la siguiente línea:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import explorerhat
explorerhat.light.on()
```
