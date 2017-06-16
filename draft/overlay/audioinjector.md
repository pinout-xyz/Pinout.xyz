<!--
---
name: Audio Injector
class: board
type: audio
formfactor: HAT
manufacturer: Flatmax Studios
collected: Other
description: High quality analog audio input and output
url: http://www.audioinjector.net/
buy: Amazon, ebay
image: 'audioinjector.png'
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
    name: SDA
    mode: i2c
  '5':
    name: SCL
    mode: i2c
    description: Button 1
  '12':
    name: BitClock
    mode: i2s
  '35':
    name: LRClock
    mode: i2s
  '38':
    name: DataIn
    mode: i2s
  '40':
    name: DataOut
    mode: i2s
-->
#Audio Injector

* Microphone: Inbuilt electret microphone with mixer controls. Allowing voice control or other applications.

* Headphones: 50 mW max power into 16 ohm and 30 mW max power into 32 Ohm headphones (check the updates to see more)

* Driver : ALSA

* Latency: As low as 0.54 ms in or out (that is 540 microseconds !)

* Linux : Already integrated into the Raspberry Pi kernel. If you have an older version of the kernel, simply run "rpi-update" if you need to. Edit /boot/config.txt and set dtoverlay=audioinjector-soundcard

* DAC and ADC : 96 kHz, 32 bit audio.

* Analog Voltage : 3.3 V rail to rail. Separate linear supply to reduce noise.

* GPIO : Standard 40 Pin header, broken out above the add on card to accept more add on cards and hats.

