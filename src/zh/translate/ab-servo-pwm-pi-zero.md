<!--
---
name: Servo PWM Pi Zero
class: board
type: io,motor
formfactor: pHAT
manufacturer: AB Electronics UK
description: 16-channel, 12-bit PWM Controller
url: https://www.abelectronics.co.uk/p/72/servo-pwm-pi-zero
github: https://github.com/abelectronicsuk
schematic: https://www.abelectronics.co.uk/docs/pdf/schematic-servopi-zero.pdf
buy: https://www.abelectronics.co.uk/p/72/servo-pwm-pi-zero
image: 'ab-servo-pwm-pi-zero.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '14':
  '20':
  '30':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: OE
    mode: output
    active: high
i2c:
  '0x40':
    alternate: [ '0x40', '0x41', '0x42', '0x43', '0x44', '0x45', '0x46', '0x47', '0x48', '0x49', '0x4A', '0x4B', '0x4C', '0x4D', '0x4E', '0x4F','0x50', '0x51', '0x52', '0x53', '0x54', '0x55', '0x56', '0x57', '0x58', '0x59', '0x5A', '0x5B', '0x5C', '0x5D', '0x5E', '0x5F','0x60', '0x61', '0x62', '0x63', '0x64', '0x65', '0x66', '0x67', '0x68', '0x69', '0x6A', '0x6B', '0x6C', '0x6D', '0x6E', '0x6F','0x70', '0x71', '0x72', '0x73', '0x74', '0x75', '0x76', '0x77', '0x78', '0x79', '0x7A', '0x7B', '0x7C', '0x7D', '0x7E', '0x7F' ]
    name: PCA9685
    device: PCA9685
-->
# Servo PWM Pi Zero

The Servo PWM Pi Zero is a 16-channel, 12-bit PWM controller for the Raspberry Pi, suitable for driving LEDs and radio control servos. The board is based around PCA9685 PWM I2C LED controller IC from NXT and can drive each of the 16 outputs with 12 bit (4096 steps) duty cycle from 0%  to 100%.

The output frequency is programmable from a typical 40Hz to 1000Hz. Each output driver is programmed to be either open-drain with a 22 mA current sink capability at 5 V or totem pole with a 22 mA sink, 10 mA source capability at 5 V. 220R current limiting resistors are used on each channel allowing you to connect servos or LEDs directly to the outputs.

Python, C, C++, Node.js and Windows 10 IOT libraries are available on GitHub.