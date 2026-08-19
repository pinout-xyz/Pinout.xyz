# PiJack

La forma más sencilla de añadir Ethernet a Raspberry Pi Zero. Simplemente conecta PiJack a tu Pi y arranca la última versión de Raspbian. PiJack será detectada a nivel del kernel Linux, cargando el controlador correcto y la interfaz Ethernet estará lista para uso.

Por defecto, Raspbian configura la interfaz para DHCP así que en cuento conectes PiJack tendrás acceso a la red.

Cada placa PiJack se programa con una dirección MAC única, que se mantiene a cada arranque. Esto permite configurar tu router para que asigne la misma IP siempre.

Debido a que el controlador está siendo mejorado, lo mejor es usar la última versión de Raspbian bien grabando una microSD nueva o ejecutando:

```bash
sudo apt-get update
sudo apt-get dist-upgrade
```
