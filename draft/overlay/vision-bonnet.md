<!--
---
name: AIY Vision Bonnet
class: board
type: sensor,other
formfactor: pHAT
manufacturer: Google
description: A pHAT that helps you build an intelligent camera that can see and recognize objects using machine learning
url: https://aiyprojects.withgoogle.com/vision
github: https://github.com/google/aiyprojects-raspbian
image: 'vision-bonnet.png'
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
  '15':
    mode: gpio
    name: Buzzer
  '16':
    mode: gpio
    name: Button
  '19':
    mode: spi
  '21':
    mode: spi
  '23':
    mode: spi
  '24':
    mode: spi
  '31':
    mode: gpio
    name: Pi to Myriad IRQ
  '33':
    mode: gpio
    name: Myriad to Pi IRQ
  '37':
    mode: gpio
-->
# AIY Vision Bonnet

The AIY Vision Bonnet comes with the AIY Vision Kit by Google—a do-it-yourself intelligent camera. The Vision Bonnet connects to a Raspberry Pi Zero to create an intelligent camera that can see and recognize objects using machine learning (ML).

The bonnet includes on-board hardware to accelerate vision-based ML models, a connector for the Raspberry Pi Camera v2, a 10-pin button connector, and 4 unique GPIO pins called `PIN_A`, `PIN_B`, `PIN_C`, and `PIN_D`.

