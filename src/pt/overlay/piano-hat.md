<!--
---
name: Piano HAT
description: A tiny Pi piano with 16 touch-sensitive buttons
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '7':
    name: Alert A
    mode: input
  '11':
    name: Reset A
    mode: output
  '13':
    name: Alert B
    mode: input
  '15':
    name: Reset B
    mode: output
i2c:
  '0x28':
    name: Cap Touch A
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
  '0x2b':
    name: Cap Touch B
    device: cap1188
    datasheet: http://ww1.microchip.com/downloads/en/DeviceDoc/CAP1188%20.pdf
-->
#Piano HAT

Piano HAT has 16 touch-sensitive buttons. 13 of these are a single Piano octave, the rest give you octave up/down and instrument select functionality.

It uses two Microchip CAP1188 chips with the i2c addresses 0x28 and 0x2b.

You can use the one-line product installer to get Piano HAT set up and ready to go, just:

```bash
curl get.pimoroni.com/pianohat | bash
```

And follow the instructions!
