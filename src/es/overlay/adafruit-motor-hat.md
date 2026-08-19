# DC & Stepper Motor HAT

Haz tus sueños de root realidad con el nuevo DC+Stepper Motor HAT de Adafruit. Es perfecto para cualquier proyecto que implique movimiento ya que permite controlar 4 motores DC o 2 paso a paso con un control completo de la velocidad PWM.

Como Raspberry Pi no tiene muchos pines PWM, se utiliza un controlador para la dirección y la velocidad, que funciona mediante I2C. Sólo necesita dos pines (SDA y SCL) para controlar múltiples motores y, al ser I2C, permite conectar más dispositivos a los mismos pines. de hecho, se podrían acoplar hasta 32 HATs como este para controlar 64 motores paso a paso o 128 DC (o una mezcla de ambos).

Especificaciones:

4 H-Bridge: el chipset TB6612 proporciona 1.2A por bridge, con protección térmica y diodos de protección.

Puede controlar motores de 4.5VDC a 13.5VDC.
Hasta 4 motores DC bidireccionales con selección de velocidad individual de 8-bit (márgen 0.5%)

Hasta dos motores paso a paso (unipolar o bipolar) con bobina única, doble, entrelazado o micro-paso.

Terminal de 2 pines protegido de polaridad y cable para conectar corriente externa de 5-12VDC.

Para instalar:

```bash
git clone https://github.com/adafruit/Adafruit-Motor-HAT-Python-Library.git
cd Adafruit-Motor-HAT-Python-Library
sudo apt-get install python-dev
sudo python setup.py install
```
