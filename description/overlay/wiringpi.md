#Raspberry Pi WiringPi

###WiringPi is an attempt to bring Arduino-wiring-like simplicity to the Raspberry Pi.

The goal is to have a single common platform and set of functions for accessing the Raspberry Pi GPIO across muliple languages. WiringPi is a C library at heart, but it's available to both Ruby and Python users who can "gem install wiringpi" or "pip install wiringpi2" respectively.

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
