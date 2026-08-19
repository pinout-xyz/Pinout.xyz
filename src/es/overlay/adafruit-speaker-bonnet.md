# Speaker Bonnet

El Speaker Bonnet (Gorro parlante) es un amplificador estéreo que se adapta al Raspberry Pi. Utiliza un bus I2S para mayor claridad en el sonido. Los datos digitales entran directo al amplificador por lo que no hay estática como con un enchufe de audífonos. Funciona con cualquier Raspberry Pi con conector 2x20 - A+, B+, Zero, Pi 2, Pi 3.

Una vez soldado, solo conecte un parlante entre 4Ω y 8Ω a los bloques terminal o unos parlantes Adafruit al conector JST.

Para instalar:

```bash
curl -sS https://raw.githubusercontent.com/adafruit/\
Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```
