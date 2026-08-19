# Pi-LITE-r

Pi-LITE-r es una placa adicional completa para Raspberry Pi. Cuenta con 8 LEDs blanco ultra-brillantes y se conecta directamente a los GPIO. Puede utilizarse en proyectos I/O para dar información del estado. Iluminar los 8 LEDs consume poca corriente, menos que un sólo LED (20 mA nominales, 14.4 mA para Pi-LITE-r)

Aplicaciones:

* Monitor de estado I/O
* Gráficos de barras
* Control de luz
* Indicador de actividad
* Efectos de luz

```python
from gpiozero import PiLiter
from time import sleep

lite = PiLiter()

for led in lite:
    led.on()
    sleep(0.1)
    led.off()

lite.on()
sleep(5)
```
