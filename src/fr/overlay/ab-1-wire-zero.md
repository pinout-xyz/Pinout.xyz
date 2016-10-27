<!--
---
name: 1 Wire Pi Zero
class: board
type: com.
formfactor: pHAT
manufacturer: AB Electronics
description: 1-Wire vers interface I2C
url: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/76/1-Wire-Pi-Zero
image: 'ab-1-wire-pi-zero.png'
pincount: 40
eeprom: no
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
  '0x18':
    name: DS2482
    device: DS2482-100
-->
#1 Wire Pi Zero

Le **1 Wire Pi Zero** de **AB Electronics UK** est une carte chapeau de communication supportant le protocole **1-Wire®** et conçu pour une utilisation avec le Raspberry Pi Zero. Un port I2C 5v est aussi disponible sur la carte.

Le port **1-Wire®** sur la carte chapeau **1 Wire Pi Zero** est conçu autour d'un pont **DS2482-100**: **I2C** vers **1-Wire®**. Le **DS2482-100** permet une conversion de protocole bi-directionnel entre le port **I2C** du Raspberry et n'importe quel equipement esclave **1-Wire®** attaché à la carte. Une diode de protection ESD permet de protéger la carte **1 Wire Pi Zero** et le Raspberry Pi Zero de toutes décharges électrostatiques sur le port **1-Wire®**. Les connections sur le port **1-Wire®** se font grâce à une prise **RJ-12** ou sur les points de soudures de la carte.

Le cavalier sur la carte permet de sélectionner l'addresse **I2C** de la carte **1 Wire Pi Zero** permettant ainsi d'utiliser la carte avec d'autres equipements sur le même bus.

[https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi](https://www.abelectronics.co.uk/kb/article/3/owfs-with-i2c-support-on-raspberry-pi "Configuring and using the 1-Wire® port on your Raspberry Pi")
