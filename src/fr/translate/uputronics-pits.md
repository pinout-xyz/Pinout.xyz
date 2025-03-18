<!--
---
name: Uputronics Pi In The Sky Board
class: board
type: gps,Radio
formfactor: HAT
manufacturer: Uputronics
description: Radio telemetry board for Raspberry Pi
url: http://www.pi-in-the-sky.com/
buy: https://store.uputronics.com/index.php?route=product/product&path=62&product_id=52
github: https://github.com/piinthesky
schematic: https://github.com/PiInTheSky/pits-hardware/blob/master/PiInTheSky-Mainboard-v2.4.sch
image: 'uputronics-pits.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '8':
    mode: UART/MTX2 TXD
  '10':
    mode: UART
  '38':
    name: PPS
  '7':
    name: ONEWIRE
  '11':
    name: MTX2 ENABLE
  '13':
    name: UBLOX SDA Bit Banged
  '15':
    name: UBLOX SCL Bit Banged
  '35':
    name: WARN LED
  '37':
    name: OK LED
i2c:
  '0x00':
    name: ADC
    device: MAXIM MCP3426
-->
# Uputronics Pi In The Sky Board

Telemetry board designed for use on high altitude balloons. Features Ublox MAX-M8Q, Radiometrix MTX2 434MHz radio transmitter, efficient 2A buck/boost, I2C ADC and One Wire temperature sensor.

Features: 

* Back powers Raspberry Pi 
* Ublox MAX-M8Q GPS module which can give positional information up to 50km altitude
* Spare header for external i2C devices/additional temperature sensor (DS18B20)
* Allows use of Raspberry Pi camera for live image tranmission.
* Stackable with other Uputronics Boards for LoRa transmission and APRS.
* Open source code and hardware

<a href="http://www.daveakerman.com/?p=1732">For further information on high altitude balloon launching click here</a>
