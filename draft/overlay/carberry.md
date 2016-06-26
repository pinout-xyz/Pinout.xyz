<!--
---
name: Carberry
class: board
type: other
formfactor: Custom
image: 'carberry.png'
manufacturer: Paser
description: add-on board designed to inteface with car electronics
url: http://www.carberry.it/en/p/347/Carberry/
buy: http://www.carberry.it
pincount: 26
eeprom: no
power:
  '2':
ground:
  '6':
pin:
  '8':
    name: TXD / Transmit
    direction: output
  '10':
    name: RXD / Receive
    direction: input
  '12':
    name: LIRC
  '13':
    name: Shutdown
-->
#Carberry

Carberry is an add-on board for Raspberry Pi that can be used to inteface between car electronics and your Pi. It allows the development of end-user applications, such as media centers, vehicle diagnostics, data logging, fleet management, tracking, blackboxes, burglar alarms, carputing, internet, and much more.