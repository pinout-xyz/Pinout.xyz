<!--
---
description: eine "Alles-in-Einem" Licht, Ton, Ein- und Ausgabe Erweiterungsplatine.
-->
# Pibrella

Die "Alles-in-Einem" Licht, Ton, Ein- und Ausgabe Erweiterungsplatine von Pimoroni vs Cyntech 
benutzt jede Menge I/O Anschlüsse des Pi aber lässt die serielle Schnittstelle und den I2C-Bus noch frei und somit viel Raum für creative Erweiterungen!

Pibrella is einfach zu benutzen - einfach das entsprechende Modul über die Kommandozeile installieren:

```bash
sudo apt-get install python-pip
sudo pip install pibrella
```

... dann die Library in Dein Python-Skript importieren und anfangen zu basteln:

```bash
import pibrella
pibrella.light.red.on()
```