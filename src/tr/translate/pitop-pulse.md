<!--
---
name: pi-topPULSE
class: board
type: audio,io,led,sensor,multi
formfactor: HAT
manufacturer: pi-top
collected: Other
description: 7×7 RGB LED matrix, speaker and microphone
url: http://pi-top.com/products/pulse
github: https://github.com/pi-top/pi-topPULSE
buy: http://pi-top.com/products/pulse
image: 'pitop-pulse.png'
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
  '3':
    mode: i2c
  '5':
    mode: i2c
  '8':
    mode: uart
  '10':
    mode: uart
  '12':
    name: BCKL
    mode: i2s
  '35':
    name: LRCK
    mode: i2s
  '40':
    name: DOUT
    mode: i2s
i2c:
  '0x24':
    name: Feature-enable IC
    device: pca9570
install:
  'devices':
    - 'i2s'
    - 'i2c'
  'apt':
    - 'pt-pulse'
    - 'python-pt-pulse'
    - 'python3-pt-pulse'
-->
#pi-topPULSE

The pi-topPULSE is a Raspberry Pi HAT and a pi-top/pi-topCEED compatible add-on board comprising of a 7x7 LED array, a speaker and a microphone. Additionally the device features ambient lights: 4 around the speaker, and 3 on the underside.

The speaker uses I2S, and the LEDs and microphone use serial (UART) - Tx and Rx respectively. A PCA9570 IC is exposed at I2C address 0x24, which allows for enabling/disabling/probing the on-board speaker, MCU and EEPROM as well as toggling the microphone sampling rate between 16KHz and 22KHz.
