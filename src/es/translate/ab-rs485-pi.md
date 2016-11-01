<!--
---
name: RS485 Pi
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics
description: UART to RS485 Converter
url: https://www.abelectronics.co.uk/p/77/RS485-Pi
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/77/RS485-Pi
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

RS485 Pi es un conversor UART a RS485 para Raspberry Pi.

El puerto RS485 se conecta al puerto UART de Raspberry Pi usando la interfaz SN65HVD72. La interfaz SN65HVD72 IC convierte los 3.3V del puerto UART a voltages diferenciales RS485 permitiendo la comunicación con dispositivos compatibles con RS485 mediante un cable. El puerto RS485 es accesible mediante el puerto DB9 o soldando en el PCB.

RS485 Pi tiene protección contra picos de voltage gracias a un diodo TVS y dos resistencias de 100. La placa también cuenta con una resistencia de 1200.

##Especificaciones

- Puerto RS-485.
- Tasa de transferencia de hasta 250 kbps.
- Utiliza la Raspberry Pi para controlar dispositivos RS-485.
- Acoplable con otras placas adicionales para Raspberry >Pi.
- Agujeros de montaje para el kit de montaje de AB Electronics UK (vendido por separado)

[Configuring the UART communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
