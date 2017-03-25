<!--
---
name: MotoZero
class: board
type: motor
formfactor: pHAT
manufacturer: The Pi Hut
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
  '29':
    name: En1
  '11':
    name: En2
  '32':
    name: En3
  '22':
    name: En4
  '18':
    name: +1
  '31':
    name: +2
  '16':
    name: +3
  '33':
    name: +4
  '13':
    name: -1
  '15':
    name: -2
  '36':
    name: -3
  '12':
    name: -4

-->
# MotoZero

The MotoZero is a simple Raspberry Pi motor controller add-on board that lets you control up to 4 motors independently.
With simple GPIO control and its very own GPIO Zero library entry, it's one of the easiest ways to control lots of motors on your Raspberry Pi 

Features:

* Control 4 motors independently in both forwards and reverse
* Control with basic GPIO 'on/off' code, or use the excellent GPIO Zero library
* Terminals break out the motor outputs to the edge of the board, ideal for wheeled and tracked robots
* Robust chunky terminal blocks for solid connections
* Pi Zero sized, although will fit all 40pin Raspberry Pi models
* Simply power your Pi the usual way (via the micro-USB connection using a plug, power bank or similar) and then add battery power for the motors.
* Built-in flyback diodes within the controller chips, which prevent damage from motor 'flyback' voltage spikes

