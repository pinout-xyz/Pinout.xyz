<!--
---
name: Flick HAT
class: board
type: gesture
formfactor: HAT
manufacturer: Pi Supply
description: Flick HAT is a 3D tracking and gesture pHAT.
url: https://www.pi-supply.com/product/flick-large-standalone-3d-tracking-gesture-breakout/
github: https://github.com/PiSupply/Flick
buy: https://www.pi-supply.com/product/flick-hat-3d-tracking-gesture-hat-raspberry-pi/
image: 'flick-hat.png'
pincount: 40
eeprom: setup
power:
  '1':
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
  '11':
    name: Reset
  '13':
    name: TS
i2c:
  '0x42':
    name: Gesture controller
    device: MGC3130
-->
# Flick HAT
Integra Flick en tu proyecto I2C para  múltiples formas de controlarlo. Con la tecnología de gestos de campo cercano, puedes ocultar tu proyecto detrás de material no conductor (madera / acrílico) y seguir utilizando Flick.

* Seguimiento 3D
* Gesto de detección hasta 15cm.
* Reconoce toque y pulsación
* Se comunica con la Raspberry Pi a través de I2C.
* No requiere soldadura
* Chip regulador para permitir que la placa funcione con 3V3 o 5V de potencia
* Instalador de una línea
* Totalmente CE y FCC probado y aprobado
