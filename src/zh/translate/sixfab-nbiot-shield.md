<!--
---
name: Raspberry Pi NB-IoT Shield
class: board
type: com
formfactor: HAT
manufacturer: Sixfab
description: Connect from anywhere to the internet via NB-IoT on a Raspberry Pi
github: https://github.com/sixfab/RPI-NB-IoT-Shield
url: https://sixfab.com/product/raspberry-pi-nb-iot-shield/
buy: https://sixfab.com/product/raspberry-pi-nb-iot-shield/
image: 'sixfab-nbiot-shield.png'
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
  '29':
    mode: input
    name: IN2
  '31':
    mode: input
    name: VDD_EXT
  '32':
    mode: input
    name: IN1
  '33':
    mode: input
    name: RI
  '37':
    mode: output
    name: Reset
  '37':
    mode: output
    name: Relay
  '38':
    mode: output
    name: User Led
  '38':
    mode: input
    name: User Button
-->
# Raspberry Pi NB-IoT Shield

It is a narrow band IoT (Nb-IoT) shield for Raspberry Pi. NB-IOT is very suitable for IoT applications with low power consumption. Shield also has the built-in 3-axis accelerometer, temperature, humidity, light sensors, opto-coupler, and relay. If you like, you can also add your own sensors using the built-in 4 channel ADC.

Also using the USB connector you can use the shield with Linux, Windows and Android.

## Features

- LTE BC95 Nb-IoT Module B20 800MHz 
- ADS1015 12 Bit 4 Channel ADC
- Relay with opto-coupler protection (24V DC, 120-220V AC Switching)
- Opto-coupler (3-12 V DC switching)- Built-in 3 axis accelerometer (MMA8452Q)
- Built-In HDC1080 temperature sensor (-40 +125 C)
- Built-In HDC1080 humidity sensor (0 100%)
- Built-In ALS-PT19 ambient light sensor()
- 1-Wire interface (3 male pins)(It can be used with DS18B20, DHT21 etc.)
- I2C interface (4 male pins)
- User button and LED
- Micro SIM Socket
- Built-in PCB Antenna
- UFL socket for external antenna

## Warnings

! All data pins work with 3.3V reference. Any other voltage level should harm your shield or RPI.

## Applications

- Smart farming sensor
- Smart cities sensor
- Smart home sensor
- Internet of Things (IoT) sensor
- Smart door lock
- Smart lightning
- Smart metering
- Bike sharing
- Smart parking
- Smart city
- Security and asset tracking
- Home appliances
- Agricultural and environmental monitoring
