<!--
---
name: uBLOX ZED-X20P Expansion Board for Raspberry Pi
class: board
type: gps
formfactor: HAT
manufacturer: Uputronics
description: All band GPS receiver for Raspberry Pi
url: https://store.uputronics.com
buy: https://store.uputronics.com/products/ublox-zed-x20p-expansion-for-raspberry-pi
image: 'uputronics-zed-x20p-hat.png'
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
    mode: uart
  '10':
    mode: uart
  '12':
    name: PPS
  '16':
    name: TXREADY Not Connected
  '29':
    name: TXREADY Not Connected
  '32':
    name: TXD5
  '33':
    name: RXD5
i2c:
  '0x42':
    name: Ublox
    device: Ublox X20

-->
# uBLOX ZED-X20P Expansion Board for Raspberry Pi 
<br>
The Uputronics uBLOX ZED-X20P Expansion Board for Raspberry Pi provides a modern all band GPS receiver with quick no soldering required connection to all Raspberry Pi boards with the 2x20 header. Featuring PPS (Pulse per second) output to permit the use of the board for PPS disciplined NTP servers, carrier phase output available and super cap for GPS hot start/setting retention.
<br>
<br>
USB-C For direct serial connection to a PC Windows/Linux/Mac (Independent of the Raspberry Pi)

Features: 

* 25Hz update rate, 672 channel X20 GPS Engine
* All Band 
GPS L1C/A, L2C, L5
GAL E1, E5a, E6
BDS B1I, B1C, B2a, B3I
QZSS L1C/A, L1C/B, L2C, L5, L6
NavIC L5 
SBAS L1
* PPS Output on fix (programmable 0.25Hz -> 10MHz)
* LED indicator on PPS
* SMA connector for external antenna (3V Supplied uBLOX ANN-MB3 recommended)
* Current draw up to 80mA in acquire.
* Carrier phase output 

Datasheet: <a href="https://cdn.shopify.com/s/files/1/0835/7707/8094/files/uBLOX_ZED-X20P_Expansion_Board_for_Raspberry_Pi.pdf?v=1787054479">uBLOX ZED-X20P Expansion Board for Raspberry Pi Datasheet</a>
<br>
Command reference guide: <a href="https://cdn.shopify.com/s/files/1/0835/7707/8094/files/u-blox-X20-HPG-2.03_InterfaceDescription_UBXDOC-304424225-20728.pdf?v=1785240336">ZED-X20 Interface Description</a>

