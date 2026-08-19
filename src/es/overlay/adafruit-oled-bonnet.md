

# OLED Bonnet

El bonnet OLED es una simple pantalla de 128x64 para Raspberry Pi con un joystick de 5 direcciones y 2 botones.

La pantalla de 1.3"  está formada por pixels OLED blancos individuales, creando su propia luz por lo que no necesita iluminación trasera. Esto reduce la cantidad de energía necesaria y le da un alto contraste.

Para instalar usa los siguientes comandos:

```bash
sudo apt-get install git python-imaging python-smbus
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
