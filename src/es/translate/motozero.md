<!--
---
name: MotoZero
class: board
type: motor
formfactor: pHAT
manufacturer: PiHut
description: Control 4 motors from your Raspberry Pi
url: https://thepihut.com/products/motozero
buy: https://thepihut.com/products/motozero
image: 'motozero.png'
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
  '11':
    name: "Motor 2 EN"
  '12':
    name: "Motor 4 -"
  '13':
    name: "Motor 1 -"
  '15':
    name: "Motor 2 -"
  '16':
    name: "Motor 3 +"
  '18':
    name: "Motor 1 +"
  '22':
    name: "Motor 4 EN"
  '29':
    name: "Motor 1 EN"
  '31':
    name: "Motor 2 +"
  '32':
    name: "Motor 3 EN"
  '33':
    name: "Motor 4 +"
  '36':
    name: "Motor 3 -"
-->
# MotoZero

The MotoZero is a simple Raspberry Pi motor controller add-on board that lets you control up to 4 motors independently.
With simple GPIO control and its very own GPIO Zero library entry, it's one of the easiest ways to control lots of motors on your Raspberry Pi.

Features:

* Control 4 motors independently in both forwards and reverse
* Control with basic GPIO 'on/off' code, or using GPIO Zero library
* Terminals break out the motor outputs to the edge of the board
* Built-in flyback voltage protection diodes
* Suitable for all 40 pin Raspberry Pi models
