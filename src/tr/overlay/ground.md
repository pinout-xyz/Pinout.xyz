<!--
---
name: Toprak
class: interface
type: pinout
description: Raspberry Pi Toprak Pinleri
pin:
  '6': {}
  '9': {}
  '14': {}
  '20': {}
  '25': {}
  '30': {}
  '34': {}
  '39': {}
-->
#Toprak

Raspberry Pi'deki GND pinlerinin hepsi birbiri ile bağlantılıdır, bu yüzden hangi pine toprağı verdiğinizin bir önemi yok.

Genel olarak devrenizin duruşuna en yakın toprak pinini seçmeniz devrenizin daha derli ve düzenlenebilir olmasını sağlayacaktır. Toprak için alternatif olarak elektrik akımına yakın olan pini de seçebilirsiniz.

Eğer [SPI](/pinout/spi) bağlantılarını kullanıyorsanız 3v3 için Fiziksel pin 17'yi ve de toprak için Fiziksel pin 25'i kullanmanız bu pinlerin SPI0 için önemli olan pinlerin yanında olması sebebi ile iyi bir seçim olacaktır.