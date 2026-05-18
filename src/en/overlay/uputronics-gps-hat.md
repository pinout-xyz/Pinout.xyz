<!--
---
name: Uputronics GPS Expansion Board
class: board
type: gps
formfactor: HAT
manufacturer: Uputronics
description: Provides position and PPS Time Reference for Raspberry Pi
url: https://store.uputronics.com
buy: https://store.uputronics.com/products/raspberry-pi-gps-rtc-expansion-board
image: 'uputronics-gps-hat.png'
pincount: 40
eeprom: no
power:
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
  '0x42':
    name: Ublox
    device: Ublox M8030
  '0x52':
    name: RV-3028-C7
    device: Microcrystal RV-3028-C7 RTC


-->
# Uputronics GPS Expansion Board
<br>
Adds location and PPS to enable precision time keeping to your Raspberry Pi. 
<br>
Fitted with a RV-3028-C7 RTC.
<br>
USB-C For direct serial connection to a PC Windows/Linux/Mac (Independant of the Raspberry Pi)

Features: 

* 166 dBm sensitivity, 18Hz update rate, 72 channel
* Supports up to 3 concurrent GNSS sources GPS (American) GALILEO (European) Glonass (Russian) QZSS (Japan) and BeiDou (China) 
* PPS Output on fix (programmable 0.25Hz -> 10MHz)
* LED indicator on PPS
* Altitude limit 50km in flight mode
* Robust SMA connector for external antenna
* Current draw 6mA in cyclic mode up to 18mA in acquire.
* Seperate RV-3028-C7 RTC
* RAW Output available from the GPS

Datasheet: <a href="https://cdn.shopify.com/s/files/1/0835/7707/8094/files/Uputronics_Raspberry_Pi_GPS_RTC_Board_Datasheet_9eec2e77-d368-45ee-acc2-be899ff1d0be.pdf?v=1736517155">Raspberry Pi GPS/RTC Expansion Board Datasheet</a>
<br>
Command reference guide: <a href="https://cdn.shopify.com/s/files/1/0835/7707/8094/files/u-blox8-M8_ReceiverDescrProtSpec__UBX-13003221__Public_fba84713-56a9-46e5-a976-1ce199a1c935.pdf?v=1773174585">U-Blox M8 Receiver Description</a>

