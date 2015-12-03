<!--
---
name: "Sense HAT"
manufacturer: Raspberry Pi Foundation
url: https://www.raspberrypi.org/products/sense-hat/
description: Add-on board that includes an 8×8 RGB LED matrix, 5-button joystick as well as IMU and environmental sensors 
install:
  'devices':
    - 'i2c'
    - 'spi'    
pincount: 40
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  16:
    name: Joystick
    mode: input
  18:
    name: Joystick
    mode: input
  19:
    mode: spi
  21:
    mode: spi
  22:
    name: Joystick
    mode: input
  23:
    mode: spi
  24:
    mode: spi
-->
#Sense HAT

LED Matrix: LED2472G -> ATTINY88 -> SPI
Joystick: SKRHABE010 -> ATTINY88 -> GPIO23/24/25
Axis/IMU: LSM9DS1 -> i2c 0x1c(1e),0x6a(6b) (INT on MCU)
Pressure/Temp: LPS25H -> i2c 0x5c
Humidity/Temp: HTS221 -> i2c 0x5f