<!--
---
name: RaspBee
class: board
type: iot,radio
formfactor: Custom
manufacturer: dresden elektronik
collected: Other
description: Una placa Zigbee para Raspberry Pi
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

La placa añade capacidades Zigbee completas a una Raspberry Pi, para usar luces, sensores e interruptores de varios fabricantes.

* Compatible con dispositivos Zigbee 3.0, Zigbee Light Link (ZLL) y Zigbee Home Automation (ZHA)
* Admite hasta 200 dispositivos
* Amplificador de potencia integrado para un alcance de señal de máx. 200 m (650 pies) en línea de visión directa
* Compatible con los sistemas de automatización del hogar de código abierto más populares
