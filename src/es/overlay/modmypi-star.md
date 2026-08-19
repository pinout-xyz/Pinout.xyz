<!--
---
description: Una placa LED en forma de estrella para Raspberry Pi que sirve como punta del árbol de Navidad.
-->
# Christmas Tree Star

La ModMy Pi Christmas Tree Star es una placa LED para Raspberry Pi diseñada para colocarse en la copa de tu árbol de Navidad. Tiene 30 LED blancos controlables mediante una biblioteca de Python que extiende GPIO Zero y está disponible en GitHub.

## Características
- 30 LED blancos
- Biblioteca compatible con GPIO Zero.
- Puntos de montaje para Raspberry Pi Zero.
- [Guía de montaje del árbol de Navidad](https://www.modmypi.com/blog/christmas-tree-star-guide)

## Código de ejemplo
```
from star import Star
from time import sleep

# Inicializa la estrella
star = Star()

# Enciende y apaga la estrella.
star.on()
sleep(1)
star.off()

# Enciende y apaga los LED exteriores e interiores.
star.outer.on()
sleep(1)
star.off()
star.inner.on()
sleep(1)
star.off()

# Enciende LED individuales del anillo exterior.
star.outer.A.on()
star.outer.F.on()
star.outer.P.on()
star.outer.X.on()
sleep(1)
star.off()
```
