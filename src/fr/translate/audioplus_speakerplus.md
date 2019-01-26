<!--
---
name: RASPIAUDIO AUDIO+ SPEAKERS+
class: board
type: audio,io
formfactor: phat
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter with 2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS
buy: https://raspiaudio.com
image: 'audioplus_speakerplus.png'
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
  '12':
    name: I2S Clock
  '16':
    name: Button
    mode: input
    active: low
  '22':
    name: LED
    mode: output
    active: high
  '35':
    name: I2S WS
  '40':
    name: I2S Data
install:
  'devices':
  - 'i2s'
-->
#Audio+ Speaker+ 
##2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS

* Great for any portable radio project where you need built in speaker

* Power your old speaker directly

* No extra power supply required

##Features:

(There is no microphone on this board, for a microphone see our other model MIC+)

1. 2x5w Stereo Amplification 2 onboard speaker included

2. DAC I2s 24-bit audio with studio sampling quality

3. Line out stereo 3.5mm jack

4. Onboard red button, 1 status led

5. Extension screw terminal for external speakers (2 to 8 ohm)

6. Extension screw terminal for external push button, external led.

7. Soldered Long female header 2x20 (NO soldering required) Compatible with Raspberry Pi 3, 2, B+, A+, and Zero

##INSTALLATION for Raspian users:

* Plug Audio+ firmly on top of your Raspberry Pi GPIO and turn on your Pi

* Open a terminal and type the following to download and run the installer:

```bash
sudo wget -O - script.raspiaudio.com | bash
```

* Say yes TO the reboot

* On the next reboot you have to run the test to finish the installation (it is an ALSA oddness):

```bash
sudo speaker-test -l5 -c2 -t wav
```

* Reboot again and you will be able to control the volume from your desktop or by using the command-line tool `alsamixer` 
