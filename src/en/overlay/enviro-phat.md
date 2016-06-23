<!--
---
name: Enviro pHAT
class: board
type: iot
image: 'enviro-phat.png'
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://shop.pimoroni.com/products/enviro-phat
github: https://github.com/pimoroni/enviro-phat
buy: https://shop.pimoroni.com/products/enviro-phat
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
    name: Lights
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

Coupled with a Pi Zero, Enviro pHAT is an affordible mix of sensors, ideal for monitoring server rooms, bedrooms, ballrooms or anything you might want to observe.

It also includes a 4-channel ADC, for adding sensors of your own.

##Features:

- BMP280 temperature/pressure sensor
- TCS3472 light and RGB colour sensor
- Two LEDs for illumination
- LSM303D accelerometer/magnetometer sensor
- ADS1015 4-channel analog to digital sensor (ADC)
