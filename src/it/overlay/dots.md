<!--
---
name: Raspberry Pi Dots
class: board
type: Tutti
formfactor: Altro
manufacturer: Raspberry Pi
image: 'image.png'
description: Unisci i puntini e crea un circuito
url: http://www.raspberrypi.org/dots/
github: https://github.com/raspberrypilearning/dots
pincount: 40
pin:
  bcm0:
    name: 'Colore: Blu'
    direction: input
  bcm1:
    name: Puntino 7
    direction: input
  bcm2:
    name: Puntino 22
    direction: input
  bcm3:
    name: Puntino 21
    direction: input
  bcm4:
    name: Puntino 2
    direction: input
  bcm5:
    name: Puntino 9
    direction: input
  bcm6:
    name: Puntino 14
    direction: input
  bcm7:
    name: Puntino 6
    direction: input
  bcm8:
    name: Puntino 18
    direction: input
  bcm9:
    name: Puntino 17
    direction: input
  bcm10:
    name: 'Colore: Verde'
    direction: input
  bcm11:
    name: Puntino 8
    direction: input
  bcm12:
    name: Puntino 10
    direction: input
  bcm13:
    name: Cloud
    direction: input
  bcm14:
    name: Puntino 1
    direction: input
  bcm15:
    name: Puntino 3
    direction: input
  bcm16:
    name: Puntino 13
    direction: input
  bcm17:
    name: Puntino 4
    direction: input
  bcm18:
    name: Puntino 20
    direction: input
  bcm19:
    name: 'Colore: Arancione'
    direction: input
  bcm20:
    name: Bear
    direction: input
  bcm21:
    name: Puntino 12
    direction: input
  bcm22:
    name: Puntino 15
    direction: input
  bcm23:
    name: Puntino 16
    direction: input
  bcm24:
    name: Puntino 19
    direction: input
  bcm25:
    name: Puntino 5
    direction: input
  bcm26:
    name: Puntino 11
    direction: input
  bcm27:
    name: 'Colore: Rosso'
    direction: input
-->
#Raspberry Pi Dots

###Dots è una scheda HAT punto-a-punto per il Raspberry Pi che ti permette di chiudere il circuito con la vernice conduttiva BARE!

Ogni puntino ("Dot") sulla scheda Dots è un contatto metallico temporaneo, in attesa di essere collegato con una pennellata di vernice.

Per leggere un Dot devi impostare il pin corrispondente come INPUT e assicurarti che sia impostato così:

```python
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM )
GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
state = GPIO.input(dot_pin)
```

È buona norma attivare il PULLUP soltanto quando vuoi leggere un Dot, quindi è preferibile utilizzare 
qualcosa del genere:

```python
def is_dot_connected(dot_pin):
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_UP)
    state = GPIO.input(dot_pin)
    GPIO.setup(dot_pin, GPIO.IN, GPIO.PUD_OFF)
    return state == 0
```