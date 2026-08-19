# Sense HAT

Sense HAT es una placa adicional para Raspberry Pi con una matriz led 8x8 RGB, un joystick de 5 botones y los siguientes sensores: giroscopio, acelerómetro, magnetómetro, temperatura, presión barométrica y humedad.

El controlador de la matriz LED es un LED2472G conectado mediante ATTINY88 y comunicándose mediante i2c en la dirección 0x46 con la Pi. El joystick multidireccional SKRHABE010 switch/joystick se controla de manera similar.

Los sensores también funcionan mediante el bus i2c:

Los IUM (giroscopio, acelerómetro y magnetómetro) a trabés de LSM9DS1 en las direcciones i2c 0x1c(0x1e),0x6a(0x6b), con interrupciones en el ATTINY88.

Los sensores medioambientales son un LPS25H presión+temperatura en la dirección 0x5c y un HTS221 humedad+temperatura en la dirección 0x5f del bus i2c.
