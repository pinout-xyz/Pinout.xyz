<!--
---
name: Serial Pi Plus
class: board
type: com
formfactor: Custom
manufacturer: AB Electronics UK
description: UART to RS232 Converter
url: https://www.abelectronics.co.uk/p/51/serial-pi-plus
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-serial-pi-plus.pdf
buy: https://www.abelectronics.co.uk/p/51/serial-pi-plus
image: 'ab-serial-pi-plus.png'
pincount: 40
eeprom: no
power:
  '1':
ground:
  '6':
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
#Serial Pi Plus

Serial Pi Plus es un convertidor en serie UART a RS232 para el Raspberry Pi.

El puerto RS232 está conectado al puerto UART en la Raspberry Pi usando una interfaz MAX3232. El MAX3232 IC convierte el puerto UART de 3.3V a voltajes RS232 permitiendo la comunicación con dispositivos compatibles con RS232 a través de un cable serial DB9 o con el uso de un cable de módem nulo, la placa permite el acceso a la terminal con Linux en Raspberry Pi usando una aplicación de terminal. Se puede acceder al puerto RS232 a través del puerto DB9 o los puntos de soldadura en la PCB.

##Características

- Puerto maestro RS232.
- Controle Raspberry Pi a través de RS232 o conéctese a accesorios seriales externos.
- Combinable con otras placas accesorias Raspberry Pi.
- Orificios de montaje para usar con los kits de montaje de AB Electronics UK (se venden por separado)
[Configuring the RS232 communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
