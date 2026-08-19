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
