<!--
---
name: Arduino SPI
description: Programmer une carte Arduino avec une Raspberry Pi
pin:
  19:
    name: MOSI
    direction: output
    active: high
    description: Master Out / Slave In
  21:
    name: MISO
    direction: input
    active: high
    description: Master In / Slave Out
  23:
    name: SCKL
    direction: output
    active: high
    description: Clock
  24:
    name: CE0
    direction: output
    active: high
    description: Arduino Reset
-->
#ATmega 328p / Arduino over SPI

###Saviez-vous qu'il était possible de programmer une carte Arduino ou un ATmega328 à partir d'une Raspberry Pi, en utilisant juste quelques câbles, un 'breadboard', un quartz de 16 MHz et quelques condensateurs?

Voici un article qui vous guidera dans cette entreprise:
[complete Pico PiDuino tutorial](http://pi.gadgetoid.com/article/building-the-pico-piduino)

Une fois votre 'Arduino' assemblé, il vous faudra installer une version modifiée de [AVRDude](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/).

Ensuite:

Connectez la broche 8 de la Raspi à l'ATmega Reset/RST, la broche 9 à son MISO/D12, la broche 10 à son MOSI/D11, et finalement la broche 11 au SCLK/D13.

Alimentez votre ATmega en 3.3 volts et raccordez le à la masse. Pour ce faire, vous pouvez utiliser les broches de la Raspi.

Vous voilà fin prêt. Assurez vous que vous n'avez pas de drivers SPI parasites sur le bus et que l'ATmega est bien détecté:

```bash
avrdude -p m328p -c gpio
```

Et finalement installez les derniers logiciels requis:

```bash
sudo apt-get install arduino arduino-mk
```

Puis voyez les détails associés à la compilation en elle-même dans [l'article suivant](http://pi.gadgetoid.com/article/programming-your-pico-piduino)!