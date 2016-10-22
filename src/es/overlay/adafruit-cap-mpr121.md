<!--
---
name: Capacitive Touch HAT
class: board
type: cap
formfactor: HAT
manufacturer: Adafruit
description: Create electronics that can react to human touch with up to 12 individual sensors
url: https://www.adafruit.com/products/2340
github: https://github.com/adafruit/Adafruit_Python_MPR121
buy: https://www.adafruit.com/products/2340
image: 'adafruit-cap-mpr121.png'
pincount: 40
eeprom: yes
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
i2c:
  '0x5A':
    name: Cap Touch
    device: mpr121
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
#Capacitive Touch HAT

Esta placa para Raspberry Pi proporciona 12 entradas táctiles capacitivas y todo el sistema para poder leerlas mediante el puerto I2C.

Basado en el chip MPR121, este HAT permite crear dispositivos electrónicos que reaccionan al tacto humano, pudiendo utilizar hasta 12 sensores.
