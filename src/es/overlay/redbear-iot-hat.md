<!--
---
name: IoT pHAT
class: board
type: iot
formfactor: pHAT
manufacturer: RedBear
description: A Wi-Fi + Bluetooth add-on board for the Pi Zero
url: https://www.kickstarter.com/projects/1991736672/iot-hat-for-raspberry-pi-a-must-have-for-pi-zero
github: https://github.com/redbear/IoT_pHAT
buy: https://redbear.cc/product/rpi/iot-phat.html
image: 'redbear-iot-hat.png'
pincount: 40
eeprom: setup
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
  '8':
    name: 'BLE TDX'
  '10':
    name: 'BLE RXD'
  '11':
    name: 'BLE RTS'
  '13':
    name: 'WiFi SDIO_D3'
  '15':
    name: 'WiFi SDIO_CLK'
  '16':
    name: 'WiFi SDIO_CMD'
  '18':
    name: 'WiFi SDIO_D0'
  '22':
    name: 'WiFi SDIO_D1'
  '29':
    name: 'BLE BT_RST_N'
  '31':
    name: 'WiFi WL_REG_ON'
  '36':
    name: 'BLE CTS'
  '37':
    name: 'WiFi SDIO_D2'
-->
#IoT pHAT

IoT HAT fabricado por RedBear lleva el BCM43438 usado en Raspberry Pi 3 a formato HAT, compatible con Pi Zero.

El chip proporciona Wi-Fi 802.11n y Bluetooth 4.1 (Modo Dual).

* Bluetooth 4.1
* WiFi
* Bajo consumo
* Se puede añadir antena externa
* Compatible con el mismo software WiFi/Bluetooth usado en Raspberry Pi 3
* Funciona con Pi Zero, A+, B+, Pi 2
