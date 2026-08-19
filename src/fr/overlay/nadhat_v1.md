<!--
---
description: Carte d'extension GSM/GPRS pour le Raspberry Pi
buy: https://shop.mchobby.be/fr/pi-hats/1654-nadhat-gsmgprs-sim800c-v1-3232100016545-garatronic.html
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
