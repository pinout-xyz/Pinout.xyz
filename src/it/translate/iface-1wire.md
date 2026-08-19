<!--
---
name: 1-WIRE
class: interface
type: pinout
description: Raspberry Pi One-Wire pins
url: https://www.kernel.org/doc/Documentation/w1/w1.generic
pin:
  'bcm4':
    name: Data
-->
# W1-GPIO - One-Wire Interface

To enable the one-wire interface you need to add the following line to /boot/firmware/config.txt, before rebooting your Pi:

```
dtoverlay=w1-gpio
```

or 

```
dtoverlay=w1-gpio,gpiopin=x
```

if you would like to use a custom pin (default is BCM4, as illustrated in pinout herein).

Alternatively you can enable the one-wire interface using raspi-config.

Newer kernels (4.9.28 and later) allow you to use dynamic overlay loading instead, including creating multiple 1-Wire buses to be used at the same time:

```
sudo dtoverlay w1-gpio gpiopin=4 pullup=0  # header pin 7
sudo dtoverlay w1-gpio gpiopin=17 pullup=0 # header pin 11
sudo dtoverlay w1-gpio gpiopin=27 pullup=0 # header pin 13
```

Devices found on any of the buses appear in `/sys/bus/w1/devices/`.

n.b. Using w1-gpio on the Raspberry Pi typically needs a 4.7 kΩ pull-up resistor connected between the GPIO pin and a 3.3v supply (e.g. header pin 1 or 17).  Other means of connecting 1-Wire devices to the Raspberry Pi are also possible, such as using i2c to 1-Wire bridge chips.
