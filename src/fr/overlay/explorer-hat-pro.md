<!--
---
description: Un chapeau multi-usage avec entrées analogiques et contrôle moteurs
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
  '35':
    name: Moteur 1 +
  '36':
    name: Sortie 4
  '37':
    name: Moteur 2 -
  '38':
    name: Moteur 1 -
  '40':
    name: Moteur 2 +
i2c:
  '0x28':
    name: Capteur tactile
  '0x48':
    name: Entrées analogiques
-->
# Explorer HAT Pro

L'Explorer HAT pro est un chapeau à usage multiple avec entrées et sorties en 5V, entrées analogiques et contrôle moteurs. Tout cela agrémenté de LED et touches tactiles. C'est donc d'un véritable couteau Suisse dont il s'agit!

Pour l'installation et mise en route exécutez simplement les commandes ci-dessous et suivez les instructions présentées à l'écran:

```bash
curl -sS https://get.pimoroni.com/explorerhat | bash
```

Puis, sous Python, en guise de test que tout fonctionne bien:

```bash
import explorerhat
explorerhat.light.on()
```
