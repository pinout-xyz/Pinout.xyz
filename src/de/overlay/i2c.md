<!--
---
description: Raspberry Pi I2C Anschlüsse
-->
# I2C - Inter Integrated Circuit

Der I2C-Bus des Raspberry Pi ist sehr praktisch um mit vielen unterschiedlichen Bausteinen
zu kommunizieren - egal ob z.B. ein MCP23017 als digitale I/O-Erweiterung oder sogar ein ATmega. 

Die Adresse eines angeschlossenen I2C-Bausteins kann mit einem einfachen Einzeiler überprüft werden:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

GPIO0 und GPIO1 - I2C0 - können als alternativer I2C bus verwendet werden, typischerweise sind diese in Verwendung um das EEPROM von Hats zu lesen.
