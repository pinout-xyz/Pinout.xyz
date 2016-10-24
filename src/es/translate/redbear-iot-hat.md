<!--
---
name: IoT HAT
class: board
type: iot
formfactor: pHAT
manufacturer: RedBear
description: A Wi-Fi + Bluetooth add-on board for the Pi Zero
url: https://www.kickstarter.com/projects/1991736672/iot-hat-for-raspberry-pi-a-must-have-for-pi-zero
github:
buy: https://www.kickstarter.com/projects/1991736672/iot-hat-for-raspberry-pi-a-must-have-for-pi-zero
image: 'redbear-iot-hat.png'
pincount: 40
eeprom: no
power: 3v3,5v
pin:
  '11':
    name: 'RTS'
  '13':
    name: 'SDIO_D3'
  '15':
    name: 'SDIO_CLK'
  '29':
    name: 'BT_RST_N'
  '31':
    name: 'WL_REG_ON'
  '33':
    name: 'BT_HOST_WAKE'
  '37':
    name: 'SDIO_D2'
  '8':
    name: 'TXD'
  '10':
    name: 'RXD'
  '16':
    name: 'SDIO_CMD'
  '18':
    name: 'SDIO_D0'
  '22':
    name: 'SDIO_D1'
  '32':
    name: 'WL_HOST_WAKE'
  '36':
    name: 'CTS'
  '38':
    name: 'BT_WAKE'
-->
#PiZero IoT HAT

IoT HAT fabricado por RedBear lleva el BCM43438 usado en Raspberry Pi 3 a formato HAT, compatible con Pi Zero.

El chip proporciona Wi-Fi 802.11n y Bluetooth 4.1 (Modo Dual).

* Bluetooth 4.1
* WiFi
* Bajo consumo
* Se puede añadir antena externa
* Compatible con el mismo software WiFi/Bluetooth usado en Raspberry Pi 3
* Funciona con Pi Zero, A+, B+, Pi 2
