# PiGlow

PiGlow es una pequeña placa adicional para Raspberry Pi con 18 LEDs controlables individualmente.

La placa usa el chip de 8-bit y 18-canales PWM SN3218 para controlar los LEDs. La comunicación se realiza mediante I2C a través de los GPIO en el bus con dirección 0x54. Cada LED puede configurarse para un valor de PWM entre 0 y 255.

The board uses the SN3218 8-bit 18-channel PWM chip to drive surface mount LEDs. Communication is done via I2C over the GPIO header with a bus address of 0x54. Each LED can be set to a PWM value of between 0 and 255.

Para configurar el módulo  puedes utilizar el instalador online de una línea:

```bash
curl -sS https://get.pimoroni.com/piglow | bash
```

¡Y sigue las instrucciones!
