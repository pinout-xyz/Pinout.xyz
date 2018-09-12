<!--
---
name: Raspberry Pi Cellular IoT Application HAT – LTE-M & NB-IoT & eGPRS
class: board
type: com
formfactor: HAT
manufacturer: Sixfab
description: Connect from anywhere to the internet on a Raspberry Pi
github: https://github.com/sixfab/Sixfab_RPi_CellularIoT_Library
url: https://sixfab.com/product/raspberry-pi-cellular-iot-application-hat/
buy: https://sixfab.com/product/raspberry-pi-cellular-iot-application-hat/
image: 'sixfab-cellular-iot-application-hat.png'
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
    name: 1wire
  '8':
    mode: uart
  '10':
    mode: uart
  '11':
    mode: output
    name: Relay
  '12':
    mode: output
    name: Opto#2
  '13':
    mode: output
    name: User Led
  '18':
    mode: input
    name: User Button
  '19':
    mode: output
    name: Opto#1
  '23':
    mode: output
    name: PowerKey
  '31':
    mode: input
    name: Ap Ready
  '33':
    mode: input
    name: RI
  '37':
    mode: output
    name: Enable
  '38':
    mode: input
    name: Status
-->
# Raspberry Pi Cellular IoT Application HAT – LTE-M & NB-IoT & eGPRS

This is a hat that has combined LTE technologies Cat.M1, Cat.NB1 (NB-IoT) and eGPRS for Raspberry Pi, based on Quectel’s BG96 module. The hat has the power of new IoT phenomenon LPWA (Low Power Wide Area) with Cat.M1 and NB-IoT connection functionalities. Besides, it also provides the function of eGPRS that be enhanced version of classical GPRS.

The hat has GNSS (GPS, GLONASS etc.) functionality for the need of location, navigation, tracking, mapping and timing applications.

The design has a built-in temperature, humidity, light sensors, 3-axis accelerometer, and relay.

Also using the USB connector you can use the shield with Linux, Windows and Android.

##Features

- BG96 Cat.M1 / Cat.NB1 (NB-IoT) / eGPRS (EDGE, GPRS)
- Supported Bands : Global – B1/ B2/ B3/ B4/ B5/ B8/ B12/ B13/ B18/ B19/ B20/ B26/ B28 and B39 ( for Cat M1 only )
- eGPRS Supported Frequencies: 850/900/1800/1900Mhz
- Embedded GNSS Functionality (GPS, GLONASS, BeiDou/Compass, Galileo, QZSS)
- Optional standalone use via USB interface
- ADS1015 12 Bit 4 Channel ADC
- Relay with optocoupler protection (24V DC, 120-220V AC Switching)
- Optocoupler (3-12 V DC switching)
- Built-in 3 axis accelerometer (MMA8452Q)
- Built-In HDC1080 temperature sensor (-40 +125 C)
- Built-In HDC1080 humidity sensor (0 100%)
- Built-In ALS-PT19 ambient light sensor()
- 1-Wire interface (3 male pins)(It can be used with DS18B20, DHT21 etc.)
- I2C interface (4 male pins)
- User button and LED
- Micro SIM Socket
- UFL sockets for external antennas
