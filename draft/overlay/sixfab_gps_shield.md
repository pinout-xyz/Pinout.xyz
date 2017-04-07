<!--
---
name: Sixfab GPS Shield
class: board
type: gps
formfactor: PHAT
manufacturer: Sixfab
description: A GPS add-on board for Raspberry Pi
url: http://sixfab.com/product/gsm-shields/
buy: http://sixfab.com/product/gsm-shields/
image: 'sixfab_gps_shield.png'
pincount: 40
eeprom: yes
power:
  '4':
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
  '8':
    mode: uart
  '10':
    mode: uart
  '12':
    name: LED
  '22':
    name: Reset
  '7':
    name: 1-Wire Pin

-->
# Sixfab GPS Shield

This is an easy way to add GPS to your pi

Some features include:
* Location, Time, Speed all on the same NMEA Protocol
* Built in 1-Wire support
* Built in antenna
* Also programmable from Linux, MacOS, Windows, Android
