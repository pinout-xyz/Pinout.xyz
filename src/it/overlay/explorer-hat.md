<!--
---
description: All-in-one luce, input, touch e add-on output board.
i2c:
  '0x28':
    name: Touch capacitivo
-->
# Explorer HAT

Input ed output a 5V, touch pad, LED sono le caratteristiche dell'Explorer HAT Pro--un asso nella manica per il tuo Raspberry Pi.

Per preparare e impostare il modulo puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Importalo poi nel tuo script Python e inizia a smanettare:

```bash
import explorerhat
explorerhat.light.on()
```
