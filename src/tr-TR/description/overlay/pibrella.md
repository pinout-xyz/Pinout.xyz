#Pibrella

Pibrella Pimoroni tarafından hazırlanmış hepsi-bir-arada, hafif, ses, giriş ve çıkış destekleyen bir eklenti kartı. Cyntech çok fazla IO pini kullanmakta, fakat hem Serial, hem de I2C pinleri boşta kalmakta. Bu sebeple eğer yaratıcı olursanız bu kartla birlikte eklenti kartları için pek çok yer kalmakta.

Pibrella'yı kullanmak çok kolay. Öncelikle terminalden aşağıdaki komutları çalıştırıp kurulumu gerçekleştirin:

```bash
sudo apt-get install python-pip
sudo pip install pibrella
```

Ardından Python kodunuzda aşağıdaki gibi modülü ekleyip kurcalamaya başlayabilirsiniz:

```bash
import pibrella
pibrella.light.red.on()
```
