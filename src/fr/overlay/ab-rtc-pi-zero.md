<!--
---
name: RTC Pi Zero
class: board
type: htr
formfactor: pHAT
manufacturer: AB Electronics
description: Module Horloge pour le Raspberry Pi
url: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/70/RTC-Pi-Zero
image: 'ab-rtc-pi-zero.png'
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
  '0x68':
    name: DS1307
    device: DS1307
-->
#RTC Pi Zero

Le **RTC Pi Zero** est une carte chapeau horloge autonome pour le Raspberry Pi Zero. Cette carte garde en mémoire votre réglage date/heure quand le raspberry est non alimenté, ce qui lui donne la possiblité de récupérer la date et l'heure de la carte chapeau RTC au démarrage.

La carte chapeau **RTC Pi Zero** est alimenté via les ports GPIO du Raspberry Pi, elle étend aussi les connecteurs du GPIO pour permettre de rajouter une carte chapeau supplémentaires. Le **RTC Pi Zero** utilise une horloge **DS1307 RTC** et une batterie **CR2032** pour maintenir la date et l'heure quand l'alimentation principale du système n'est pas disponible.

Contrairement aux autres modules basé sur les horloges **DS1307 RTC**, le **RTC Pi Zero** inclu un convertisseur de niveau logique I2C qui vous permet de connecter d'autres cartes I2C 5v à votre Raspberry.

Les librairies **Arduino**, **C**, **Node.js**, **Windows 10 IOT**, **Python 2** et **Python 3** sont disponibles sur GitHub.
