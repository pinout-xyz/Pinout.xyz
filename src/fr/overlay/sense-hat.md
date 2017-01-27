<!--
---
name: Sense HAT
class: board
type: led,sensor
formfactor: HAT
manufacturer: Raspberry Pi
description: Carte d'extension incluant une metrice LED 8×8 en RGB, un joystick 5 boutons ainsi qu'un capteur IMU, de température et de pression.
url: https://www.raspberrypi.org/products/sense-hat/
github: https://github.com/RPi-Distro/python-sense-hat
schematic: https://www.raspberrypi.org/documentation/hardware/sense-hat/images/Sense-HAT-V1_0.pdf
buy: https://thepihut.com/products/raspberry-pi-sense-hat-astro-pi
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
  '16':
    name: IMU Interrupt
    mode: output
  '18':
    name: IMU Interrupt
    mode: output
  '22':
    name: Atmel Reset
    mode: output
    active: high
  '24':
    name: Atmel Selection
    mode: chipselect
    active: high
i2c:
  '0x5c':
    name: Pression/Temp
    device: lps25h
  '0x5f':
    name: Humidité/Temp
    device: hts221
  '0x6a':
    name: Accéléromètre
    device: lsm9ds1
  '0x1c':
    name: Magnétomèter
    device: lsm9ds1
  '0x46':
    name: Matrice LED
    device: led2472g
install:
  'devices':
    - 'i2c'
-->
#Sense HAT

Sense HAT est une carte d'extension pour Raspberry Pi composé d'une matrice LED 8x8 en RGB (rouge, vert, bleu), d'un joystick 5 boutons (directions+appui), et ainsi qu'un capteur IMU, de température, d'humidité et de pression.

Le registre à décalage (shift register) utilisé pour la matrice de LED est un LED2472G connecté par un microcontrôleur Atmel ATTINY88 acessible en i2c à l'adresse 0x46 (70) du Pi. Le switch/Joystick multidirectionnel SKRHABE010 est aussi piloté par le ATTINY88.

Les capteurs eux-mêmes sont pilotés par le bus i2c:

* le capteur IMU via un LSM9DS1 trouvable à l'adresse i2c 0x1c-0x1e (28-30) et 0x6a-0x6b (106-107), avec interruption par le ATTINY88,
* Le capteurs de pression/température est un LPS25H disponible à l'adresse i2c 0x5c (92),
* le capteurs d'humidité/températeur HTS221 est lui accessible à l'adresse i2c 0x5f (104).

Note: le microcontrôleur Atmel peut être reprogrammé en utilisant le bus SPI. Seuls les broches de reset et sélection sont representées ici et ajouter des périphériques SPI devrait être possible, moyennant quelques précautions.
