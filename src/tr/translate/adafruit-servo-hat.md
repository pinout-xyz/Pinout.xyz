<!--
---
name: Servo/PWM HAT
class: board
type: io,motor
formfactor: HAT
manufacturer: Adafruit
description: A 16-Channel Servo / PWM HAT for Raspberry Pi
url: https://www.adafruit.com/product/2327
github: https://github.com/adafruit/Adafruit_Python_PCA9685
buy: https://www.adafruit.com/product/2327
image: 'adafruit-servo-hat.png'
pincount: 40
eeprom: yes
power:
  '1':
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
i2c:
  '0x40':
    name: PWM Controller
    device: pca9685
install:
  'devices':
    - 'i2c'
  'apt':
    - 'python-smbus'
    - 'python3-smbus'
    - 'python-dev'
    - 'python3-dev'
-->
#Servo/PWM HAT

The Adafruit Servo/PWM HAT allows you to drive up to 16 servos or PWM outputs over I2C with only 2 pins.
The on-board PWM controller will drive all 16 channels simultaneously with no additional processing overhead for the Raspberry Pi. Using a binary addressing system set by jumpers you can solder on the PCB, it is possible to stack up to 62 HATs to control up to 992 servos, using nothing more than the I2C bus.

Important note: servos can use a lot of power and it is not a good idea to use the Raspberry Pi's 5v pin to power them up. Electrical noise and 'brownouts' from excess current draw could cause your Pi to act erratically, reset and/or overheat. Keep the Pi power supply and the servos power supply completely separate!
