# Pi Cap

Pi Cap añade botones capacitivos precisos, sensores de distancia y sonido de gran calidad a cualquier Raspberry Pi con un conector de 40 pines GPIO. Los 12 electrodos pueden ser conectados a cualquier cosa que conduzca electricidad para crear una interfaz táctil o de proximidad. Además, Pi Cap incluye un LED RGB programable y un botón multifunción.

El software de Pi Cap está en repositorio oficial de Raspbian, por lo tanto para instalarlo simplemente:

```bash
sudo apt-get update
sudo apt-get dist-upgrade
```

Reinicia la Raspberry Pi y:
```bash
sudo apt-get install picap
picap-setup
```

Pi Cap proporciona 7 pines digitales I/O, en el conector de 40 pines de Raspberry Pi. Los pines: 12, 13, 15, 16, 18, 22, 36.
El paquete de Pi Cap contiene muchos ejemplos de código escritos en: C++, Python y Node.js.
