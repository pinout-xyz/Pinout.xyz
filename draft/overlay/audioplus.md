<!--
---
name: RASPIAUDIO AUDIO+
class: board
type: audio
formfactor: Pi ZERO
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter
buy: https://raspiaudio.com
image: 'audioplus.png'
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
#Audio +

 RaspiAudio enables your Raspberry Pi ( Pi 3, 2, B+, A+, and Zero) with a state of the art audio DAC at a reasonable price.

Great for home audio sound sytem, internet radio, or any project with audio at a price that makes sense.

1- DAC I2s 24-bit 96KHz audio with studio sampling quality

2- Included dual RCA phono connector line out stereo (soldering required)

3- Line out stereo jack 3.5mm

4- Female header 2x20 (soldering required) Compatible with Raspberry Pi 3, 2, B+, A+, and Zero


-Insert your Rapsberry Pi Audio Shield in your Raspberry pI then turn it on

-Make sure your audio jack is plugged in to your amplifier

-Open a terminal (yes the black windows thing) and type:


```bash
sudo wget -O - script.raspiaudio.com | bash
```
-say yes for the reboot
-If everything went fine you should here a test sound when tryping this command:

```bash
sudo speaker-test -l5 -c2 -t wav
```


-NEW! : On the next reboot you will be able to control the volume from your desktop or by using the line command tool alsamixer



