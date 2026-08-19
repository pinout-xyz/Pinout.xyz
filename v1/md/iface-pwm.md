<!--
---
name: PWM
class: interface
type: pinout
description: Raspberry Pi PWM pins
pin:
  '32':
    name: PWM0
  '33':
    name: PWM1
  '12':
    name: PWM0
  '35':
    name: PWM1
-->
# PWM - Pulse-width Modulation

Pulse-width modulation creates a rectangular wave signal that is commonly used
for dimming or blinking an LED, control a display backlight or the speed of a
motor (e.g. a fan).

Note that the outputs are only useful as control signals, not to actually drive
a motor.

The PWM controller that has outputs available on the Raspberry Pi header
(`pwm@7e20c000`) has two independent channels. The output of the first can be
routed to GPIO 12 or GPIO 18, the second's output to GPIO 13 or GPIO 19.

On Pi 5 the RP1 PWM block has four channels instead of two, one each on GPIO 12,
GPIO 13, GPIO 18 and GPIO 19.

## Enable via config.txt

`dtoverlay=pwm` sets up one channel and `dtoverlay=pwm-2chan` sets up both, on
GPIO 18 and GPIO 19 by default. The `pin` and `func` parameters move a channel to
another of its pins:

```
dtoverlay=pwm-2chan,pin=12,func=4,pin2=13,func2=4
```

`func` is the function number for the pin you pick: 4 for GPIO 12 and GPIO 13, 2
for GPIO 18 and GPIO 19. These are the numbers the older models use, and they
still work on Pi 5, where the RP1 GPIO driver maps each one to the closest
matching RP1 function. Overlays written before Pi 5 don't need a Pi 5 variant.

The onboard analogue audio output uses both channels, so it can't be used at the
same time as PWM. GPIO 18 and GPIO 19 are also the I2S clock and frame select,
which makes GPIO 12 and GPIO 13 the pair to use alongside an I2S audio HAT.

Pi 5 also has `dtoverlay=pwm-pio`, which drives a PWM signal from PIO on any pin
in bank 0 rather than from the PWM block.
