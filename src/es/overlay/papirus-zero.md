<!--
---
name: PaPiRus Zero
class: board
type: display
formfactor: pHAT
manufacturer: Pi Supply
description: PaPiRus Zero is an ePaper / eInk screen pHAT module for the Pi Zero
url: https://www.kickstarter.com/projects/pisupply/papirus-the-epaper-screen-hat-for-your-raspberry-p
github: https://github.com/PiSupply/PaPiRus
buy: https://www.pi-supply.com/product/papirus-zero-epaper-screen-phat-pi-zero/
image: 'papirus-zero.png'
pincount: 40
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
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    name: Border Control
  '10':
    name: Discharge
  '11':
    name: Temp Sens
  '16':
    name: Panel On
  '18':
    name: Chip On Glass Reset
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Chip On Glass Busy
  '23':
    mode: spi
  '24':
    mode: spi
  '26':
    mode: spi
  '35':
    name: SW4
    mode: input
    active: low
  '36':
    name: SW2
    mode: input
    active: low
  '37':
    name: SW5
    mode: input
    active: low
  '38':
    name: SW3
    mode: input
    active: low
  '40':
    name: SW1
    mode: input
    active: low
i2c:
  '0x48':
    name: Temperature Sensor
    device: LM75BD
-->
#PaPiRus Zero

PaPiRus Zero es una pantalla ePaper versátil para Raspberry Pi, con tamaños desde 1.44" a 2.0".

A diferencia de las pantallas convencionales, refleja la luz y puede mantener imagen y textos por tiempo indefinido, hasta sin electricidad. Esta pantalla no requiere electricidad para mantener la imagen y durará varios días hasta desaparecer. Se puede leer a la luz del día y tiene un gran contraste.

* Tamaños de pantalla intercambiables (1.44" o 2.0")
* Memoria Flash de 32MBit
* Control de temperatura digital
* Pines GPIO accesibles
* Cuenta con 6 interruptores opcionales

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sSL https://pisupp.ly/papiruscode | sudo bash
```
