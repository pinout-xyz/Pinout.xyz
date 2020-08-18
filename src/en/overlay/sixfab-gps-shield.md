<!--
---
name: GPS Shield
class: board
type: gps
formfactor: pHAT
manufacturer: Sixfab
description: A GPS add-on board for Raspberry Pi
url: https://sixfab.com/product/gps-shield/
buy: https://sixfab.com/product/gps-shield/
image: 'sixfab-gps-shield.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
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
  '7':
    mode: 1-wire
  '8':
    mode: uart
  '10':
    mode: uart
  '12':
    name: 
  '18':
    name: 1-PPS    
  '22':
    name: Reset
  '40':
    name: User Led
-->
# GPS Shield

The sixfab GSP Shield  is an easy way to add GPS to your Raspberry Pi.

## Features include

* Location, Time, Speed all on the same NMEA Protocol
* Built-in antenna
* 1-Wire sensor breakout (bcm4)
* Programmable from Linux, MacOS, Windows, Android
