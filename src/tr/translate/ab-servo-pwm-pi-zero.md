<!--
---
name: Servo PWM Pi Zero
class: board
type: io,motor
formfactor: pHAT
manufacturer: AB Electronics
description: 16-channel, 12-bit PWM Controller
url: https://www.abelectronics.co.uk/p/72/Servo-PWM-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/72/Servo-PWM-Pi-Zero
image: 'ab-servo-pi-zero.png'
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
    name: PCA9685
    device: PCA9685
-->
#Servo PWM Pi Zero

The Servo PWM Pi Zero is a 16-channel, 12-bit PWM controller for the Raspberry Pi, suitable for driving LEDs and radio control servos. The board is based around PCA9685 PWM I2C LED controller IC from NXT and can drive each of the 16 outputs with 12 bit (4096 steps) duty cycle from 0%  to 100%.

The output frequency is programmable from a typical 40Hz to 1000Hz. Each output driver is programmed to be either open-drain with a 22 mA current sink capability at 5 V or totem pole with a 22 mA sink, 10 mA source capability at 5 V. 220R current limiting resistors are used on each channel allowing you to connect servos or LEDs directly to the outputs.

Arduino, C, Node.js, Windows 10 IOT, Python 2 and Python 3 libraries are available on GitHub.