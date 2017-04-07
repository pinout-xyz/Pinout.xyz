<!--
---
name: Zero LiPo
class: board
type: power
formfactor: Otro
manufacturer: Pimoroni
description: LiPo/LiIon power supply shim for Raspberry Pi
url: https://shop.pimoroni.com/products/zero-lipo
buy: https://shop.pimoroni.com/products/zero-lipo
image: 'zero-lipo.png'
pincount: 8
eeprom: no
power:
  '2':
ground:
  '6':
pin:
  '7':
    name: Battery Low
    mode: input
    active: high
-->
# Zero LiPo

El objetivo de Zero LiPo es ser la fuente de alimentación para Raspberry Pi más compacta.

Esta placa inclute LEDs indicadores de alimentación y bajo nivel de batería, además de un conector JST para conectar una batería LiPo, LiIon o cualquier otra batería compatible con JST. El convertidor TPS61232 step-up de Texas Instruments convierte el voltaje de 3-4.2V de entrada de las LiPo/LiIon en 5V, dando una alimentación de 5V estable perfecta para tu Pi.

```bash
curl https://get.pimoroni.com/zerolipo | bash
```

Especificaciones:

* PCB de 0.8 mm de grosor
* Perfil lo más bajo posible
* Conector JST de 2 polos, ideal para la mayoría de baterías LiPo/LiIon
* LEDs indicadores de alimentación y bajo nivel de batería
* Proporciona corriente continua de 1.5A
* Alerta de nivel bajo de batería a 3.4V (configura el GPIO #4 high)
* Apagado automático a 3.0V para proteger la batería
* Pines VBAT+, GND y EN accesibles
* Consumo de corriente en reposo de 15uA
