<!--
---
name: Picon Zero
class: board
type: motor
formfactor: pHAT
image: '4tronix-picon-zero.png'
manufacturer: 4tronix
description: A robot controller board for the Raspberry Pi
url: http://4tronix.co.uk/piconzero/
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=552
pincount: 40
eeprom: no
power:
  '2':
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
  '38':
    name: Ultrasonic
    mode: input/output
i2c:
  '0x22':
    name: PiconZero
    device: ATMega328
-->
#Picon Zero

The Picon Zero is an add-on PCB for the Raspberry Pi that is physically the same size as a Raspberry Pi Zero and so is ideal as a pseudo-Hat (pHat) for the Pi Zero. However, it can of course be used on any Raspberry Pi with a 40-pin GPIO connector.

As well as 2 full H-Bridge motor drivers, the Picon Zero has a number of Input and Output pins that can be configured in a variety of ways, allowing you to easily add analog inputs or neopixel outputs to your Raspberry Pi without any complicated software and kernel specific drivers. It also provides an interface for an HC-SR04 ultrasonic distance sensor and opens up 5 GPIO pins from the Raspberry Pi for you to use as you see fit.
