<!--
---
description: Unisci i puntini e crea un circuito
pin:
  bcm0:
    name: 'Colore: Blu'
  bcm1:
    name: Puntino 7
  bcm2:
    name: Puntino 22
  bcm3:
    name: Puntino 21
  bcm4:
    name: Puntino 2
  bcm5:
    name: Puntino 9
  bcm6:
    name: Puntino 14
  bcm7:
    name: Puntino 6
  bcm8:
    name: Puntino 18
  bcm9:
    name: Puntino 17
  bcm10:
    name: 'Colore: Verde'
  bcm11:
    name: Puntino 8
  bcm12:
    name: Puntino 10
  bcm14:
    name: Puntino 1
  bcm15:
    name: Puntino 3
  bcm16:
    name: Puntino 13
  bcm17:
    name: Puntino 4
  bcm18:
    name: Puntino 20
  bcm19:
    name: 'Colore: Arancione'
  bcm21:
    name: Puntino 12
  bcm22:
    name: Puntino 15
  bcm23:
    name: Puntino 16
  bcm24:
    name: Puntino 19
  bcm25:
    name: Puntino 5
  bcm26:
    name: Puntino 11
  bcm27:
    name: 'Colore: Rosso'
-->
# Raspberry Pi Dots

### Dots è una scheda HAT punto-a-punto per il Raspberry Pi che ti permette di chiudere il circuito con la vernice conduttiva BARE!

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