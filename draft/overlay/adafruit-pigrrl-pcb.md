<!--
---
name: PiGRRL Gamepad
class: board
type: io
formfactor: Custom
manufacturer: Adafruit
description: An add-on board for the Raspberry Pi
url: https://learn.adafruit.com/pigrrl-2
buy: https://www.adafruit.com/product/3015
image: 'adafruit-pigrrl-pcb.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '8':
    name: 'Button A'
    mode: input
    active: low
  '10':
    name: 'Button B'
    mode: input
    active: low
  '12':
    name: 'Button Y'
    mode: input
    active: low
  '32':
    name: 'Button L'
    mode: input
    active: low
  '33':
    name: 'Button R'
    mode: input
    active: low
  '38':
    name: 'Button X'
    mode: input
    active: low
  '7':
    name: 'D-Pad Left'
    mode: input
    active: low
  '29':
    name: Select
    mode: input
    active: low
  '31':
    name: Start
    mode: input
    active: low
  '35':
    name: 'D-Pad Right'
    mode: input
    active: low
  '36':
    name: 'D-Pad Up'
    mode: input
    active: low
  '37':
    name: 'D-Pad Down'
    mode: input
    active: low
-->
#PiGRRL Gamepad

The PiGRRL Gamepad PCB is designed for use in portable gaming projects like the PiGRRL 2 but it's basically a set of buttons wired between ground and select GPIO.

All button inputs should be configured with their corresponding internal pull-ups. Note that there are no protection circuitry, so be sure not to drive the GPIO high and short them to ground via button actions!
