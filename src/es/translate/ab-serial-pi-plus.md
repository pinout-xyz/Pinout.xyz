<!--
---
name: Serial Pi Plus
class: board
type: com
formfactor: HAT
manufacturer: AB Electronics
description: UART to RS232 Converter
url: https://www.abelectronics.co.uk/p/51/Serial-Pi-Plus
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/51/Serial-Pi-Plus
image: 'ab-serial-pi-plus.png'
pincount: 40
eeprom: no
power: 3v3
pin:
  '8':
    mode: UART
  '10':
    mode: UART
-->
#Serial Pi Plus

Serial Pi Plus es un coversor UART a RS232 serie para Raspberry Pi.

El puerto RS232 se conecta al puerto UART de Raspberry Pi utilizando una interfaz MAX2323. MAX3232 IC convierte los 3.3V del puerto UART a voltajes RS232 permitiendo la comunicación con dispositivos compatibles con RS232 mediante un cable serie DB) o con el uso de un cable null-modem que permita elacceso mediante terminal a Raspberry Pi. El puerto RS232 puede accederse a partir del puerto DB9 o soldando en el PCB.

##Especificaciones

- Puerto maestro RS232.
- Control de Raspberry Pi con RS232 o permitir la conexión de accesorios externos.
- Acoplable con otras placas para Raspberry Pi A+, B+ o 2 modelo B.
- Diseñada para montarse con los kits de montaje de AB Electronics UK (vendidos por separado)

[Configuring the RS232 communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
