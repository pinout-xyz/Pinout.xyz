<!--
---
name: Sense HAT
class: board
type: led,sensor
formfactor: HAT
manufacturer: Raspberry Pi
description: Add-on board that includes an 8×8 RGB LED matrix, 5-button joystick as well as IMU and environmental sensors
url: https://www.raspberrypi.org/products/sense-hat/
github: https://github.com/RPi-Distro/python-sense-hat
schematic: https://www.raspberrypi.org/documentation/hardware/sense-hat/images/Sense-HAT-V1_0.pdf
buy: https://thepihut.com/products/raspberry-pi-sense-hat-astro-pi
image: 'sense-hat.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '16':
    name: IMU Interrupt
    mode: output
  '18':
    name: IMU Interrupt
    mode: output
  '22':
    name: Atmel Prog Reset
    mode: output
    active: high
  '24':
    name: Atmel Chip Select
    mode: chipselect
    active: high
i2c:
  '0x5c':
    name: Pressure/Temp
    device: lps25h
  '0x5f':
    name: Humidity/Temp
    device: hts221
  '0x6a':
    name: Accelerometer
    device: lsm9ds1
  '0x1c':
    name: Magnetometer
    device: lsm9ds1
  '0x46':
    name: LED Matrix
    device: led2472g
install:
  'devices':
    - 'i2c'
-->
# Sense HAT

The Sense HAT is an add-on board for Raspberry Pi comprising of a 8×8 RGB LED matrix, a five-button joystick and the following sensors: Gyroscope, Accelerometer, Magnetometer, Temperature, Barometric pressure and Humidity.

The shift register driving the LED Matrix is a LED2472G connected via an Atmel ATTINY88 communicating via i2c at address 0x46 with the Pi. The Multi-Directional SKRHABE010 Switch/Joystick is similarly controlled.

The sensors themselves also operate over the i2c bus:

The IMU (Accelerometer and Magnetometer) through a LSM9DS1 found at i2c address 0x1c(0x1e) and 0x6a(0x6b), with Interrupts on the ATTINY88.

Environmental sensors are represented by a LPS25H Pressure/Temperature sensor at address 0x5c and by a HTS221 Humidity/Temperature sensor at 0x5f on the i2c bus.

In addition, the Atmel chip can be reprogrammed via the SPI interface. The pinout herein only maps the reset and chip select - adding a display or other SPI device alongside the Sense HAT should be possible with a few precautions.
