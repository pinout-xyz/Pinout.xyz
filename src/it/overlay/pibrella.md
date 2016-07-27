<!--
---
name: Pibrella
class: board
type: tutti
manufacturer: Pimoroni Vs Cyntech
url: https://github.com/pimoroni/pibrella
description: Una scheda all-in-one per luci, suoni, input ed output.
pincount: 26
pin:
  '7':
    name: LED verde
    direction: output
    active: high
  '11':
    name: LED giallo
    direction: output
    active: high
  '12':
    name: Buzzer - cicalino
    direction: output
    active: high
  '13':
    name: LED rosso
    direction: output
    active: high
  '15':
    name: Output A
    direction: output
    active: high
  '16':
    name: Output B
    direction: output
    active: high
  '18':
    name: Output C
    direction: output
    active: high
  '19':
    name: Input D
    direction: output
    active: high
  '21':
    name: Input A
    direction: input
    active: high
  '22':
    name: Output D
    direction: output
    active: high
  '23':
    name: Button
    direction: input
    active: high
  '24':
    name: Input C
    direction: input
    active: high
  '26':
    name: Input B
    direction: input
    active: high
-->
#Pibrella

La scheda all-in-one per luci, suoni, input ed output di Pimoroni vs Cyntech utilizza molti dei pin IO 
del Raspberry, ma la seriale e l'I2C restano liberi, lasciando molto spazio alla creatività.

Pibrella è facile da usare; innanzitutto devi installare il modulo usando un terminale (LXTerminal):

```bash
curl -sS get.pimoroni.com/pibrella | bash
```

E poi lo importi nel tuo script Python per smanettare:

```bash
import pibrella
pibrella.light.red.on()
```