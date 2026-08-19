<!--
---
description: Una scheda all-in-one per luci, suoni, input ed output.
pin:
  '7':
    name: LED verde
  '11':
    name: LED giallo
  '12':
    name: Buzzer - cicalino
  '13':
    name: LED rosso
-->
# Pibrella

La scheda all-in-one per luci, suoni, input ed output di Pimoroni vs Cyntech utilizza molti dei pin IO 
del Raspberry, ma la seriale e l'I2C restano liberi, lasciando molto spazio alla creatività.

Pibrella è facile da usare; innanzitutto devi installare il modulo usando un terminale (LXTerminal):

```bash
curl -sS https://get.pimoroni.com/pibrella | bash
```

E poi lo importi nel tuo script Python per smanettare:

```bash
import pibrella
pibrella.light.red.on()
```