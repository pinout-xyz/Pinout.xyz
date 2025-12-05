<!--
---
name: Pi Servo HAT
class: board
type: io,motor
formfactor: pHAT
manufacturer: SparkFun
description: 16-channel, 12-bit PWM Controller
url: https://www.sparkfun.com/products/14328
github: https://github.com/sparkfun/Pi_Servo_Hat
schematic: https://cdn.sparkfun.com/assets/1/a/1/6/3/PI_Servo_Shield_v10.pdf
buy: https://www.sparkfun.com/products/14328
image: 'sparkfun-pi-servo-hat.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
  '4':
  '17':
ground:
  '6':
  '9':
  '14':
  '20':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    mode: uart
  '10':
    mode: uart
i2c:
  '0x40':
    name: PCA9685
    device: PCA9685
-->
# SparkFun Pi Servo HAT

The SparkFun Pi Servo HAT allows your Raspberry Pi to control up to 16 servo motors in a straightforward and uncomplicated manner via an I2C connection. Thanks to its I2C capabilities, this PWM HAT saves the Raspberry Pi's GPIO, allowing you to use them for other purposes. Additionally, the Pi Servo HAT adds a serial terminal connection, which will allow you to bring up a Raspberry Pi without having to hook it up to a monitor and keyboard.
