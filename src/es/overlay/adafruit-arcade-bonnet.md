# Arcade Bonnet

Arcade Bonnet de Adafruit está diseñado para facilitar la construcción de pequeños emuladores. Estas son sus especificaciones:

Tiene una toma JST para conectar 6 botones de arcade fácilmente.

Permite utilizar distintos tipos de joysticks, tipo "clicky", analógicos o con potenciómetros.

Tiene una salida de altavoces de 3W para conectar altavoces de 4-8  ohm mientras se usa la salida de TV, HDMI o PiTFT.

Los pulsadores se manejan con el conversor I2C-GPIO, muy rápido y libera todos los pines para poder utilizar Arcade Bonnet con cualquier otro dispositivo que utilice muchos  pines.

Para instalar:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/arcade-bonnet.sh
sudo bash arcade-bonnet.sh
curl -sS https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/i2samp.sh | bash
```
