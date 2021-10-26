<!--
---
name: Enviro
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://shop.pimoroni.com/products/enviro
github: https://github.com/pimoroni/enviroplus-python
buy: https://shop.pimoroni.com/products/enviro
image: 'pimoroni-enviro.png'
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
  '12':
    mode: PCM
    name: Mic i2s clk
  '35':
    mode: PCM
    name: Mic i2s fs
  '38':
    mode: PCM
    name: Mic i2c data
  '19':
    mode: SPI
  '23':
    mode: SPI
  '21':
    mode: output
    name: LCD D/C
  '32':
    mode: output
    name: Backlight
  '26':
    mode: spi
    name: SPI CS
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x76':
    name: Temperature & Pressure Sensor
    device: BME280
  '0x23':
    name: Lux/Proximity Sensor
    device: LTR559
-->
# Enviro

An all-in-one hobbyist indoor monitoring board. Measures temperature, pressure, humidity, light and noise level.

## Features

* BME280 temperature, pressure, humidity sensor
* LTR-559 light and proximity sensor
* MEMS microphone
* 0.96" colour LCD (160x80)