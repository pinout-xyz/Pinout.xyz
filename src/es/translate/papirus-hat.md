<!--
---
name: PaPiRus HAT
class: board
type: display
formfactor: HAT
manufacturer: Pi Supply
description: PaPiRus is an ePaper / eInk screen HAT module for the Raspberry Pi
url: https://www.kickstarter.com/projects/pisupply/papirus-the-epaper-screen-hat-for-your-raspberry-p
github: https://github.com/PiSupply/PaPiRus
buy: https://www.pi-supply.com/product/papirus-epaper-eink-screen-hat-for-raspberry-pi/
image: 'papirus-hat.png'
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
  '8':
    name: Border Control
  '10':
    name: Discharge
  '11':
    name: Temp Sens          
  '12':
    name: ePaper PWM
  '13':
    name: RTC
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
  '36':
    name: Button 1
    mode: input
    active: low
  '37':
    name: Button 2
    mode: input
    active: low  
  '38':
    name: Button 3
    mode: input
    active: low
  '40':
    name: Button 4
    mode: input
    active: low
-->
#PaPiRus HAT

PaPiRus HAT es una pantalla ePaper versátil para Raspberry Pi, con tamaños desde 1.44" a 2.7".

A diferencia de las pantallas convencionales, refleja la luz y puede mantener imagen y textos por tiempo indefinido, hasta sin electricidad. Esta pantalla no requiere electricidad para mantener la imagen y durará varios días hasta desaparecer. Se puede leer a la luz del día y tiene un gran contraste.

* El diseño cumple el estándar HAT
* Tamaños de pantalla intercambiables (1.44", 2.0" o 2.7")
* Memoria Flash de 32MBit
* Cuenta con un reloj de tiempo real alimentado por batería (batería CR2032 incluída)
* Formato plug and play con EEPROM
* Control de temperatura digital
* Pines GPIO accesibles
* Pin de reset opcional
* Cuenta con 4 interruptores opcionales

Para configurar el HAT puedes utilizar el instalador online de una línea.

```bash
curl -sSL https://goo.gl/i1Imel | sudo bash
```

Antes de utilizar PaPiRus activa las interfaces SPI e I2C
