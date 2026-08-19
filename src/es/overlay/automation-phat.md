# Automation pHAT

Automation pHAT sirva para monitorizar y domotizar el hogar con Raspberry Pi; cuenta con relés, canales analógicos, salidas con alimentación y entradas regulables. Todo capaz de funcionar con 24V.

Para configurar el pHAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/automationhat | bash
```
Luego impórtalo en tu script Python y empieza a realizar proyectos:

```bash
import automationhat
automationhat.relay.one.on()
```
