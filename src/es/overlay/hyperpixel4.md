# HyperPixel 4

HyperPixel 4 es una pantalla TFT de 4" para Raspberry Pi. Usa una interfaz DPI de alta velocidad que da lugar a una tasa de 60 FPS a una resolución de 270 píxeles por pulgada (800x480)

La pantalla es capaz de mostrar color de 18-bits (6 bits por color, modo DPI 6 - RGB666) y cuenta con capacidad multi-toque capacitiva, más sensible y con mejor respuesta que una pantalla resistiva.

HyperPixel 4 es compatible con cualquier version de Raspberry Pi de 40 pines, incluidas Pi Zero y Pi Zero W.

HyperPixel 4 es más grande que cualquier HAT estándar para que quepa la pantalla, por lo sobresaldrá por ambos lados de Raspberry Pi. Requiere una conector de extensión de GPIO (incluido) para conectarse.

Debido a que HyperPixel 4 utiliza todos los pines de Raspberry Pi es complicado utilizarlo con otros dispositivos, sin embargo permite utilizar el bus de software I2C (i2c 3) que puedes compartir con el controlador táctil de la pantalla.

Para configurar la pantalla puedes utilizar el instalador de una línea:

```bash
curl https://get.pimoroni.com/hyperpixel4 | bash
```

¡y sigue las instrucciones!
