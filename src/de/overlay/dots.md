<!--
---
name: Raspberry Pi Dots
description: verbinde die Punkte um eine Schaltung zu erstellen
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
formfactor: '40-way'
pincount: 40
pin:
  bcm0:
    name: 'Farbe: Blau'
    direction: input
  bcm1:
    name: Dot 7
    direction: input
  bcm2:
    name: Dot 22
    direction: input
  bcm3:
    name: Dot 21
    direction: input
  bcm4:
    name: Dot 2
    direction: input
  bcm5:
    name: Dot 9
    direction: input
  bcm6:
    name: Dot 14
    direction: input
  bcm7:
    name: Dot 6
    direction: input
  bcm8:
    name: Dot 18
    direction: input
  bcm9:
    name: Dot 17
    direction: input
  bcm10:
    name: 'Farbe: Grün'
    direction: input
  bcm11:
    name: Dot 8
    direction: input
  bcm12:
    name: Dot 10
    direction: input
  bcm13:
    name: Cloud
    direction: input
  bcm14:
    name: Dot 1
    direction: input
  bcm15:
    name: Dot 3
    direction: input
  bcm16:
    name: Dot 13
    direction: input
  bcm17:
    name: Dot 4
    direction: input
  bcm18:
    name: Dot 20
    direction: input
  bcm19:
    name: 'Farbe: Orange'
    direction: input
  bcm20:
    name: Bear
    direction: input
  bcm21:
    name: Dot 12
    direction: input
  bcm22:
    name: Dot 15
    direction: input
  bcm23:
    name: Dot 16
    direction: input
  bcm24:
    name: Dot 19
    direction: input
  bcm25:
    name: Dot 5
    direction: input
  bcm26:
    name: Dot 11
    direction: input
  bcm27:
    name: 'Farbe: Rot'
    direction: input
-->
#Raspberry Pi Dots

###Dots ist eine verbinde die Punkte HAT Platine für den Raspberry Pi, auf dem Du Punkte mit leitender Farbe verbindest!

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