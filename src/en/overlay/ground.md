<!--
---
name: Ground
class: interface
type: pinout
description: Raspberry Pi Ground Pins
pincount: 1
pin:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
-->
#Ground

The Ground pins on the Raspberry Pi are all electrically connected, so it doesn't matter
which one you use if you're wiring up a voltage supply.

Generally the one that's most convenient or closest to the rest of your connections is tidier
and easier, or alternatively the one closest to the supply pin that you use.

For example, it's a good idea to use Physical Pin 17 for 3v3 and Physical Pin 25 for ground when using
the SPI connections, as these are right next to the important pins for SPI0.
