<!--
---
class: board
type: multi
name: "Sense HAT"
image: 'sense-hat.png'
manufacturer: Raspberry Pi Foundation
description: Add-on board that includes an 8×8 RGB LED matrix, 5-button joystick as well as IMU and environmental sensors
url: https://www.raspberrypi.org/products/sense-hat/
formfactor: 'HAT'
pincount: 40
eeprom: yes
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
install:
  'devices':
    - 'i2c'
-->
#Sense HAT

The Sense HAT is an add-on board for Raspberry Pi comprising of a 8×8 RGB LED matrix, a five-button joystick and the following sensors: Gyroscope, Accelerometer, Magnetometer, Temperature, Barometric pressure and Humidity.

The shift register driving the LED Matrix is a LED2472G connected via an ATTINY88 communicating via i2c at address 0x46 with the Pi. The Multi-Directional SKRHABE010 Switch/Joystick is similarly controlled.

The sensors themselves also operate over the i2c bus:

The IMU (Gyroscope, Accelerometer, Magnetometer) through a LSM9DS1 found at i2c address 0x1c(0x1e),0x6a(0x6b), with Interrupts on the ATTINY88.

Environmental sensors are represented by a LPS25H Pressure+Temperature sensor at address 0x5c and by a HTS221 Humidity+Temp sensor at 0x5f on the i2c bus.
