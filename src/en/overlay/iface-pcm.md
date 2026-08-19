<!--
---
name: PCM
class: interface
type: pinout
description: Raspberry Pi PCM pins
pin:
  'bcm18':
    name: CLK
  'bcm19':
    name: FS
  'bcm20':
    name: DIN
  'bcm21':
    name: DOUT
-->
# PCM - Pulse-code Modulation

PCM (Pulse-code Modulation) is a digital representation of sampled analog. On the Raspberry Pi it's a form of digital audio output which can be understood by a DAC for high quality sound.

These are the pins you'll want for I2S (Inter-IC Sound), which is the signalling most audio HATs and DACs use and the name they usually give it.