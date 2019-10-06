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
image: 'aiy-vision-bonnet.png'
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

El bonnet de AIY Vision viene con el kit de AIY Vision de Google, para hacer una cámara inteligente conectándose a Raspberry Pi. Esta cámara puede ver y reconocer objetos usando los modelos de aprendizaje de máquinas (ML) incluidos en el dispositivo.

Este bonnet incluye hardware para acelarar los modelos ML, un conector de cámara v2 para Raspberry Pi, un conector de botones de 10 pines y 4 GPIO llamados `PIN_A`, `PIN_B`, `PIN_C`, y `PIN_D`.
