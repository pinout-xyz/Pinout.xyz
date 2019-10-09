<!--
---
name: RS485 Pi
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics UK
description: UART to RS485 Converter
url: https://www.abelectronics.co.uk/p/77/rs485-pi
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-rs485pi.pdf
buy: https://www.abelectronics.co.uk/p/77/rs485-pi
image: 'ab-rs485-pi.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '8':
    mode: UART
  '10':
    mode: UART
-->
#RS485 Pi

RS485 Pi es un convertidor en serie UART a RS485 para el Raspberry Pi.

El puerto RS485 está conectado al puerto UART en la Raspberry Pi usando una interfaz SN65HVD72. El IC SN65HVD72 convierte el puerto UART de 3.3V a voltajes diferenciales RS485 permitiendo la comunicación con dispositivos compatibles con RS485 a través de un cable de par trenzado. Se puede acceder al puerto RS485 a través del puerto DB9 o los puntos de soldadura en la PCB.

RS485 Pi contiene protección contra picos de voltaje en forma de un diodo TVS y dos resistencias de película gruesa a prueba de pulsos de 10O. Se incluye una resistencia de terminación 120O con la placa.

##Características

- Puerto RS-485 Half Duplex.
- Velocidad de transferencia de hasta 250 kbps.
- Use Raspberry Pi para controlar dispositivos externos RS-485.
- Combina con otras placas accesorias Raspberry Pi.
- Orificios de montaje para usar con los kits de montaje de AB Electronics UK (se venden por separado)
[Configuring the UART communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
