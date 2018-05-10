<!--
---
name: RASPIAUDIO AUDIO+ SPEAKERS+
class: board
type: audio,io
formfactor: HAT ZERO FORMAT
manufacturer: RASPIAUDIO
collected: Other
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
2X5W STEREO AMP FOR ONBOARD/EXTERNAL SPEAKERS

-Any portable radio project where you need built in speaker

-Power directly your old speaker

-No extra power supply required



INSTALLATION for Raspian users:

-Insert your Rapsberry Pi Shield in your Raspberry pI then turn it on

-Open a terminal (yes the black window thing) and type this to download the bash file and run it:

```bash
sudo wget -O - script.raspiaudio.com | bash
```

-Say yes for the reboot

-On the next reboot you  have to run the test to finish the installation (it is an ALSA oddness):

```bash
sudo speaker-test -l5 -c2 -t wav
```

On the next reboot you will be able to control the volume from your desktop or by using the line command tool alsamixer 



Features:

(There is no microphone on this board, for microphone see our other model MIC+)

2. 2x5w Stereo Amplification 2 onboard speaker included

3. DAC I2s 24-bit audio with studio sampling quality

4. Line out stereo 3.5mm jack

5. Onboard red button, 1 status led

6. Extention screw terminal for external speakers (2 to 8 ohm)

7. Extention screw terminal for external push button, external led.

8. Soldered Long female header 2x20 (NO soldering required) Compatible with Raspberry Pi 3, 2, B+, A+, and Zero



