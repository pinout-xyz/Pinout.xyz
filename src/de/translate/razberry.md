<!--
---
name: RaZberry
class: board
type: iot,radio
formfactor: Custom
manufacturer: Z-Wave.Me
description: Z-Wave transceiver module for Raspberry Pi
url: https://z-wave.me/products/razberry/
image: 'razberry.png'
pincount: 10
eeprom: no
power:
  '1':
ground:
  '6':
  '9':
pin:
  '8':
    mode: uart
  '10':
    mode: uart
-->
# RaZberry

RaZberry hosts a Sigma Designs ZM5101 Z-Wave transceiver module (a so called 5th generation Z-Wave module), an external 32 K SPI flash for network data and a PCBA antenna. Additionally two LEDs are used to indicate certain status of the Z-Wave controller chip. Beside the PCBA antenna there is an option to solder a U.FL connector for external SMA antenna.

The power consumption of the board is typically 18 mA at 3.3 V but can peak up to 40 mA when the chip is transmitting.

RaZberry supports Z-Wave Security S2 and Smart Start technologies.
