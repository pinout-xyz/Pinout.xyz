<!--
---
description: broches i2c de la Raspberry Pi
pin:
  '3':
    name: Données
  '5':
    name: Horloge
  '27':
    name: EEPROM Données
  '28':
    name: EEPROM Horloge
-->
# I2C (Inter Integrated Circuit)

I2C est un moyen très pratique pour communiquer avec de multiples périphériques, un MCP23017 IO expander digital, un microprocesseur ATmega connecté à la Raspberry Pi, etc.

Les broches i2c de la Raspi incorporent une résistance de tirage fixée à 1.8 kohms qui maintient la ligne à 3.3 volts. En conséquence elles ne peuvent être utilisées en entrées/sorties pour les applications générales ne nécessitant pas de 'pull-up'. 

Pour vérifier la présence d'un périphérique sur le bus i2c, exécutez simplement les commandes suivantes:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

