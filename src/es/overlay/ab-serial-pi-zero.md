<!--
---
name: Serial Pi Zero
class: board
type: com
formfactor: pHAT
manufacturer: AB Electronics
description: UART to RS232 Converter
url: https://www.abelectronics.co.uk/p/75/Serial-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/75/Serial-Pi-Zero
image: 'ab-serial-pi-zero.png'
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
#Serial Pi Zero

Serial Pi Zero es un conversor UART a RS232 para Raspberry Pi Zero.

El puerto RS232 se conecta al puerto UART de Raspberry Pi mediante la interfaz MAX3232. La interfaz IC MAX3232 convierte los 3.3V del puerto UART a voltajes compatibles con RS232 permitiendo la comunicación con este tipo de dispositivos mediante un cable serie DB9 o un cable de modem, permitiendo acceder mediante terminal. El puerto RS232 puede accederse mediante el puerto DB9 o soldando en el PCB.

##Especificaciones

- Puerto maestro RS232.
-  Controla Raspberry Pi mediante RS232 o conecta dispositivos serie externos.
- Acoplable con otras placas para Raspberry Pi.
- Agujeros para montaje con el kit de montaje de AB Electronics UK (vendido por separado)

[Configuring the RS232 communication on the Raspberry Pi](https://www.abelectronics.co.uk/kb/article/20/raspberry-pi-serial-port-usage)
