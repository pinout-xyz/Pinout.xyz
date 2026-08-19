# Automation HAT

Automatian HAT es una placa adicional de domótica para Raspberry Pi; con relés, canales analógicos, salidas alimentadas y entradas regulables. Todos con tolerancia hasta 24V.

Para configurar el HAT puedes utilizar el instalador online de una línea.

```bash
curl -sS https://get.pimoroni.com/automationhat | bash
```

Después importalo en tu programa de Python y empieza a experimentar:

```bash
import automationhat
automationhat.relay.one.on()
```
