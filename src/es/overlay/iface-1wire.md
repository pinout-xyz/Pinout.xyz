<!--
---
name: 1-WIRE
class: interface
type: pinout
description: Raspberry Pi One-Wire pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/
pin:
  'bcm4':
    name: Data
-->
# W1-GPIO - One-Wire Interface

Para habilitar la interaz one-wire necesitas añadir la siguiente línea a /boot/config.txt y después reiniciar tu Pi:

```
dtoverlay=w1-gpio
```

También puedes habilitar la interfaz sobre la marcha, cuando sea necesario:

```
sudo modprobe w1-gpio
```

Tras realizar una de las dos acciones anteriores, puedes enumerar los dispositivos conectados al GPIO4 de tu Raspberry Pi (por defecto) con:

```
ls /sys/bus/w1/devices/
```
