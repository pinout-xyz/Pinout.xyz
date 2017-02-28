<!--
---
name: Ultimate GPS HAT
class: board
type: gps,rtc
formfactor: HAT
manufacturer: Adafruit
description: Add precision time and location to your Raspberry Pi
url: https://learn.adafruit.com/adafruit-ultimate-gps-hat-for-raspberry-pi
schematic: https://learn.adafruit.com/assets/21938
buy: https://www.adafruit.com/products/2324
image: 'adafruit-gps-hat.png'
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
  '7':
    name: PPS
  '8':
    mode: UART
  '10':
    mode: UART
-->
#Ultimate GPS HAT

The Ultimate GPS HAT from Adafruit adds precision time and location to your Raspberry Pi.

Features:

* 165 dBm sensitivity, 10 Hz updates, 66 channels
* Only 20mA current draw
* Built in Real Time Clock (RTC)
* PPS output on fix
* Works up to ~32Km altitude
* Internal patch antenna + u.FL connector for external active antenna
* Fix status LED blinks when the GPS has determined the current coordinates
* break-outs for all the Raspberry Pi's extra pins
* Prototyping area for adding LEDs, sensors, and more
