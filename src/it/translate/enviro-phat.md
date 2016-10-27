<!--
---
name: Enviro pHAT
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://shop.pimoroni.com/products/enviro-phat
github: https://github.com/pimoroni/enviro-phat
buy: https://shop.pimoroni.com/products/enviro-phat
image: 'enviro-phat.png'
pincount: 40
eeprom: no
power:
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    mode: output
    name: LEDs
i2c:
  '0x1d':
    name: Motion Sensor
    device: LSM303D
  '0x29':
    name: Light/Colour Sensor
    device: TCS3472
  '0x49':
    name: 4-Channel Analog Input
    device: ADS1015
  '0x77':
    name: Temp/Pressure Sensor
    device: BMP280
-->
#Enviro pHAT

Coupled with a Pi Zero, Enviro pHAT is an affordable mix of sensors, ideal for monitoring server rooms, bedrooms, ballrooms or anything you might want to observe. It also includes a 4-channel ADC, for adding sensors of your own. It works with all of the 40-pin Raspberry Pi variants - 3/2/B+/A+/Zero.

Features:

* BMP280 temperature/pressure sensor (0x77 on the i2c bus)  
* TCS3472 light and RGB colour sensor (0x29 on the i2c bus)  
(with two GPIO controlled LEDs for illumination)  
* LSM303D accelerometer/magnetometer sensor (0x1d on the i2c bus)  
* ADS1015 4-channel 5v tolerant 12-bit ADC (0x49 on the i2c bus)  
(3.3v 12-bit ADC at address 0x48 in first production run of the board)

To get the pHAT set up and ready to go you can use the one-line product installer:

```bash
curl -sS get.pimoroni.com/envirophat | bash
```

Then import it into your Python script and start tinkering:

```bash
from envirophat import light, motion, weather, analog, leds
```
