<!--
---
name: Arcade Bonnet
class: board
type: io
formfactor: pHAT
manufacturer: Adafruit
description: Connect joystick,buttons and speakers to your Pi
url: https://learn.adafruit.com/adafruit-arcade-bonnet-for-raspberry-pi
buy: https://www.adafruit.com/products/3422
image: adafruit-arcade-bonnet.png
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '30':
  '34':
  '39':
  '25':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '12':
    name: I2S Clk
  '35':
    name: I2S FS
  '40':
    name: I2S Dout
i2c:
  '0x26':
    name: MCP23017
    device: MCP23017   
-->
#Arcade Bonnet

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
