<!--
---
name: Enviro pHAT
class: board
type: iot
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://github.com/pimoroni/enviro-phat
github: https://github.com/pimoroni/enviro-phat
buy: https://github.com/pimoroni/enviro-phat
formfactor: Custom
pincount: 40
eeprom: no
power: 5v
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    mode: output
i2c:
  '0x29':
    name: Light/Colour Sensor
    device: TCS3472
  '0x1d':
    name: Motion Sensor
    device: LSM303D
  '0x77':
    name: Temp/Pressure Sensor
    device: BMP280
  '0x48':
    name: 4-Channel Analog Input
    device: ADS1015
-->
#Enviro pHAT
