<!--
---
name: Picon Zero
class: board
type: moteur
formfactor: pHAT
image: '4tronix-picon-zero.png'
manufacturer: 4tronix
description: Une carte de contrôle de robot pour le Raspberry Pi
url: http://4tronix.co.uk/piconzero/
buy: http://4tronix.co.uk/store/index.php?rt=product/product&product_id=552
pincount: 40
eeprom: no
power:
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
  '38':
    name: Ultrasonic
    mode: input/output
i2c:
  '0x22':
    name: PiconZero
    device: ATMega328
-->
#Picon Zero

Le **Picon Zero** est une carte chapeau au format pHat (pseudo-Hat) pour le **Raspberry Pi Zero**. La carte peut, bien evidemment, être utilisée sur les autres Raspberry pi grâce au connecteur GPIO 40 broches.

En plus de 2 pilotes moteur **H-Bridge**, Le **Picon Zero** a un ensemble d'entrée/sorties entièrement paramétrables, vous permettant facilement de rajouter des entrées analogiques ou sorties neopixel à votre Raspeberry Pi sans logiciels ou kernel compliqués ou spécifiques. La carte propose aussi une interface **HC-SR04** pour capteur de distance ultrasonique et libère aussi 5 port GPIO de votre Raspberry Pi.
