<!--
---
description: Raspberry Pi pin i2c
pin:
  '3':
    name: Dati
  '27':
    name: Dati EEPROM
  '28':
    name: Clock EEPROM
-->
# I2C - Inter Integrated Circuit

L'I2C del Raspberry è un modo estremamente utile per comunicare con molti tipi diversi di periferiche esterne, dall'expander digitale MCP23017, ad un ATmega collegato.

I pin I2C includono una resistenza pull-up da 1.8 KOhm a 3.3V, il che significa che non sono adatti ad un IO generico dove una resistenza pull-up non è richiesta.

Puoi controllare l'indirizzo delle periferiche I2C collegate con una singola riga di codice:

```bash
sudo apt-get install i2c-tools
sudo i2cdetect -y 1
```

