<!--
---
description: Una placa Jam amigable con 6 LEDs, 2 botones y un zumbador.
-->
# Jam Hat

Una placa complementaria con LED, botón y zumbador para Raspberry Jams, Jam Makers y personas que están aprendiendo lo básico de GPIO.

La placa tiene 6 LEDs, 2 botones y un zumbador tonal que permiten un montón de experimentación hardware utilizando la biblioteca GPIO Zero para una sencillez de uso.
```
from gpiozero import JamHat
from time import sleep

jh = JamHat()

# Enciende la plaza, espera y apágala.
jh.on()
sleep(1)
jh.off()

# Reproduce tones mediante el zumbador.
jh.buzzer.play('C4')
sleep(0.5)
jh.buzzer.play('D4')
sleep(0.5)
jh.buzzer.play('E4')
sleep(0.5)
jh.off()

# Utiliza los botones para encender las luces.
jh.button_1.when_pressed = jh.lights_1.on
jh.button_1.when_released = jh.lights_1.off
jh.button_2.when_pressed = jh.lights_2.on
jh.button_2.when_released = jh.lights_2.off
```

Las guías completas de inicio están disponibles en [El sitio web de ModMyPi](https://www.modmypi.com/blog/getting-started-with-the-jamhat)
