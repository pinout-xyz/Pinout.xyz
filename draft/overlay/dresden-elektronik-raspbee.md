<!--
---
name: RaspBee
class: board
type: iot,radio
formfactor: Custom
manufacturer: dresden elektronik
description: A Zigbee add-on board for the Raspberry Pi
url: https://phoscon.de/raspbee
github: https://github.com/dresden-elektronik/deconz-rest-plugin
buy: https://phoscon.de/raspbee#buy
image: 'dresden-elektronik-raspbee.png'
pincount: 12
eeprom: no
power:
  '2':
ground:
  '6':
  '9':
pin:
  '8':
    name: TXD
    mode: UART
  '10':
    name: RXD
    mode: UART
  '11':
    name: RESET
    mode: input
    active: low
  '12':
    name: SW1
    mode: GPIO
-->
# RaspBee Zigbee add-on board

The add-on board adds full Zigbee capabilities to a Raspberry Pi, to use lights, sensors and switches from various vendors.

* Supports Zigbee 3.0, Zigbee Light Link (ZLL) and Zigbee Home Automation (ZHA) devices
* Supports up to 200 devices
* On board power-amplifier for a signal-range of max. 200 m (650ft) in free line of sight
* Supported by the most popular open source home automation systems
