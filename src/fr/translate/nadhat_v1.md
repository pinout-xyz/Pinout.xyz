<!--
---
name: NadHAT v1
class: board
type: IOT,ADC
formfactor: pHAT
manufacturer: Garatronic
description: Carte d'extension GSM/GPRS pour le Raspberry Pi
url: https://www.garatronic.fr
github: https://github.com/garatronic/nadhat
schematic: https://github.com/garatronic/nadhat/tree/master/hardware/nadhat_v1_schematics.pdf
buy: https://www.amazon.fr/NadHAT-GPRS-expansion-board-Raspberry/dp/B076M83F38
image: 'nadhat_v1.png'
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
  '8':
    mode: uart
    name: TXD
  '10':
    mode: uart
    name: RXD
  '37':
    name: PWR_BT
    mode: output
    active: high
-->
# NadHAT v1

NadHAT v1 est un modem GSM/GPRS au format pHAT pour le Raspberry Pi, basé sur le module Simcom SIM800C. L'ensemble supporte gammu et pppd pour l'échange de SMS et de données.

Il dispose d'une horloge sauvegardée par pile bouton CR1225, d'un convertisseur analogique/numérique 10 bits, de 2 LEDs d'état et d'une alimentation à découpage à haut rendement. Il nécessite un abonnement téléphonique et d'une carte micro SIM pour son utilisation

Pour installer le logiciel nécessaire, utilisez les commandes suivantes:

```bash
sudo apt-get install minicom python-dev python-setuptools
sudo apt-get install python-serial python-pip git
sudo pip install wiringpi
sudo apt-get install wiringpi
cd ~
git clone https://github.com/garatronic/nadhat
cd nadhat/software
./nadpwr.sh
```
