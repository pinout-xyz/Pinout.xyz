<!--
---
description: All-in-one luce, input, motore, touch e add-on output board.
pin:
  '37':
    name: Motore 2 -
  '38':
    name: Motore 1 -
  '40':
    name: Motore 2 +
i2c:
  '0x28':
    name: Touch capacitivo
  '0x48':
    name: Input analogico
-->
# Explorer HAT Pro

Input ed output a 5V, touch pad, LED, input analogici e un motore H-Bridge sono le caratteristiche dell'Explorer HAT Pro--un asso nella manica per il tuo Raspberry Pi.

Per preparare e impostare il modulo puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Importalo poi nel tuo script Python e inizia a smanettare:

```bash
import explorerhat
explorerhat.light.on()
```
