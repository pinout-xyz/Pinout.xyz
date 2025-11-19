<!--
---
name: PWM
class: interface
type: pinout
description: Raspberry Pi PWM Pins
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

Mit Pulse-width Modulation wird auf einem Output-Pin eine periodische
Rechteckspannung erzeugt. Diese wird typischerweise verwendet um eine LED zu
dimmen oder blinken zu lassen, die Hintergrundbeleuchtung eines Displays oder
die Geschwindigkeit eines Motors (z.B. eines Lüfters) zu steuern.

Die Output-Pins dienen nur als Kontrol-Signal und sind nicht geeignet einen
Motor zu treiben.

Der PWM Controller, der Pins auf dem Raspberry Pi Header steuern kann
(`pwm@7e20c000`) hat zwei voneinander unabhängige Kanäle. Der erste kann zu den
GPIOs 12 oder 18 geroutet werden, der zweite zu den GPIOs 13 oder 19.
