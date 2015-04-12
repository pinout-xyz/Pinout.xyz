#Explorer HAT ve Explorer HAT Pro

5V giriş ve çıkışları, dokunmatik paneli, LEDler, analog girişler ve bir H-Bridge motor ile Explorer HAT Pro, Raspberry Pi'de prototipleme için tam teşekkürlü bir araç olarak teşkil etmekte.

```bash
sudo apt-get install python-pip
sudo pip install explorer-hat
```

Ardından Python scriptinize aşağıdaki kodları ekleyip prototipinizi kurcalamaya başlayabilirsiniz:

```bash
import explorerhat
explorerhat.light.on()
```