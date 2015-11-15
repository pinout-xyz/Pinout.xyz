<!--
---
name: WiringPi GPIO Pinout
page_url: wiringpi
github: https://github.com/WiringPi/WiringPi2-Python
url: http://wiringpi.com
pin:
  '3':
    name: WiringPi 8
  '5':
    name: WiringPi 9
  '7':
    name: WiringPi 7
  '8':
    name: WiringPi 15
  '10':
    name: WiringPi 16
  '11':
    name: WiringPi 0
  '12':
    name: WiringPi 1
  '13':
    name: WiringPi 2
  '15':
    name: WiringPi 3
  '16':
    name: WiringPi 4
  '18':
    name: WiringPi 5
  '19':
    name: WiringPi 12
  '21':
    name: WiringPi 13
  '22':
    name: WiringPi 6
  '23':
    name: WiringPi 14
  '24':
    name: WiringPi 10
  '26':
    name: WiringPi 11
  '29':
    name: WiringPi 21
  '31':
    name: WiringPi 22
  '32':
    name: WiringPi 26
  '33':
    name: WiringPi 23
  '35':
    name: WiringPi 24
  '36':
    name: WiringPi 27
  '37':
    name: WiringPi 25
  '38':
    name: WiringPi 28
  '40':
    name: WiringPi 29
-->
#Raspberry Pi WiringPi

###WiringPi is an attempt to bring Arduino-wiring-like simplicity to the Raspberry Pi.

The goal is to have a single common platform and set of functions for accessing the Raspberry Pi GPIO across multiple languages. WiringPi is a C library at heart, but it's available to both Ruby and Python users who can "gem install wiringpi" or "pip install wiringpi2" respectively.

Python users note the 2 on the end, the WiringPi2-Python library finally brings a whole host of existing WiringPi functionality to Python including brand new features from WiringPi 2.

For more information about WiringPi you should visit the official WiringPi website.

##Getting started with WiringPi

WiringPi uses its own pin numbering scheme, here you'll learn how WiringPi numbers your GPIO pins, what those pins do and how to do shiny things with them from within Python or Ruby.

WiringPi, the Arduino-like GPIO library for the Pi, is available in C right from Gordon's git repository, Python, Ruby and even Perl and PHP to a lesser extent.

Installing to Python couldn't be easier, just:

```bash
sudo pip install wiringpi2
```

Note the 2 on the end? That's the all new, shinier WiringPi!