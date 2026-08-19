# Unicorn pHAT

32 LEDs brillantes, cegadores, dentro de un pHAT controlado por una librería C ultrarápida con la que puedes comunicarte mediante Python hacen del Unicorn HAT el hermano mayor, más brillate de PiGlow.

Nota: Unicorn pHAT usa un truco PWM, la misma técnica que hace que tu Pi pueda reproducir sonido a través del jack de audio (sonido analógico) así que no se pueden usar a la vez.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/unicornhat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import unicornhat
unicornhat.set_layout(unicornhat.PHAT)
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```
