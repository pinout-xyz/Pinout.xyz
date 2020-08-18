<!--
---
name: Fe-Pi Audio Z V2
class: board
type: audio
formfactor: pHAT
manufacturer: Fe-Pi
description: A complete audio solution for the Raspberry Pi
url: https://fe-pi.com/products/fe-pi-audio-z-v2
buy: https://fe-pi.com/products/fe-pi-audio-z-v2
image: 'fepi-audio-z-V2.png'
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
# Fe-Pi Audio Z V2

The Fe-Pi Audio Z V2 is designed to provide a complete low cost audio solution for Raspberry Pi 2, 3, and Zero, needing line-in, line-out, headphone-out/mic-in, and stereo speakers.

## Features

* Small Raspberry Pi Zero PCB footprint.
* SGTL5000 low power stereo codec.
* 3.5 mm, 4 contact, jack for Headphone/MIC (black).
* 3.5 mm jack for stereo Line Out (green), and stereo Line In (pink).
* ADC > 90 dB SNR and -72 dB THD+N
* Line-Out > 100 dB SNR and -85 dB THD+N
* HP Output > 100 dB SNR and -80 dB THD+N, 62.5 mW max into 16 ohm.
* Hardware level controls for Headphone Volume, Line In, Line Out. ALSA support.
* 2x20pin 2.54mm female header and 40pin male breakable header included!
* Optional RCA jack for Composite Video output when used with Raspberry Pi Zero.
