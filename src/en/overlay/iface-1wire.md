<!--
---
name: 1-WIRE
class: interface
type: pinout
description: Raspberry Pi One-Wire pins
url: https://www.raspberrypi.org/documentation/hardware/raspberrypi/dpi/
pin:
  'bcm4':
    name: Data
-->
# W1-GPIO - One-Wire Interface

To enable the one-wire interface you need to add the following line to /boot/config.txt, before rebooting your Pi:

```
dtoverlay=w1-gpio
```

Alternatively you can enable the one-wire interface on demand using:

```
sudo modprobe w1-gpio
```

once either of the steps above has been performed, you can list the devices your Raspberry Pi can probe via (by default) GPIO4, like so:

```
ls /sys/bus/w1/devices/
```
