<!--
---
name: Enviro Plus
class: board
type: adc,sensor
formfactor: pHAT
manufacturer: Pimoroni
description: A package of environmental sensors for IoT projects
url: https://shop.pimoroni.com/products/enviro-plus
github: https://github.com/pimoroni/enviroplus-python
buy: https://shop.pimoroni.com/products/enviro-plus
image: 'pimoroni-enviro-plus.png'
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
  '8':
    mode: uart
    name: PMS5003
  '10':
    mode: uart
    name: PMS5003
  '13':
    mode: output
    name: PMS5003 Reset
  '15':
    mode: output
    name: PMS5003 Enable
  '16':
    mode: input
    name: ADS1015 Alert
  '18':
    mode: output
    name: Gas Heater En
  '12':
    mode: PCM
    name: Mic i2s clk
  '35':
    mode: PCM
    name: Mic i2s fs
  '38':
    mode: PCM
    name: Mic i2s data
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
  '0x49':
    name: Analog for Gas Sensor
    device: ADS1015
-->
# Enviro+

An all-in-one hobbyist environmental monitoring board. Measures air quality (particulates and gases), temperature, pressure, humidity, light and noise level.

## Features

* BME280 temperature, pressure, humidity sensor
* LTR-559 light and proximity sensor
* MICS6814 analog gas sensor
* ADS1015 analog to digital converter (ADC)
* MEMS microphone
* 0.96" colour LCD (160x80)
* Connector for particulate matter (PM5003) sensor
