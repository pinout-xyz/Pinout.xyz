#Pibrella

The all-in-one light, sound, input and output add-on board from Pimoroni vs Cyntech uses lots of IO on the Pi but leaves both Serial and I2C free leaving plenty of room for expansion if you get creative.

Pibrella is easy to use, first you should install the module using LXTerminal/Command Line:

```bash
sudo apt-get install python-pip
sudo pip install pibrella
```

Then import it into your Python script and start tinkering:

```bash
import pibrella
pibrella.light.red.on()
```
