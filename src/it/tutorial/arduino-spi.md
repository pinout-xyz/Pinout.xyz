<!--
---
name: Arduino SPI
description: Programma Arduino con le porte  SPI del Raspberry Pi
pin:
  '19':
    name: MOSI
    direction: output
    active: high
    description: Master Out / Slave In
  '21':
    name: MISO
    direction: input
    active: high
    description: Master In / Slave Out
  '23':
    name: SCKL
    direction: output
    active: high
    description: Clock
  '24':
    name: CE0
    direction: output
    active: high
    description: Arduino Reset
-->
#ATmega 328p / Arduino via SPI

###Sapevi che il tuo Raspberry può alimentare e programmare un ATmega 328p/Arduino direttamente, soltanto con pochi cavi, una breadboard, un oscillatore a 16Mhz ed alcuni condensatori da 22pF?

Leggi il mio [tutorial completo a Pico PiDuino](http://pi.gadgetoid.com/article/building-the-pico-piduino) per imparare le basi con poco più di 5&pound;.

Dovrai installare l'[AVRDude modificato di Gordon Henderson](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/).

Collega 8/CEO al pin Reset/RST dell'ATmega, il 9/MISO al pin MISO (D12), il 10 al pin MOSI (D11) e 11/SCLK al pin SCLK (D13).

Alimenta l'ATmega con i 3.3v e la massa (pin GND) del tuo Raspberry, e sei pronto a procedere.

Assicurati di non avere alcun malefico driver SPI in esecuzione e controlla che sia collegato correttamente con:

```bash
avrdude -p m328p -c gpio
```

Per fare i primi tentativi con la compilazione per Arduino, lancia da un terminale:

```bash
sudo apt-get install arduino arduino-mk
```

Questo Makefile essenziale dovrebbe darti le basi. Per creare un semplice progetto, dagli nome mysketch.ino e lancia:

```bash
export BOARD=atmega328
make
avrdude -p m328p -c gpio -e -U flash:w:build-cli/Arduino.hex
```
