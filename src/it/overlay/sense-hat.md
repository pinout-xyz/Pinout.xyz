<!--
---
name: "Sense HAT"
description: Scheda add-on che include una matrice 8×8 LED RBG, un joystick a 5 bottoni, un IMU e sensori ambientali
pincount: 40
pin:
  '3':
    mode: i2c
  '5':
    mode: i2c
  '16':
    name: Joystick
    mode: input
  '18':
    name: Joystick
    mode: input
  '19':
    mode: spi
  '21':
    mode: spi
  '22':
    name: Joystick
    mode: input
  '23':
    mode: spi
  '24':
    mode: spi
-->
#Sense HAT

Il Sense HAT è una scheda add-on per il Raspberry Pi che comprende una matrice 8×8 LED RGB, un joystick a 5 bottoni e i 
seguenti sensori:

Giroscopio, Accelerometro, Magnetometro, Temperatura, Pressione barometrica e Umidità.

Lo shift register che controlla la matrice LED è un LED2472G, collegato tramite un ATTINY88 al bus SPI del Raspberry. 
Il Joystick/Switch multidirezionale SKRHABE010 è anch'esso connesso al bus SPI.

Di per sé, i sensori operano (prevalentemente) sul bus I2C; gli IMU (Giroscopio, Accelerometro, Magnetometro) operano tramite un LSM9DS1 collocato all'indirizzo i2c 0x1c(0x1e), 0x6a(0x6b), con interrupts sul ATTINY88.

I sensori ambientali sono implementati da un sensore LPS25H (pressione e temperatura) all'indirizzo 0x5c e da un sensore HTS221 (umidità e temperatura) all'indirizzo 0x5f sul bus I2C.