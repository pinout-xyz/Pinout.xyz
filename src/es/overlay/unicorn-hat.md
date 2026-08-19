<!--
---
description: 64 LEDs RGB cegadores en un único HAT
pin:
  '12':
    name: Datos
-->
# Unicorn HAT

64 LEDs RGB cegadores contenidos en un HAT y controlados con una ultrarrápida librería escrita en C, controlable
desde Python, hacen al Unicorn HAT el hermano mayor del PiGlow.

Nota: El Unicorn HAT utiliza trucos especiales con el PWM, ejecutados con el mismo hardware que le permite a tu Pi
producir sonido a través del jack de audio ( audio analógico ), así que no puedes usar ambos al mismo tiempo.

La instalación es fácil, únicamente:

```bash
curl -sS https://get.pimoroni.com/unicornhat | bash
```
Después importa el módulo en tu programa de Python y empieza a experimentar:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
