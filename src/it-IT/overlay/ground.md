<!--
---
name: Ground
description: Pin a massa del Raspberry Pi
pin:
  '6':
  '9':
  '14':
  '20':
  '25':
  '30':
  '34':
  '39':
-->
#Massa

I pin a massa sul Raspberry Pi sono tutti collegati, quindi non importa quale colleghi nel fornire 
la tensione di alimentazione.

Quello che è più conveniente da raggiungere o più vicino alle tue connessioni è in generale la soluzione
più pulita; in alternativa puoi usare uno vicino al pin di alimentazione che usi.

È una buona idea utilizzare il pin fisico 17 per la 3v3 e il pin 25 per la massa quando usi le connessioni 
[SPI](/pinout/spi), per esempio, dal momento che sono vicini ai pin più importanti per l'SPI0.
