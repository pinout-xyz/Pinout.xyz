<!--
---
description: Raspberry Pi SPI pinleri
-->
# SPI - Serial Peripheral Interface

### four-wire serial bus olarak da bilinen SPI, bir pin setinden birden fazla adresteki birden fazla uygun cihazı [papatya zinciri](https://tr.wikipedia.org/wiki/Papatya_zinciri) yapıp yönetmenizi sağlar.

SPI portunuz ayrıca Gordon Henderson'un modifiye AVRDude'una Arduino skeçleri yükleyerek ATmega 328'ye "[bit banging](http://en.wikipedia.org/wiki/Bit_banging)" de yapabilirsiniz.

Raspberry Pi'nizin SPI port'unu ATmega'nıza bağlayın ve ATmega'yı Raspberry Pi'nin 3.3v gücüyle besleyip açın. SPI sürücüleri çalıştırmadığınızdan emin olduktan sonra "`avrdude -p m328p -c gpio`" komutu ile bağlantıyı kontrol edin.

ATmega'nız varsa her bir pin için ayrı ayrı tıklayarak nasıl bağlayabileceğinizi öğrenebilirsiniz.
