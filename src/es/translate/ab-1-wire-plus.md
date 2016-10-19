<!--
---
name: 1 Wire Pi Plus
class: board
type: com
formfactor: HAT
manufacturer: AB Electronics
description: 1-Wire to I2C host interface
url: https://www.abelectronics.co.uk/p/60/1-Wire-Pi-Plus
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/60/1-Wire-Pi-Plus
image: 'ab-1-wire-pi-plus.png'
pincount: 40
eeprom: no
power: 3v3,5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x18':
    name: DS2482
    device: DS2482-100
-->
#1 Wire Pi Plus

1 Wire Pi Plus de AB Electronics UK es una placa de comunicación diseñada para Raspberry Pi A+, B+ y 2 modelo B, compatible con el protocolo 1-Wire®. La placa incluye un puerto I2C de 5V regulable.

El puerto 1-Wire® en 1 Wire Pi Plus está basado en el componente puente de DS2482-100 I2C a 1-Wire®. El DS2482-100 proporciona una protocolo de conversión bidireccional entre el puerto I2C en Raspberry Pi y cualquier dispositvo esclavo conectado a 1-Wire®. Se utiliza un diodo de protección ESD para proteger 1 Wire Pi Plus y Raspberry Pi de descargas electrostáticas en el puerto 1-Wire®. Las conexiones al puerto 1-Wire® se pueden realizar a través del conector RJ-12 o soldando en el PCB.

La librería Quick2wire  [https://github.com/quick2wire/quick2wire-python-api](https://github.com/quick2wire/quick2wire-python-api) permite un acceso sencillo al puerto I2C mediante Python.

[https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi](https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi "Configuring and using the 1-Wire® port on your Raspberry Pi")
