<!--
---
name: 1 Wire Pi Plus
class: board
type: com
formfactor: HAT
manufacturer: AB Electronics UK
description: 1-Wire to I2C host interface
url: https://www.abelectronics.co.uk/p/60/1-wire-pi-plus
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-1-wire-pi-plus-v2.pdf
buy: https://www.abelectronics.co.uk/p/60/1-wire-pi-plus
image: 'ab-1-wire-pi-plus.png'
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
    alternate: ['0x19', '0x1A', '0x1B']
    name: DS2482
    device: DS2482-100
-->
#1 Wire Pi Plus

1 Wire Pi Plus de AB Electronics UK es una placa de comunicación que admite el protocolo 1-Wire® diseñado para su uso en la Raspberry Pi. También se proporciona un puerto I2C amortiguado de 5V en la placa.

El puerto 1-Wire® en 1 Wire Pi Plus se basa en un dispositivo de puente DS2482-100 I2C a 1-Wire®. El DS2482-100 proporciona conversión de protocolo bidireccional entre el puerto I2C en la Raspberry Pi y cualquier dispositivo esclavo 1-Wire® conectado. Se utiliza un diodo de protección ESD para proteger 1 Wire Pi Plus y Raspberry Pi de picos electrostáticos en el puerto 1-Wire®. Las conexiones al puerto 1-Wire® se pueden realizar a través del zócalo RJ-12 o los puntos de soldadura en la PCB.

Los puentes de soldadura de selección de dirección I2C le permiten configurar la dirección I2C del 1 Wire Pi Plus permitiendo que la placa se use con otros dispositivos I2C en el mismo bus.

[https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi](https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi "Configuring and using the 1-Wire® port on your Raspberry Pi")
