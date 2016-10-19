<!--
---
name: PiStep2 Dual
class: board
type: Stepper Motor Driver
formfactor: pHAT
manufacturer: 4tronix
description: A Dual Stepper Motor Driver for 
url: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=554
github: 
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=554
image: 'pistep2d.png'
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
    name: A0
    mode: output
  '12':
    name: A1
    mode: output
  '13':
    name: A2
    mode: output
  '15':
    name: A3
    mode: output
  '16':
    name: B0
    mode: output
  '18':
    name: B1
    mode: output
  '22':
    name: B2
    mode: output
  '7':
    name: B3
    mode: output
-->
# PiStep2 Dual
Drive 2 uni-polar stepper motors using a single control board.
Uses a ULN2803 Darlington driver chip to drive the motors.
Ideal for use with 28BYJ48 stepper motors
Supported in Scratch GPIO as well as in Python

