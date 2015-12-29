<!--
---
name: Skywriter HAT
description: Un sensore 3D posizionale per le dita.
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '11':
    name: Reset
  '13':
    name: Transfer
-->
#Skywriter HAT

Skywriter HAT percepisce la posizione del tuo dito in 3 dimensioni, e restituisce un asse in X, Y, Z
che puoi usare nei tuoi script Python.

È anche in grado di riconoscere gesti, come ad esempio swipe ("scorrimento"), e molti altri.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS get.pimoroni.com/skywriter | bash
```

&hellip;e seguire le istruzioni!
