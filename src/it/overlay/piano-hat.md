<!--
---
description: Un piccolo Pi-piano con 16 tasti touch
pin:
  '7':
    name: Allarme A
  '13':
    name: Allarme B
i2c:
  '0x28':
    name: Touch capacitivo A
  '0x2b':
    name: Touch capacitivo B
-->
# Piano HAT

Il Piano HAT ha 16 tasti touch, 13 di questi sono singole ottave, gli altri ti danno 
le ottave superiori e inferiori e la selezione dello strumento.

Utilizza due Microchip CAP1188 con indirizzi i2c 0x28 e 0x2b.

Per preparare e impostare l'HAT puoi utilizzare l'installer fornito:

```bash
curl -sS https://get.pimoroni.com/pianohat | bash
```

&hellip;e seguire le istruzioni!
