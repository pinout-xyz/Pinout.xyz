# RGB Matrix Bonnet

Este HAT se conecta a tu Pi y hace muy sencillo controlar matrices RGB, como las que ves en Times Square, permitiendo crear una pantalla en movimiento llena de color o un mini muro LED.

* Se necesita una fuente de 5V para alimentar la matriz.
* Para calcular la corriente máxima, multiplica el ancho de la matriz encendida por 0.12. Una matriz de 32 pixel necesita 32-0.12 = 3.85A así que elige una fuente de 5V y 4A.
* Este HAT sólo se puede utilizar con matrices tipo HUB75 RGB. No se puede usar con NeoPixel, DotStar u otras matrices de LEDs direccionables.

Especificaciones:

* Diseño simple. Conecta la corriente, el cable IDC y programa.
* Circuito de protección de corriente. Puedes conectar una fuente de 5V 4A y el HAT se protegerá ante sobre o bajo voltajes.
* Convertidores de nivel en la placa. Estos convierten los 3.3V de Raspberry Pi a 5.0V para funcionar con menos fallos.

Es compatible con cualquier Pi con el conector de 2x20.

Para instalar:

```bash
curl -O https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/master/rgb-matrix.sh
sudo bash rgb-matrix.sh
```
