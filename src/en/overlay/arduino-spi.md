<!--
---
type: content
name: Arduino SPI
description: Program Arduino with Raspberry Pi SPI
pincount: 4
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
#ATmega 328p / Arduino over SPI

###Did you know that your Pi could power and program an ATmega 328p/Arduino directly, with nothing but a few wires, a breadboard, a 16Mhz crystal oscillator and some 22pF capacitors?

Read my [complete Pico PiDuino tutorial](http://pi.gadgetoid.com/article/building-the-pico-piduino) to get started for just over &pound;5

You'll need to install [Gordon's modified AVRDude](https://projects.drogon.net/raspberry-pi/gertboard/arduino-ide-installation-isp/).

Connect 8/CEO to your ATmega's Reset/RST pin, 9/MISO to its MISO pin (D12), 10 to its MOSI pin (D11) and 11/SCLK to its SCLK pin (D13).

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
