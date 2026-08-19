# PiOLED

PiOLED es una pequeña pantalla OLED de 128x32 diseñada para colocarse en los seis primeros pines de Raspberry Pi. usa comunicación I2C por lo que quedan pines libres para botones, LEDs y sensores.

La pantalla OLED tiene un contraste muy alto por lo que da lugar a imágenes y texto nítidos, además al producir su propia luz consume muy poca energía.

La pantalla tiene una diagonal de 1" y se actualiza a 30FPS, permitiendo crear animaciones simples. Además, el chipset SSD1306 es fácil de controlar con un simple librería Python.

Para instalar usa los siguientes comandos:

```bash
sudo apt-get install git python-imaging python-smbus
git clone https://github.com/adafruit/Adafruit_Python_SSD1306
cd Adafruit_Python_SSD1306
sudo python setup.py install
```
