#Raspberry Pi WiringPi

###WiringPi, Arduino benzeri bir kablolama basitliğini Raspberry Pi'ye getirmeyi amaçlayan bir projedir.

WiringPi, Arduino kullanmış olanların hiç yabancılık çekmeyeceği, Arduino benzeri bir pinleme/klablolama sistemini Raspberry Pi'ye getirmeyi amaçlamış üçüncü parti bir kütüphanedir. Bu kütüphanenin amacı benzer ve ortak bir platform oluşturmak, ve de Raspberry Pi GPIO pinlerini farklı diller ile yönetebilmektir. WiringPi özünde C dili ile yazılmıştır, fakat hem Ruby hem de Python türevleri mevcuttur. Bunları sıra ile Ruby için "gem install wiringpi" veya Python için "pip install wiringpi2" diyerek kurabilirsiniz.

Python kullanıcıları kütüphanenin adının sonundaki 2'ye dikkat etmiş olabilirler. Bu aslında WiringPi2-Python kütüphanesidir. Bu kütüphane sonunda mevcut WiringPi kütüğhanesindeki özellikleri ve esnekliği Raspberry Pi'ye Python dilinde getirmeyi başarmış bir kütüphanedir.

Daha fazla bilgi için [WiringPi resmi web sitesi](http://wiringpi.com/)ni ziyaret edebilirsiniz.

##WiringPi'ye başlangıç

WiringPi [kendi pin numaralama şematiğini kullanıyor](http://wiringpi.com/pins/). Bu linkten WiringPi'nin GPIO pinlerinizi nasıl numaralandırdığını görebilir, pinlerin ne yaptığını inceleyebilir, ve de C, Python veya Ruby dilleri ile GPIO programlamaya başlayabilir, devre elemanlarınızı yönetebilirsiniz.


Arduino benzeri GPIO kütüphanesi WiringPi, C dili için doğrudan [Gordon'un Git reposu](https://git.drogon.net/?p=wiringPi;a=summary)nda mevcuttur. Ayrıca Python, Ruby hatta Perl ve PHP için de daha kısıtlı da olsa desteği mevcuttur.

Python'a kurmak saniyelerinizi alacak:

```bash
sudo pip install wiringpi2
```

Sonundaki 2'yi fark ettiniz mi? İşte bu yeni, ve de daha modern WiringPi kütphanesi (WiringPi2)!
