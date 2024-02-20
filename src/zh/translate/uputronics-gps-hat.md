<!--
---
name: Uputronics GPS Expansion Board
class: board
type: gps
formfactor: HAT
manufacturer: Uputronics
description: Provides position and PPS Time Reference for Raspberry Pi
url: https://store.uputronics.com
buy: https://store.uputronics.com/index.php?route=product/product&path=60_64&product_id=81
image: 'uputronics-gps-hat.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    mode: UART
  '10':
    mode: UART
  '12':
    name: PPS
i2c:
  '0x00':
    name: Ublox
    device: Ublox
-->
# Uputronics GPS Expansion Board

Adds location and PPS to enable precision time keeping to your Raspberry Pi. 

Features: 

* 166 dBm sensitivity, 18Hz update rate, 72 channel
* Supports up to 3 concurrent GNSS sources GPS (American) GALILEO (European) Glonass (Russian) QZSS (Japan) and BeiDou (China) 
* PPS Output on fix (programmable 0.25Hz -> 10MHz)
* LED indicator on PPS
* Altitude limit 50km in flight mode
* Robust SMA connector for external antenna
* Current draw 6mA in cyclic mode up to 18mA in acquire.

I2C is connected but uses clock stretching.

Command reference guide: <a href="https://www.u-blox.com/sites/default/files/products/documents/u-blox8-M8_ReceiverDescrProtSpec_(UBX-13003221)_Public.pdf">U-Blox M8 Receiver Description</a>
