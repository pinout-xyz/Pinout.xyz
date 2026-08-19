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

One-wire is a single-wire communication bus typically used to connect sensors to the Pi.

The Raspberry Pi supports one-wire on any GPIO pin, but the default is GPIO 4.

## Enable via config.txt

Add the overlay to /boot/firmware/config.txt and reboot, or let `raspi-config` do it for you:

```
dtoverlay=w1-gpio
```

The default pin is GPIO 4. Any other pin needs the `gpiopin` parameter, for example `dtoverlay=w1-gpio,gpiopin=17`.

## Enable at runtime

Kernels since 4.9.28 can load overlays without a reboot, including several 1-Wire buses at once:

```
sudo dtoverlay w1-gpio gpiopin=4  # header pin 7
sudo dtoverlay w1-gpio gpiopin=17 # header pin 11
sudo dtoverlay w1-gpio gpiopin=27 # header pin 13
```

Devices found on any of the buses appear in `/sys/bus/w1/devices/`.

Using w1-gpio on the Raspberry Pi typically needs a 4.7 kΩ pull-up resistor connected between the GPIO pin and a 3.3v supply (e.g. header pin 1 or 17). [GPIO 2 and GPIO 3](/pinout/i2c) already have a 1.8 kΩ pull-up fitted, which will do the same job if you can spare the I2C pins. Other means of connecting 1-Wire devices to the Raspberry Pi are also possible, such as using i2c to 1-Wire bridge chips.
