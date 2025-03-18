<!--
---
name: Massa
class: interface
type: pinout
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
# Massa

I pin a massa sul Raspberry Pi sono tutti collegati, quindi non importa quale colleghi nel fornire
la tensione di alimentazione.

In generale la soluzione più pulita è scegliere il più conveniente da raggiungere o il più vicino alle
tue connessioni; in alternativa puoi usarne uno vicino al pin di alimentazione che usi.

Di solito, è una buona idea utilizzare il pin fisico 17 per la 3v3 e il pin 25 per la massa, per esempio
quando usi le connessioni [SPI](/pinout/spi), dal momento che sono vicini ai pin più importanti per l'SPIO.
