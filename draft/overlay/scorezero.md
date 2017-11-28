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
power: external
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
  '5':
    name: Start
    mode: input
    active: low
  '6':
    name: Select
    mode: input
    active: low
  '22':
    name: Up
    mode: input
    active: low
  '23':
    name: Right
    mode: input
    active: low
  '24':
    name: Down
    mode: input
    active: low
  '25':
    name: Left
    mode: input
    active: low
  '26':
    name: B
    mode: input
    active: low
  '27':
    name: A
    mode: input
    active: low
i2c:
-->
#Score:Zero

Score:Zero is a simple-soldering-kit-come-games-controller for the Raspberry Pi Zero. It has eight active-low pushbuttons connected to various GPIO pins. On the underside of the board there are also solder pads connected to power, ground, I2C, SPI and serial comms. 

Use this section to provide additional information such as features, technical parts, install requirements, etc. Please keep this section to the point and avoid copy/paste of marketing blurb - the board's extended description should be primarily neutral and technical.

The overlay itself uses the following fields, some of which are mandatory, as noted below:

MANDATORY
* name: the board name as it will appear at pinout.xyz
* class: the class the overlay falls in, 'board' is the most common (use that if in doubt).
* type: the typical applications of the board, i.e 'lcd' (use 'other' if in doubt). If multiple types apply, use a comma separated list (for example, 'adc,motor'). The keywords submitted will be used to filter boards on the site so don't include anything but tags that are relevant to the key functionality of the board.
* formfactor: the board's form factor. Valid values are Custom, HAT and pHAT. Note that an EEPROM is required for HAT specs, use Custom if that is not the case.
* manufacturer: the manufacturer's name.
* description: a description of what the add-on board provides.
* url: the main URL for the product providing detailed technical information about the board.
* pin: an array of the pins used. Do not specify power or EEPROM pins as part of the array!

DESIRABLE
* pincount: the header pin count, typically 26 or 40 but shims/custom boards are acceptable.
* eeprom: whether the board includes an eeprom (required by 'HAT' specs!).
* power: the supply logic required by the board. Valid values are 'external', '3v3', '5v' and '3v3,5v'.
* i2c: if the board uses i2c, a list of the bus address(es) and device(s) identification.

OPTIONAL
* image: a top-down image of the board as png with transparency or appropriate placeholder (see image template in board directory).
* github: github repository address.
* buy: URL where the board can be purchased.
