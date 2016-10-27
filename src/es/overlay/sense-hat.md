<!--
---
name: Sense HAT
class: board
type: led,sensor
formfactor: HAT
manufacturer: Raspberry Pi
description: Add-on board that includes an 8×8 RGB LED matrix, 5-button joystick as well as IMU and environmental sensors
url: https://www.raspberrypi.org/products/sense-hat/
image: 'sense-hat.png'
pincount: 40
eeprom: setup
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
i2c:
  '0x5c':
    name: Pressure/Temp
    device: lps25h
  '0x5f':
    name: Humidity/Temp
    device: hts221
  '0x6a':
    name: Accelerometer
    device: lsm9ds1
  '0x1c':
    name: Magnetometer
    device: lsm9ds1
  '0x46':
    name: LED Matrix
    device: led2472g
install:
  'devices':
    - 'i2c'
-->
#Sense HAT

Sense HAT es una placa adicional para Raspberry Pi con una matriz led 8x8 RGB, un joystick de 5 botones y los siguientes sensores: giroscopio, acelerómetro, magnetómetro, temperatura, presión barométrica y humedad.

El controlador de la matriz LED es un LED2472G conectado mediante ATTINY88 y comunicándose mediante i2c en la dirección 0x46 con la Pi. El joystick multidireccional SKRHABE010 switch/joystick se controla de manera similar.

Los sensores también funcionan mediante el bus i2c:

Los IUM (giroscopio, acelerómetro y magnetómetro) a trabés de LSM9DS1 en las direcciones i2c 0x1c(0x1e),0x6a(0x6b), con interrupciones en el ATTINY88.

Los sensores medioambientales son un LPS25H presión+temperatura en la dirección 0x5c y un HTS221 humedad+temperatura en la dirección 0x5f del bus i2c.
