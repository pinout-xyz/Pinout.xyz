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

###Saviez-vous qu'il était possible de programmer une carte Arduino ou un ATmega328 à partir d'une Raspberry Pi, en utilisant juste quelques cables, un 'breadboard', Quartz de 16 MHz et quelques condensateurs?

Did you know that your Pi could power and program an ATmega 328p/Arduino directly, with nothing but a few wires, a breadboard, a 16Mhz crystal oscillator and some 22pF capacitors?

Voici un article qui vous guidera dans cette entreprise:
[Construire un Arduino](https://itechnofrance.wordpress.com/2013/04/13/construire-un-arduino/)

Une fois votre 'Arduino' assemblé, il vous faudra installer une version modifiée de [AVRDude](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/).

Connectez la broche 8 de la Raspi à l'ATmega Reset/RST, la broche 9 à son MISO/D12, la broche 10 à son MOSI/D11, et finalement la broche 11 au SCLK/D13.

Power your ATmega with the 3.3v and GND pins from your Pi, and you're good to go.

Make sure you have no rogue SPI device drivers running and check it's connected correctly using:

```bash
avrdude -p m328p -c gpio
```

To get started compiling Arduino sketches from the command line:

```bash
sudo apt-get install arduino arduino-mk
```

This basic Makefile should get you started. Create a basic sketch, name it mysketch.ino and run:

```bash
export BOARD=atmega328
make
avrdude -p m328p -c gpio -e -U flash:w:build-cli/Arduino.hex
```
