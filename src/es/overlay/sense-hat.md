<!--
---
name: "Sense HAT"
manufacturer: Raspberry Pi Foundation
url: https://www.raspberrypi.org/products/sense-hat/
description: Placa que incluye una matriz LED RGB de 8x8, joystick de 5 botones, un IMU y sensonres ambientales
install:
  'devices':
    - 'i2c'
    - 'spi'    
pincount: 40
pin:
  3:
    mode: i2c
  5:
    mode: i2c
  16:
    name: Joystick
    mode: entrada
  18:
    name: Joystick
    mode: entrada
  19:
    mode: spi
  21:
    mode: spi
  22:
    name: Joystick
    mode: entrada
  23:
    mode: spi
  24:
    mode: spi
-->
#Sense HAT

El Sense HAT es una placa para la Raspberry Pi que incluye una matrix RGB LED de 8x8, un joystick de 5 botones y los siguientes sensores:

Giroscopio, Acelerómetro, Magnetómetro, Termómetro, Barómetro, Presión e Higrómetro.

El controlador de la matriz LED es un LED2472G conectado vía un ATtiny88 al bus SPI de la Pi. El multidireccional botón/joystick SKRHABE010 está similarmente conectado al bus SPI.

Los sensores en si operan (mayoritariamente) a través del bus i2c:

El IMU (Giroscopio, Acelerómetro, Magnetómetro) a través de un LSM9DS1, en la dirección i2c 0x1c(0x1e), 0x6a(0x6b), con Interrups en el ATtiny88.

Los sensores ambientales están representados por un LPS25H, que incluye sensor de presión y temperatura, en la dirección 0x5c, y un HTS221, que incluye humedad y temperatura en la dirección 0x5f.
