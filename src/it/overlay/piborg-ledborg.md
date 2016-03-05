<!--
---
name: PiBorg LEDBorg
manufacturer: PiBorg
description: Un singolo LED RBG per il tuo Raspberry Pi
url: https://www.piborg.org/ledborg-new/install
buy: https://www.piborg.org/ledborg
pincount: 26
pin:
  '11':
    name: LED rosso
    direction: output
    active: high
    description: PiBorg LED rosso
  '13':
    name: LED verde
    direction: input
    active: high
    description: PiBorg LED verde
  '15':
    name: LED blu
    direction: output
    active: high
    description: PiBorg LED blu
-->
###Il PiBorg LedBorg è un LED RGB ultra-luminoso per il Raspberry Pi.

PiBorg ha il suo driver, quindi non devi controllarlo manualmente.

Se vuoi una gamma di colori decisamente più ampia tuttavia, puoi controllarlo manualmente
usando softPwm su WiringPi. L'assegnazione dei pin è come segue:

* WiringPi pin 0: LED rosso
* WiringPi pin 2: LED verde
* WiringPi pin 3: LED blu

È facile usando WiringPi con Python:


```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(0,0,100)
wiringpi.softPwmCreate(2,0,100)
wiringpi.softPwmCreate(3,0,100)

# Viola!
wiringpi.softPwmWrite(3,100) # Blu al massimo
wiringpi.softPwmWrite(0,100) # Rosso al massimo
wiringpi.softPWMWrite(2,0)	 # Verde spento
```