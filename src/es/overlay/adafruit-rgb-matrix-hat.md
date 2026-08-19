# RGB Matrix HAT + RTC

Este HAT hace sencillo controlar matrices RGB como las que se ven en Times Square, permitiendo crear una pantalla en movimiento con color o un panel LED. Se necesita una fuente de alimentación de 5V, no incluida, para alimentar la matriz. Raspberry Pi no puede hacerlo al tratarse de grandes corrientes. Para calcular la máxima corriente de la matriz, multiplica la anchura de las matrices por 0.12. Una matriz de 32 píxeles necesita 32*0.12 = 3.85A así que escoge una fuente de alimentación de 5V y 4A. Este HAT es sólo para ser utilizado con las matrices HUB75 tipo RGB. No se puede utilizar con NeoPixel, DotStar u otros LEDs direccionables.

Características:

Diseño simple, conecta un par de cables y ¡ejecuta el código Python!
Circuito de protección ante sobrevoltajes o voltajes bajos, tu montaje no se destruirá por accidente.
Controladores integrados para convertir los 3.3V de Raspberry Pi en 5.0V y controlar la matriz de manera limpia.
El reloj de tiempo real DS1307 permite controlar el tiempo de Raspberry Pi incluso tras reiniciar o apagar, para mostrar la hora en la matriz.

Para instalar:

 ```bash
sudo apt-get update
sudo apt-get install python-dev python-imaging
wget https://github.com/adafruit/rpi-rgb-led-matrix/archive/master.zip
unzip master.zip
cd rpi-rgb-led-matrix-master/
make
 ```
