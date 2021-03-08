<!--
---
name: I2S PCM5102 DAC
class: board
type: Audio
formfactor: Custom
manufacturer: DiyMore
description: I2S PCM5102A DAC With 3.5mm Jack Out
url: https://www.diymore.cc/collections/wifi-module/products/i2s-pcm5102-dac-decoder-32bit-player-module-than-es9023-pcm1794-for-raspberry-pi?_pos=4&_sid=786fea80b&_ss=r
image: 'dmi2spcm5102dac.png'
pincount: 11
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
    name: BCK
  '35':
    name: LCK
  '40':
    name: DIN
-->
#I2S PCM5102 DAC

- 24-bit audio at 192KHz
- Line out stereo jack
- Uses the PCM5102A DAC & I2S interface

Only 3 data pins plus power and gnd are needed. Just a short explanation what all of the grounded pins do:

- FLT: Filter select. GND for normal latency, pull up (10k 3,3V) for low latency
- DMP: de-emphasis control. Low = off, high = on
- SCL: if to GND internal SCK will be generated from BCK
- FMT: audio data format selection. Low for I2S (high for Left-Justified)
- XMT: pulled to GND = mute, pulled high via 10k to 3.3V un-mute

Also see: <https://blog.sengotta.net/connecting-a-pcm5102a-breakout-board-to-a-raspberry-pi/>

##Pins from DAC board to Pi GPIO

- VCC <–> Pin 2 / 5v Power
- 3.3V <–> See XMT Pin below
- GND <–> GND
- FLT <–> GND
- DMP <–> GND
- SCL <–> GND
- BCK <–> Pin 12
- DIN <–> Pin 40
- LCK <–> Pin 35
- FMT <–> GND
- XMT <–> See XMT Pin below

##XMT Pin
- XMT <–> 10k Resistor <–> 3.3V Pin of the PCM5102A board to un-mute

Now you can install Volumio etc on your Pi, enable I2S, select the Hifiberry DAC and play your Music!

