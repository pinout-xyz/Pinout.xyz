<!--
---
name: Score:Zero
class: board
type: io,other
formfactor: pHAT
manufacturer: The Wonky Resistor Co
description: A super-simple and stylish soldering kit - makes an NES-style games controller when assembled.
url: http://wonkyresistor.com/scorezero
github: https://github.com/wonkyresistor/scorezero
schematic: 
buy: http://wonkyresistor.com/scorezero
image: 'scorezero.png'
pincount: 40
eeprom: no
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
    name: Start
    mode: input
    active: low
  '31':
    name: Select
    mode: input
    active: low
  '15':
    name: Up
    mode: input
    active: low
  '16':
    name: Right
    mode: input
    active: low
  '18':
    name: Down
    mode: input
    active: low
  '22':
    name: Left
    mode: input
    active: low
  '37':
    name: B
    mode: input
    active: low
  '13':
    name: A
    mode: input
    active: low
-->
# Score:Zero

Score:Zero is a simple-soldering-kit-come-games-controller for the Raspberry Pi Zero.

It has eight active-low push-buttons connected to various GPIO pins.

On the underside of the board there are also solder pads connected to power, ground, I2C, SPI and serial comms.