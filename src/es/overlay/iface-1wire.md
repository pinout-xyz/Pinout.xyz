# W1-GPIO - One-Wire Interface

Para habilitar la interaz one-wire necesitas añadir la siguiente línea a /boot/firmware/config.txt y después reiniciar tu Pi:

```
dtoverlay=w1-gpio
```

Tras habilitar la interfaz, puedes enumerar los dispositivos conectados al BCM4 de tu Raspberry Pi (por defecto) con:

```
ls /sys/bus/w1/devices/
```
