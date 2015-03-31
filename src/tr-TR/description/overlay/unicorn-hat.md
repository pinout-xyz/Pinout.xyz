#Unicorn HAT

64 adet parlak LEDe sahip bu HAT kart'ı bir C kütüphanesi ile çok hızlı çalışacak bir şekilde yönetebilir, LEDlerin daha parlak veya sönük yanmasını sağlayabilirsiniz.

Not: Unicorn HAT bazı PWM kurnazlıkları kullanmakta. Bunun içnde analog ses çıkışından Raspberry Pi'nin ses çıkartmasını sağlayan şeyler de olduğundan ikisini aynı anda kullanamazsınız!

Kurulumu çok basit, sadece aşağıdaki komutu çalıştırın:

```bash
curl get.pimoroni.com/unicornhat | bash
```

Ardından Python scriptinize modülü ekleyip kurcalamaya başlayabilirsiniz:

```bash
import unicornhat
unicornhat.set_pixel(0, 0, 255, 255, 255)
unicornhat.show()
```