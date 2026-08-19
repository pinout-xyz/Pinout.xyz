<!--
---
description: Un chapeau multi-usage avec entrées et sorties 5V
pin:
  '15':
    name: Entrée 2
  '16':
    name: Entrée 1
  '18':
    name: Entrée 3
  '22':
    name: Entrée 4
  '31':
    name: Sortie 1
  '32':
    name: Sortie 2
  '33':
    name: Sortie 3
  '36':
    name: Sortie 4
i2c:
  '0x28':
    name: Capteur tactile
-->
# Explorer HAT

L'Explorer HAT est un chapeau multi-usage avec entrées et sorties en 5V, LED et touches tactiles. Une extension utile pour tout prototype!

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import explorerhat
explorerhat.light.on()
```
