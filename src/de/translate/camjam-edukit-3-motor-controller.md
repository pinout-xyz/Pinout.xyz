<!--
---
name: CamJam EduKit 3 motor controller board
class: board
type: motor
formfactor: Custom
manufacturer: PiHut
description: A motor controller board to control two motor channels and break out unused pins. Please note, pinouts for the original version and the new version are the same.
url: https://camjam.me/?page_id=1035
buy: https://thepihut.com/collections/camjam-edukit/products/camjam-edukit-3-robotics
github: https://github.com/CamJam-EduKit/EduKit3/
image: 'camjam-edukit-3-motor-controller.png'
pincount: 26
eeprom: no
pin:
  '21':
    name: MotorA_0
    mode: output
  '19':
    name: MotorA_1
    mode: output
  '26':
    name: MotorB_0
    mode: output
  '24':
    name: MotorB_1
    mode: output
-->
# CamJam EduKit 3 motor controller board

This motor controller board is part of CamJam EduKit 3 - Robotics but is also [available separately from The Pi Hut](https://thepihut.com/products/camjam-edukit-motor-controller). It provides two motor outputs for 6V motors using a DRV8833 H Bridge and breaks out most of the unused pins to a female header on top of the board.

Pins that are broken out to the header are as follows: 5v, 3v3, SDA and SCL (for I2C devices), 4, 17, 18, 22, 23, 24, 25, 27, and Ground.

The board expects 4 AA batteries to be used to power the board, although it will accept up to 10V if you have more powerful motors available. A flyback diode is provided to protect your board and Raspberry Pi if you should accidentally wire up the power source the wrong way around.

The motor controller board was designed by Rachel Rayns for The Pi Hut. Educational material was written by [Tim Richardson](https://twitter.com/Geeky_Tim) and tested by [Michael Horne](https://twitter.com/recantha) over at [CamJam](https://camjam.me/edukit).
