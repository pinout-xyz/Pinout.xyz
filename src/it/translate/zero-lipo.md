<!--
---
name: Zero LiPo
class: board
type: power
formfactor: Custom
manufacturer: Pimoroni
description: LiPo/LiIon power supply shim for Raspberry Pi
url: https://shop.pimoroni.com/products/zero-lipo
buy: https://shop.pimoroni.com/products/zero-lipo
image: 'zero-lipo.png'
pincount: 8
eeprom: no
power:
  '2':
ground:
  '6':
pin:
  '7':
    name: Battery Low
    mode: input
    active: high
-->
#Zero LiPo

The Zero LiPo aims to give you the most compact Raspberry Pi power supply possible.

The board includes power on and battery low indicator LEDs as well as a JST connector, to which you can connect a LiPo, LiIon, or other battery with a JST plug. The TPS61232 step-up boost converter from Texas Instruments converts the 3-4.2V input voltage from the LiPos/LiIons to 5V, providing a stable 5V supply perfect for your Pi.

Features:

* 0.8mm thick PCB
* Shaped to sit as low as possible on the Raspberry Pi 3, 2, Zero, A+, B+
* 2-pole JST connector ideal for most LiPo/LiIon batteries
* Power and low battery LED indicators
* Supplies up to 1.5A continuous current
* Low battery warning at 3.4V (assets GPIO #4 high)
* Automatic shutdown at 3.0V to protect your battery
* VBAT+, GND, and EN pins available to break out
* 15uA quiescent current
