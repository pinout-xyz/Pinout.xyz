<!--
---
description: verbinde die Punkte um eine Schaltung zu erstellen
pin:
  bcm0:
    name: 'Farbe: Blau'
  bcm10:
    name: 'Farbe: Grün'
  bcm19:
    name: 'Farbe: Orange'
  bcm27:
    name: 'Farbe: Rot'
-->
# Raspberry Pi Dots

### Dots ist eine verbinde die Punkte HAT Platine für den Raspberry Pi, auf dem Du Punkte mit leitender Farbe verbindest!

Jeder Punkt auf der Dots-Platine ist ein offener Metallkontakt der darauf wartet mit der Farbe kontaktiert zu werden.


Um einen Punkt auszulesen setze den dazugehörigen Anschluss als Eingang und checke, ob der Kontakt hergestellt ist:


```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

Es ist gute Praxis den Eingang nur auf PULLUP zu schalten, wenn Du den Kontakt auch lesen möchtest.
Somit ist folgender Code empfohlen:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input( dot_pin )
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```