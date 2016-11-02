<!--
---
name: 1 Wire Pi Zero
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics
description: 1-Wire to I2C host interface
url: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/stock/raspberrypi/1wirepizero/1wirepizero-schematic.png
buy: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
image: 'ab-1-wire-pi-zero.png'
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
i2c:
  '0x18':
    name: DS2482
    device: DS2482-100
-->
#1 Wire Pi Zero

1 Wire Pi Zero fabricada por AB Electronics UK es una placa de comunicación que funciona con el protocolo 1-Wire® y ha sido diseñada para Raspberry Pi Zero. Además cuenta con un puerto I2C de 5V regulable.

El puerto 1-Wire® en 1 Wire Pi Zero está basado en el dispositivo puente DS2482-100 I2C a 1-Wire®. El DS2482-100 proporciona una conversión bidireccional entre el puerto I2C en Raspberry Pi y cualquier dispositivo 1-Wire® conectado como esclavo. Un diodo de protección ESD se utiliza para proteger 1 Wire Pi Zero y Raspberry Pi de descargas electrostáticas en el puerto 1-Wire®. Las conexiones al puerto 1-Wire® se pueden hacer a través del enchufe RJ-12 o soldando puntos en el PCB.

Mediante cables jumper se puede seleccionar la dirección I2C de 1 Wire Pi Zero permitiendo su uso con otros dispositivos I2C en el mismo puerto.

[https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi](https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi "Configuring and using the 1-Wire® port on your Raspberry Pi")
