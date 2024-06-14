<!--
---
name: Sixfab XBee Shield V2
class: board
type: com
formfactor: pHAT
manufacturer: Sixfab
description: Use XBee modules with the Raspberry Pi
url: http://sixfab.com/product/xbee-shield/
buy: http://sixfab.com/product/xbee-shield/
image: 'sixfab-xbee-shield-v2.png'
pincount: 40
eeprom: no
power:
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
  '7':
    mode: 1-wire
  '8':
    mode: uart
  '10':
    mode: uart
  '11':
    mode: output
    name: RTS
  '13':
    mode: output
    name: XBee_Reset
  '18':
    mode: output
    name: XBee_IO1
  '22':
    mode: output
    name: XBee_IO1
  '32':
    mode: output
    name: IN1
  '36':
    mode: output
    name: RSSI
  '38':
    mode: input
    name: User Button
  '40':
    mode: output
    name: User Led
-->
# Sixfab XBee Shield V2

The Sixfab XBee Shield is add-on board that allows you to use XBee modules easily with your Pi.

## Features include

* Headers fit most XBee modules
* Up to 28 miles range
* Point to point communication
* Communication LED
* 1-Wire sensor breakout (bcm4)
* Programmable from Linux, Windows and Android
