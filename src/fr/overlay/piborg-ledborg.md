<!--
---
name: PiBorg LedBorg
description: une carte LED RGB pour la Raspberry Pi
pincount: 26
pin:
  '11':
    name: LED rouge
    direction: output
    active: high
    description: LED rouge de la PiBorg
  '13':
    name: LED verte
    direction: input
    active: high
    description: LED verte de la PiBorg
  '15':
    name: LED bleue
    direction: output
    active: high
    description: LED bleue de la PiBorg
-->
###La carte PiBorg LedBorg ajoute une LED tricolore RGB à votre Raspberry Pi.

La carte LedBorg prend en charge la gestion de la LED. Cependant, si vous désirez contrôler le gamut de couleurs de manière plus précise, vous pouvez vous tourner vers WiringPi et son softPwn.

Pour ce faire, sachez que les broches WiringPi concernées sont les suivantes:

WiringPi broche 0: LED rouge
WiringPi broche 2: LED verte
WiringPi broche 3: LED bleue

Voici un exemple WiringPi sous Python:

```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()

wiringpi.softPwmCreate(0,0,100)
wiringpi.softPwmCreate(2,0,100)
wiringpi.softPwmCreate(3,0,100)

# Pour du violet:
wiringpi.softPwmWrite(0,100) # max rouge
wiringpi.softPwmWrite(3,100) # max bleu
wiringpi.softPWMWrite(2,0)	 # pas de vert
```