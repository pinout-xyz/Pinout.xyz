<!--
---
name: PiStep2 Quad
class: board
type: motor
formfactor: pHAT
manufacturer: 4tronix
description: A Quad Stepper Motor Driver for Raspberry Pi
url: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=554
github:
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=554
image: '4tronix-pistep2q.png'
pincount: 40
eeprom: no
power:
  '2':
  '17':
ground:
  '30':
  '34':
  '39':
pin:
  '11':
    name: MotorA_0
    mode: output
  '12':
    name: MotorA_1
    mode: output
  '13':
    name: MotorA_2
    mode: output
  '15':
    name: MotorA_3
    mode: output
  '16':
    name: MotorB_0
    mode: output
  '18':
    name: MotorB_1
    mode: output
  '22':
    name: MotorB_2
    mode: output
  '7':
    name: MotorB_3
    mode: output
  '33':
    name: MotorC_0
    mode: output
  '32':
    name: MotorC_1
    mode: output
  '31':
    name: MotorC_2
    mode: output
  '29':
    name: MotorC_3
    mode: output
  '38':
    name: MotorD_0
    mode: output
  '37':
    name: MotorD_1
    mode: output
  '36':
    name: MotorD_2
    mode: output
  '35':
    name: MotorD_3
    mode: output
-->
# PiStep2 Quad

Drive 4 uni-polar stepper motors using a single control board with the PiStep2 Quad.

* Uses ULN2803 Darlington driver chips to drive the motors
* Ideal for use with 28BYJ48 stepper motors
* Supported in Scratch GPIO as well as in Python
