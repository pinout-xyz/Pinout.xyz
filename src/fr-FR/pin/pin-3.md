SDA est la broche fournissant le signal de données du bus i2c de la Raspberry Pi, [référence i2c](/pinout/i2c).

Conseil: Il est aisé de basculer une broche de l'état haut (HIGH) vers l'état bas (LOW), ou vice versa, mais prenez cependant quelques précautions:

* Exécutez vos scripts en invoquant l'utilisateur 'root' 
* n'oubliez pas de déclarer la broche en tant que sortie (OUTPUT, 1)

Par exemple, sous WiringPi2-Python ( pip install wiringpi2 ):

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

Puis:

```bash
sudo python myscript.py
```