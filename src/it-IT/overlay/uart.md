<!--
---
name: UART
description: Pin UART del Raspberry
pin:
  '8':
    name: TXD / Trasmissione
    direction: output
    active: high
  '10':
    name: RXD / Ricezione
    direction: input
    active: high
-->
#UART - Universal Asynchronous Receiver/Transmitter

###I due pin UART in WiringPi sono il 15 e il 16.

UART è una maniera facile e semplice per collegare un Arduino (o un ATmega bootloaded) con il tuo Raspberry. Devi, tuttavia, 
fare attenzione alla differenza di tensione tra le due periferiche: il Raspberry è a 3.3V, e l'Arduino invece a 5V. Se 
li colleghi rischi di evocare del magico fumo blu.

Personalmente preferisco costruire un circuito con un Arduino Bootloaded ATmega 328 su una breadboard con un regolatore di tensione 
per prendere la linea a 5V del Raspberry e convertirla in 3.3V. L'ATmega 328 sembra piuttosto soddisfatto di funzionare a 3.3V con un 
cristallo a 16Mhz, e così ottieni un clone di Arduino con una logica a 3.3V.

Se hai WiringPi2-Python installato, questo esempio in python apre l'UART del Raspberry a 9600baud e ci scrive 'ciao mondo!'

```python
import wiringpi2 as wiringpi
wiringpi.wiringPiSetup()
serial = wiringpi.serialOpen('/dev/ttyAMA0',9600)
wiringpi.serialPuts(serial,'ciao mondo!')
```