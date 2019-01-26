<!--
---
name: RASPIAUDIO AUDIO+ SPEAKERS+ MIC+
class: board
type: audio,io
formfactor: HAT ZERO FORMAT
manufacturer: RASPIAUDIO
description: An I2S digital to analog audio converter with 2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS and detachable ONBOARD I2S MICROPHONE
buy: https://raspiaudio.com
image: 'audioplus_speakerplus_micplus.png'
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
#Audio+ Speaker+ Microphone+ 
##2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS

* Experiment with the Google AIY assistant (100% pin to pin compatible).
 
* Use open source assistants such as ADRIAN, SNIPS project and others

* Voice changer

* Great for any portable radio project where you need a built in speaker

* Power your old speaker directly

* No extra power supply required

##Features:

1. Microphone I2S High sensitivity on board (can be separate from the main boad using the included cable)

2. 2x5w Stereo Amplification anf 2 onboard speaker included

3. DAC I2s 24-bit audio with studio sampling quality

4. Line out stereo 3.5mm jack

5. Onboard red button, 1 status led

6. Extension screw terminal for external speakers (2 to 8 ohm)

7. Extension screw terminal for external push button and external led.

8. Soldered Long female header 2x20 (NO soldering required) Compatible with Raspberry Pi 3, 2, B+, A+, and Zero

##INSTALLATION:

* Plug Audio+ firmly on top of your Raspberry Pi GPIO and turn on your Pi

* Open a terminal and type the following to download and run the installer:

```bash
sudo wget -O mic mic.raspiaudio.com

sudo bash mic
```
* Say yes to reboot
* On the next reboot you must run the test to finish the installation (it is an ALSA oddness):

```bash
sudo wget -O test test.raspiaudio.com

sudo bash test
```

* Push the onboard button, you should hear "Front Left" "Front Right" then the recorded sequence by the microphone. 

* If the volume is too low you can adjust the gain of the microphone by rebooting and typing the following into a terminal:

```bash
alsamixer
```


