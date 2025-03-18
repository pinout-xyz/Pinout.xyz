<!--
---
name: RASPIAUDIO AUDIO+
class: board
type: audio
formfactor: phat
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter
buy: https://raspiaudio.com
image: 'audioplus.png'
pincount: 40
eeprom: no
power:
  '1':
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
  '12':
    name: I2S
  '35':
    name: I2S
  '40':
    name: I2S
install:
  'devices':
  - 'i2s'
-->
# Audio +

RaspiAudio enables your Raspberry Pi ( Pi 3, 2, B+, A+, and Zero) with a state of the art audio DAC.

Great for home audio sound sytems, an internet radio, or any project with audio.

## Features

1. DAC I2s 24-bit 96KHz audio with studio sampling quality

2. Included dual RCA phono connector line out stereo (soldering required)

3. Line out stereo jack 3.5mm

4. Female header 2x20 (soldering required)

5. Compatible with Raspberry Pi 3, 2, B+, A+, and Zero

## INSTALLATION for Raspian users:

* Plug Audio+ firmly on top of your Raspberry Pi GPIO and turn on your Pi

* Make sure your audio jack is plugged in to your amplifier

* Open a terminal and type:

```bash
sudo wget -O - script.raspiaudio.com | bash
```

* Answer yes to reboot
* If everything went fine you should hear a test sound when typing this command:

```bash
sudo speaker-test -l5 -c2 -t wav
```

* NEW! : On the next reboot you will be able to control the volume from your desktop or by using the command-line tool `alsamixer`



