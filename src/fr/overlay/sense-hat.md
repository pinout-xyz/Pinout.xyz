<!--
---
description: Carte d'extension incluant une metrice LED 8×8 en RGB, un joystick 5 boutons ainsi qu'un capteur IMU, de température et de pression.
pin:
  '22':
    name: Atmel Reset
  '24':
    name: Atmel Selection
i2c:
  '0x5c':
    name: Pression/Temp
  '0x5f':
    name: Humidité/Temp
  '0x6a':
    name: Accéléromètre
  '0x1c':
    name: Magnétomèter
  '0x46':
    name: Matrice LED
-->
# Sense HAT

Sense HAT est une carte d'extension pour Raspberry Pi composé d'une matrice LED 8x8 en RGB (rouge, vert, bleu), d'un joystick 5 boutons (directions+appui), et ainsi qu'un capteur IMU, de température, d'humidité et de pression.

Le registre à décalage (shift register) utilisé pour la matrice de LED est un LED2472G connecté par un microcontrôleur Atmel ATTINY88 acessible en i2c à l'adresse 0x46 (70) du Pi. Le switch/Joystick multidirectionnel SKRHABE010 est aussi piloté par le ATTINY88.

Les capteurs eux-mêmes sont pilotés par le bus i2c:

* le capteur IMU via un LSM9DS1 trouvable à l'adresse i2c 0x1c-0x1e (28-30) et 0x6a-0x6b (106-107), avec interruption par le ATTINY88,
* Le capteurs de pression/température est un LPS25H disponible à l'adresse i2c 0x5c (92),
* le capteurs d'humidité/températeur HTS221 est lui accessible à l'adresse i2c 0x5f (104).

Note: le microcontrôleur Atmel peut être reprogrammé en utilisant le bus SPI. Seuls les broches de reset et sélection sont representées ici et ajouter des périphériques SPI devrait être possible, moyennant quelques précautions.
