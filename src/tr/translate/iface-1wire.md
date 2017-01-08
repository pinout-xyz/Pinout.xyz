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

To enable the one-wire interface you need to add the following line to /boot/config.txt, before rebooting your Pi:

```
dtoverlay=w1-gpio
```

or 

```
dtoverlay=w1-gpio,gpiopin=x
```

if you would like to use a custom pin (default is BCM4, as illustrated in pinout herein).

Alternatively you can enable the one-wire interface on demand using raspi-config, or the following:

```
sudo modprobe w1-gpio
```

once either of the steps above has been performed, you can list the devices your Raspberry Pi can probe via (by default) BCM4, like so:

```
ls /sys/bus/w1/devices/
```
