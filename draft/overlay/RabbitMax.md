<!--
---
name: RabbitMax Flex
class: board
type: infrared,relay,button,buzzer,led,sensors,lcd,uart
formfactor: HAT
manufacturer: Leon Anavi
description: RabbitMax Flex is a Raspberry Pi HAT board for IoT with an IR transmitter and receiver, relay, button, buzzer, RGB LED,  5x cable slots for I2C sensors, and a slot for 16x2 LCD display module.
url: http://rabbitmax.com/
github: https://github.com/RabbitMax
schematic:
buy: https://www.indiegogo.com/projects/rabbitmax-flex-raspberry-pi-hat-for-iot
image: 'anavi-rabbitmax-flex.png'
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
    name: LCD Display (RS)
  '11'
    name: IR LED
  '12'
    name: IR Receiver
  '13':
    name: LCD Display (Data 0)
  '15':
    name: LCD Display (Data 1)
  '19':
    name: LCD Display (Data 2)
  '21':
    name: LCD Display (Data 3)
  '23':
    name: Button
    mode: input
    active: low
  '27':
    mode: i2c
  '28':
    mode: i2c
  '29':
    name: Relay
  '31':
    name: Piezo Buzzer
  '33':
    name: RGB LED (blue)
  '35':
    name: RGB LED (green)
  '37':
    name: RGB LED (red)
  '40':
    name: LCD Display (E)
-->
#RabbitMax Flex
Flexible HAT for Raspberry Pi suitable for do it yourself (DIY) weather station, automated desk assistant or prototyping Internet of Things (IoT).
RabbitMax Flex Raspberry Pi HAT includes:

* Relay
* IR LED
* IR photo sensor
* Buzzer
* Button
* RGB LED
* Slot for modular LCD character display
* Slots for up to 5 plug and play I2C sensors

Some useful resources how to get started with RabbitMax Flex Raspberry Pi HAT:
* User's manual: http://rabbitmax.com/files/rabbitmax-flex.pdf
* Open source sample applications in Python and C: https://github.com/RabbitMax/rabbitmax-examples
