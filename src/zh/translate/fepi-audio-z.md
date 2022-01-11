<!--
---
name: Fe-Pi Audio Z
class: board
type: audio
formfactor: pHAT
manufacturer: Fe-Pi
description: A complete audio solution for the Raspberry Pi
url: http://fe-pi.com/products/fe-pi-audio-z-v1
buy: http://fe-pi.com/products/fe-pi-audio-z-v1
image: 'fepi-audio-z.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: BCLK (Bit Clock)
    mode: i2s
  '35':
    name: LRCLK (Left/Right Clock)
    mode: i2s
  '38':
    name: DIN (Data In)
    mode: i2s
  '40':
    name: DOUT (Data Out)
    mode: i2s
i2c:
  '0x0a':
    name: SGTL5000
    device: SGTL5000XNAA3/R2
-->
# Audio Z

The Fe-Pi Audio Z is designed to provide a complete low cost audio solution for Raspberry Pi 2, 3, and Zero, needing line-in, line-out, and headphone-out/mic-in.

## Features

* Small Raspberry Pi Zero PCB footprint
* 3.5 mm, 4 contact, jack for Headphone/MIC (black)
* 3.5 mm jack for stereo Line Out (green), and stereo Line In (pink)
* ADC > 90 dB SNR and -72 dB THD+N
* Line-Out > 100 dB SNR and -85 dB THD+N
* HP Output > 100 dB SNR and -80 dB THD+N, 62.5 mW max into 16 ohm
* Hardware level controls for Headphone Volume, Line In, Line Out. ALSA support
* 2x20pin 2.54mm female header and 40pin male breakable header included
 
