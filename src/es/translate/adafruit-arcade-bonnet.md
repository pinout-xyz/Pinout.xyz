<!--
---
name: Adafruit Arcade Bonnet
class: board
type: IO
formfactor: PHAT
manufacturer: Adafruit
description: Connect joystick,buttons and speakers to your pi
url: https://learn.adafruit.com/adafruit-arcade-bonnet-for-raspberry-pi
buy: https://www.adafruit.com/products/3422
image: adafruit-arcade-bonnet.png
pincount: 40
eeprom: no
power:
  '2':
  '1':
  '4':
  '17':     
ground:
  '6':
  '9':
  '14':
  '20':
  '30':
  '34':
  '39':
  '25':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S Clk
  '35':
    name: I2S FS
  '40':
    name: I2S Dout
i2c:
  '0x26':
    name: MCP23017
    device: MCP23017   
-->
#Adafruit Arcade Bonnet

This Adafruit Arcade Bonnet is designed to make small emulator projects a little easier to build. Here is some features!: 

It is the same size as a Pi Zero, so for really compact builds, this is super small. You can use it with a Pi 2, 3, B+ or any 2x20 connector Pi.

It has JST sockets so you can plug in six arcade buttons easily.

Header breakouts for use with both clicky-type switched joysticks and...

Header breakout and converter for using analog-type joysticks or thumbsticks with potentiometers inside

A 3W speaker output that can drive 4-8 ohm speakers for when using with a TV output, HDMI display or PiTFT.

Switches are all managed with an I2C-GPIO converter with interrupt out. The converter is very fast and frees up all the pins so you can use this Bonnet with a PiTFT or any other accessory/device that uses a lot of pins!

To install:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/arcade-bonnet.sh
sudo bash arcade-bonnet.sh
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```
