<!--
---
name: DiscoHAT
class: board
type: audio
formfactor: HAT
manufacturer: Kertatuote
description: Computer controlled DMX lights, sounds and special effects
url: http://discohat.com
buy: http://discohat.com/shop
image: 'discohat.png'
pincount: 40
eeprom: yes
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
  '8':
    name: TXD
    active: high
    mode: output
    description: DMX out
  '13':
    name: Button1
    active: low
    mode: input
    description: Button 1
  '15':
    name: Button2
    active: low
    mode: input
    description: Button 2
  '22':
    name: Button3
    active: low
    mode: input
    description: Button 3
  '18':
    name: Button4
    active: low
    mode: input
    description: Button 4
  '16':
    name: Button5
    active: low
    mode: input
    description: Button 5
  '37':
    name: Button6
    active: low
    mode: input
    description: Button 6
  '32':
    name: Button7
    active: low
    mode: input
    description: Button 7
  '36':
    name: Button8
    active: low
    mode: input
    description: Button 8
  '19':
    name: MOSI
    mode: spi
    description: LED strip data
  '23':
    name: SCLK
    mode: spi
    description: LED strip clock
-->
#DiscoHAT

###DiscoHAT is a small board allowing you to do computer controlled lights, sounds and special effects.

It is an essential building block for making custom light and sound systems. You can easily create your own home disco based on it. It is also usable for small theatre groups, bands or school projects.

With DiscoHAT you can control DMX equipment and LED strips. It also has interfaces for up to 8 pushbuttons that can be configured to start light and sound sequences.

DiscoHAT was created to be used with QLC+ an Open Source light and sound control software that is absolutely AMAZING. The push buttons can trigger scenes (steady lights), chases (lights changing in a pattern) and shows (lights synced to music) from stage without need for displays, keyboards or mice. With a WiFi dongle you can also control the lights from your tablet or mobile phone.

The Raspberry Pi 2 has a bit more power and is recommended for DiscoHAT. You can also exchange the 40 pin connector with the 26 pin connector for using it on older Raspberries but then you lose HAT functionality and 4 buttons. The connectors are not soldered to DiscoHAT. It uses SMD through pin sockets.

DiscoHAT is being used by myself in our theater productions. The DMX output and the pushbuttons are optically isolated and ESD protected to cope with static electricity that easily builds up on stage due to long wires, hot air, plastic surfaces and nylon clothing.

The system has been in use for two plays so far and it is time to share the good things with other entertainers.

Break a leg,

Karri
