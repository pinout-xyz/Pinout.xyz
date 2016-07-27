<!--
---
name: "Sense HAT"
class: board
type: alle
formfactor: HAT
manufacturer: Raspberry Pi
image: 'image.png'
url: https://www.raspberrypi.org/products/sense-hat/
description: Erweiterungsmodul mit einer 8×8 RGB LED Matrix, 5-Tasten Joystick sowie jede menge Sensoren (Gyroskop, Beschleunigungsmesser, Magnetometer, Temperatur, Luftdruck und Luftfeuchtigkeit) 
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

LED Matrix: LED2472G -> ATTINY88 -> SPI(8/9/10/11)
Joystick: SKRHABE010 -> ATTINY88 -> GPIO23/24/25
Axis/IMU: LSM9DS1 -> i2c 0x1c(1e),0x6a(6b) (INT on MCU)
Luftdruck/Temp: LPS25H -> i2c 0x5c
Luftfeuchtigkeit/Temp: HTS221 -> i2c 0x5f