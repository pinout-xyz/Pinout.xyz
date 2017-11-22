<!--
---
name: NadHAT v1
class: board
type: IOT,ADC
formfactor: pHAT
manufacturer: Garatronic
description: An GSM/GPRS add-on board for the Raspberry Pi
url: https://www.garatronic.fr
github: https://github.com/garatronic/nadhat
schematic: https://github.com/garatronic/nadhat/tree/master/hardware/nadhat_v1_schematics.pdf
buy: https://www.amazon.co.uk/NadHAT-GPRS-expansion-board-Raspberry/dp/B076M83F38
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

NadHAT v1 is a GSM/GPRS modem pHAT for the Raspberry pi based on Simcom SIM800C standard module, gammu and pppd compatible for SMS and DATA exchange.

It have a timekeeper with CR1225 coin cell, one 10 bits ADC channel, 2 status LEDS and an efficient switched mode DC/DC converter. It needs a micro sim card line suscriber to work with it.

To install the necessary software, use the following commands:

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
