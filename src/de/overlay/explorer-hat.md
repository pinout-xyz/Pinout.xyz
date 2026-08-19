<!--
---
description: Eine Platine mit LEDs, Ein- und Ausgängen, Sensor-Tasten und Steckbrett.
-->
# Explorer HAT und Explorer HAT Pro

Der Explorer HAT Pro besteht aus 5V Ein- und Ausgängen, Sensor-Tasten, LEDs, analogen Eingängen und einem H-Bridge Motor-Treiber. 
Perfekt für alle möglichen Ideen auf dem Raspberry Pi auszuprobieren.

```bash
sudo apt-get install python-pip
sudo pip install explorer-hat
```

Anschliessend die Libraries in Dein Python-Skript importieren und basteln:

```bash
import explorerhat
explorerhat.light.on()
```
