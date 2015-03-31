#Pinout Yardımcı Arayüzleri

Pinout yardımcısı spesifik bir kart için Raspberry Pi fonksiyonlarını tanımlar.

Bu yardımcı arayüzler bir JSON dosyasından oluşmakta, ve de opsiyonel olarak gelişmiş uzun açıklamasını bir markdown dosyası ile tanımlayabilmekte.

##JSON Biçimi

The JSON arayüz dosyası isim, üretici linki, ürün linki, açıklama, ve de kartın kullandığı "pin"leri barındıran bir array (dizi) barındırmalıdır.

Eğer kart için isimde, description/overlay klasöründe aynı isimde bir .md dosyası varsa uzun açıklama için bu dosya kullanılacak.

Pin dizisi her bir pin için *fiziksel* konumunu barındırmalıdır, ve de en azından fonksiyonunu barındıran bir "name" (isim) bulundurmalıdır.

Opsiyonel olarak, her bir pin için "mode" isminde bir flah ile "input" veya "output" değerini vererek pinin giriş veya çıkış pini olduğunu da tanıtabilirsiniz.

Ayrıca, bir pine "active" değeri tanıyarak standart hali ile "low" veya "high" olduğunu belirtebilirsiniz.

Eğer kartınızda I2C ve/veya SPI pinleri de bulunuyorsa, bunları da belirtmelisiniz. Fakat spesifik olarak "input" veya "output" olarak belirtmediyseniz diğer kartlarla ortak olarak da kullanılabilir olarak tanımlanacaktırlar.

Örnek:

```json
{
	"name": "Örnek Kart",
	"manufacturer": "Arda Kılıçdağı",
	"url": "https://github.com/Ardakilic/Pinout2",
	"description": "Arda Kılıçdağı'nın örnek kartı.",
	"pin": {
		"7": {
			"name": "Yeşil LED"
		},
		"11": {
			"name": "Sarı LED"
		}
	}
}
```
