<!--
---
name: WiFi Pants
class: board
type: power, iot
formfactor: pHAT
manufacturer: SLNGadget
description: WiFi and battery power for the Raspberry Pi
url: https://hackaday.io/project/8678-rpi-wifi
github: https://github.com/al177/esp_hat
buy: https://www.tindie.com/products/ajlitt/wifi-power-pants/
image: 'wifi-pants.png'
pincount: 40
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
  '13':
    name: ESP GPIO10
  '15':
    name: ESP SCLK
  '16':
    name: ESP CSO
  '18':
    name: ESP MISO
  '22':
    name: ESP MOSI
  '27':
    name: ESP CH_PD
  '37':
    name: ESP GPIO9
-->
#WiFi Pants

WiFi Pants is a WiFi and 5V boost power supply add-on board for your Raspberry Pi based around the ESP-12F.

The WiFi Pants board fits the outline of the Pi Zero, with only a small protrusion for the antenna, and only six GPIOs are needed on the Pi's expansion connector.

It communicates over the SDIO interface to provide WiFi capability for a direct alternative to a USB WiFi adapter for low-bandwidth applications, sufficient in most embedded projects.

Most notably, WiFi Pants can add WiFi to a Pi Zero while leaving the USB port free, and boosts any battery from as low as 3V to 5V at up to 2A to power the Pi and any other add-ons.

A JST-PH connector compatible with Sparkfun and Adafruit battery packs is included with the board. An undervoltage lock-out prevents batteries from draining below 2.7V. A soft power switch input lets a microcontroller or switch easily turn off or on the power supply.

Along with the soft power switch input, the 5 pin header exposes the Raspberry Pi's serial console, great for IoT projects where there is no screen but shell access is needed for setup. The header fits the 6 pin FTDI USB-to-UART cable.

WiFi Pants also works great with the Pi A+, B+, and 2 models.