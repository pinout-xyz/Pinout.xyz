<!--
---
name: Uputronics LoRa Expansion Board
class: board
type: Radio
formfactor: HAT
manufacturer: Uputronics
description: LoRa Radio board for Raspberry Pi
url: http://www.pi-in-the-sky.com/
buy: https://store.uputronics.com/index.php?route=product/product&path=61&product_id=68
github: https://github.com/piinthesky
schematic: https://github.com/PiInTheSky/pits-hardware/blob/master/PiLoraGatewayV2.5.pdf
image: 'uputronics-lora.png'
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
  '18':
    mode: CE0/DIO5
  '22':
    mode: CE0/DIO0
  '24':
    mode: CE0/NSS
  '26':
    mode: CE1/NSS
  '32':
    name: CE1/DIO5
  '36':
    name: CE1/DIO0
  '40':
    name: CE1/DATA LED
  '19':
    name: MOSI
  '21':
    name: MISO
  '23':
    name: SCLK
  '29':
    name: CE0/DATA LED
  '31':
    name: LAN LED
  '33':
    name: INTERNET LED
-->
# Uputronics LoRa Expansion Board

Fitted with one or two (CE1 populated by default) HopeRF LoRa modules in 434,868 or 915MHz frequencies. 
Primarily designed to make a LoRa gateway for High Altitude balloon reception or stacked on the Pi In The Sky board to provide LoRa tranmission from High Altitude balloons. 
However can be used for whatever custom project you have where LoRa radio is required.

Features: 

* Four LEDs for data and other indications. 
* One or two HopeRF modules for making gateways/repeaters 
* Robust SMA connector for antennas. 
* Stackable with other Uputronics Boards 
* Open source code and hardware
