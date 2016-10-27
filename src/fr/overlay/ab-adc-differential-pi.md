<!--
---
name: ADC Differential Pi
class: board
type: a/n
formfactor: HAT
manufacturer: AB Electronics
description: 8 canaux Analogiques vers un convertisseur Digital
url: https://www.abelectronics.co.uk/p/65/ADC-Differential-Pi-Raspberry-Pi-Analogue-to-Digital-converter
github: https://github.com/abelectronicsuk
buy: https://www.abelectronics.co.uk/p/65/ADC-Differential-Pi-Raspberry-Pi-Analogue-to-Digital-converter
image: 'ab-adc-differential-pi.png'
pincount: 40
eeprom: no
power:
  '1':
  '2':
ground:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
i2c:
  '0x68':
    name: MCP3424
    device: MCP3424
  '0x69':
    name: MCP3424
    device: MCP3424
-->
#ADC Differential Pi

Le  **ADC Differential Pi** de **AB Electronics** est une carte chapeau de conversion sur 8 canaux 18 bit *Analogique vers Digital* conçu pour fonctionner avec le Raspberry Pi. Le  **ADC Differential Pi** est basé sur deux micro-puce de conversion **MCP3424 A/D** qui comportent chacun quatres entrées analogiques. La micro-puce **MCP3424** est un convertisseur *delta-sigma A/D* avec entrées différentielles à réduction de bruit.

##Caractéristiques

- 8 x Entrées 18-bit différentielles
- Controle via le port **I2C** du Raspberry Pi
- Superposez jusqu'à 4 cartes chapeau **ADC Differential Pi** sur le même Raspberry Pi
- Adresses **I2C** sélectionnable par cavaliers (8 choix)
- Port **I2C** 5V à mémoire tampon
- Basé sur le **MCP3424** de **Microchip Technologies Inc**
- Entrée à plage de tension de ±2.048V
- Tension de référence 2.048V embarquée (Précision ± 0.05%, Glissement: 15 ppm/°C)
- Amplificateur de Gain programmable embarqué (PGA): Gain de 1, 2, 4 ou 8
- Débit de données programmable:
    - 3.75 SPS (18 bits)
    - 15 SPS (16 bits)
    - 60 SPS (14 bits)
    - 240 SPS (12 bits)
- Convertion unique ou continue

Les librairies **Arduino**, **C**, **Node.js**, **Windows 10 IOT**, **Python 2** et **Python 3** sont disponibles sur GitHub.
