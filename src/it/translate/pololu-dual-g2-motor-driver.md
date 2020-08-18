<!--
---
name: Dual G2 High-Power Motor Driver
class: board
type: motor
formfactor: HAT
manufacturer: Pololu
description: A high-power motor driver board for the Raspberry Pi
url: https://shop.pimoroni.com/collections/raspberry-pi/products/pololu-dual-g2-high-power-motor-driver-for-raspberry-pi
buy: https://shop.pimoroni.com/collections/raspberry-pi/products/pololu-dual-g2-high-power-motor-driver-for-raspberry-pi
image: 'pololu-dual-g2-motor-driver.png'
pincount: 40
eeprom: no
power:
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
    name: Motor 1 Fault
    mode: input
    active: low
    pull: high
  '31':
    name: Motor 2 Fault
    mode: input
    active: low
    pull: high
  '32':
    name: Motor 1 PWM
    mode: output
    active: high
  '33':
    name: Motor 2 PWM
    mode: output
    active: high
  '15':
    name: Motor 1 Sleep
    mode: output
    active: high
    external_pull: low
  '16':
    name: Motor 2 Sleep
    mode: output
    active: high
    external_pull: low
  '18':
    name: Motor 1 Direction
    mode: output
  '22':
    name: Motor 2 Direction
    mode: output
-->
# Pololu Dual G2 High-Power Motor Driver

The Pololu Dual G2 Motor Driver is designed to drive two large brushed DC motors, and is available in 24v14, 18v18 and 18v22 versions.

* Dual discrete MOSFET H-bridges
* PWM operation up to 100 kHz
* Motor indicator LEDs
* Integrated 5V, 2.5A regulator for powering Raspberry Pi
* 18v at 22A, 18v at 18A and 24v at 14A versions available
* Up to 36V input voltage
* Minimum 6.5V input voltage
* Does not include ID EEPROM (optional footprint available)
* Reverse-voltage protection
* Under-voltage shutdown
* Short circuit protection