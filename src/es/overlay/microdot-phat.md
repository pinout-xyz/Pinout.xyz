# Micro Dot pHAT

Una placa con una matriz LED descarada, de vieja escuela, con hasta 30x7 pixels utilizando las matrices Lite-On LTP-305 (o cualquiera similar). Perfecta para construir un mensaje en movimiento retro, un pequeño analizador de espectro de 30 bandas o un reloj retro.

La placa utiliza tres chip IS31FL3730 para controlar la matriz, cada  uno controla dos matrices. La placa y el software fuero diseñados para trabajar de manera eficiente, actualizando realmente rápido.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/microdotphat | bash
```

Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import microdotphat
```
