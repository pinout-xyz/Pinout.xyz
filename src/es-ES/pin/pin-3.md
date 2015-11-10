SDA es uno de los pines i2c en la Pi, [aprende más sobre i2c](/pinout/i2c).

Es fácil escribir un HIGH (encendido) o LOW (apagado) digital a un pin del GPIO, pero debes recordar algunas cosas:

* Ejecuta tus programas como root
* Ajusta el modo de los pines a OUTPUT (1)

Asumiendo que has instalado WiringPi2-Python ( pip install wiringpi2 ) prueba a pegar lo siguiente en un archivo .py:

```python
import wiringpi2 as wiringpi
HIGH = 1
LOW = 0
OUTPUT = 1
INPUT = 0
wiringpi.wiringPiSetup()
wiringpi.pinMode(8,OUTPUT)
wiringpi.digitalWrite(8,HIGH)
```

Ejecútalo con:

```bash
sudo python myscript.py
```
