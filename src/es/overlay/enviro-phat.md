# Enviro pHAT

Junto con una Pi Zero, Enviro pHAT es un conjunto de sensores asequible, ideal para monitorizar habitáculos de servidores, habitaciones o cualquier cosa que quieras observar. Además incluye una entrada ADC de 4-canales para añadir sensores. Funciona con cualquiera de las versiones de Raspberry Pi de 40 pines - 3/2/B+/A+/Zero.

Especificaciones:

Sensor de temperatura/presión BMP280 (0x77 en el bus i2c)
Sensor de luz y color RGB TCS3472 (0x29 en el bus i2c)
(con dos LEDs para iluminación)
Sensor acelerómetro/magnetómetro LSM303D (0x1d en el bus i2c)
ADC de 12-bit, 4-canales y 3.3v ADS1015 (0x48 en el bus i2c)

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/envirophat | bash
```
Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
from envirophat import light, motion, weather, analog, leds
```
