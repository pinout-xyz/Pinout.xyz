<!--
---
name: MeArm Pi
class: board
type: other
formfactor: HAT
manufacturer: Mime Industries
collected: Other
description: A Joystick control board for controlling the MeArm Pi
url: https://mime.co.uk
github: https://github.com/mimeindustries/mearm-pi-hat-pcb
schematic: http://learn.mime.co.uk/assets/mearm-pi-hat-schematic-v1.4.pdf
buy: https://shop.mime.co.uk
image: 'mearm-pi.png'
pincount: 40
eeprom: yes
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Base Servo
    mode: output
    active: high
  '11':
    name: Right Servo
    mode: output
    active: high
  '15':
    name: Left Servo
    mode: output
    active: high
  '19':
    name: Grip Servo
    mode: output
    active: high
  '23':
    name: RGB LED - green
    mode: output
    active: high
  '24':
    name: RGB LED - red
    mode: output
    active: high
  '26':
    name: RGB LED - blue
    mode: output
    active: high
  '29':
    name: Button 1
    mode: input
    active: high
  '31':
    name: Button 2
    mode: input
    active: high
i2c:
  '0x48':
    name: Joysticks
    device: PCF8591 ADC
-->
# MeArm Pi HAT

The MeArm Pi HAT is a joystick controller board for the MeArm Pi Robotic Arm Kit

## Features

 * An 8 bit I2C ADC (address 0x48) connected to two analogue joysticks
 * Access to the push buttons of the joysticks on GPIO
 * An RGB LED for output
 * A 6 pin port to connect to the servos on the arm

Power can be supplied to the Pi through the HAT or direct in to the Pi, but the servos are only supplied through the HAT to avoid strain on the Pi power supply.

The pinout of the 6 pin connector is:

<table>
  <tr>
    <td>+5v</td>
    <td>Left Servo</td>
    <td>Grip Servo</td>
  </tr>
  <tr>
    <td>GND</td>
    <td>Base Servo</td>
    <td>Right Servo</td>
  </tr>
</table>

Additionally the I2C and power lines are brought out on to a header for easy expansion with the following pinout from top to bottom:

1. SDA
2. 3V3
3. SCL
4. GND

