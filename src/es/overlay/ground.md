<!--
---
name: Tierra
class: interface
type: pinout
description: Pines de tierra de Raspberry Pi
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
#Tierra

Los pines de Tierra en la Raspberry Pi están todos electrónicamente conectados, así que 
no importa cual uses si estás conectando una fuente de alimentación

Generalmente, usar aquel más cómodo o cercano al resto de tus conexiones hace que sea más
ordenado y fácil, o alternativamente, aquel más cercano al pin de alimentación que uses.

Es una buena idea usar el Pin Físico 17 para 3v3, y el Pin Físico 25 para tierra cuando uses
algún tipo de dispositivo [SPI](/pinout/spi), por ejemplo, ya que estos están justo al lado
de los pines importantes de SPI0.
