# Blinkt!

Blinkt! es una placa adicional ultradelgada para Raspberry Pi con 8 LEDs APA-102.

Para configurar puedes utilizar el instalador online de una línea:

```bash
curl -sS https://get.pimoroni.com/blinkt | bash
```

```python
from blinkt import set_pixel, show
from random import randint
from time import sleep

while True:
    for pixel in range(8):
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        set_pixel(pixel, r, g, b)
        show()
        sleep(0.1)
```
