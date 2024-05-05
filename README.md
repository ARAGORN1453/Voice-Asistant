
# Lucy: Kişisel Asistanınız

Lucy, günlük görevlerinizi kolaylaştırmak için tasarlanmış bir kişisel asistan uygulamasıdır. Ses tanıma ve konuşma sentezi teknolojilerini kullanarak, kullanıcıların sesli komutlarla çeşitli işlemleri gerçekleştirmelerine olanak tanır.

## Özellikler

- **Sesli Komut Algılama**: Kullanıcıların sesli komutlarını algılar ve tanır.
- **Metinden Konuşmaya Dönüştürme**: Verilen metni Türkçe olarak sesli olarak okur.
- **Çeşitli Görevleri Yerine Getirme**: Not defteri, komut istemi, kamera gibi uygulamaları açabilir ve web tarayıcısında aramalar yapabilir.
- **Kullanıcıya Selamlama**: Günün saati ne olursa olsun kullanıcıya uygun bir selamlama ile karşılık verir.

## Nasıl Çalışır

1. **Sesli Komutları Dinleme**: `take_command` fonksiyonu, mikrofondan gelen sesi dinler ve Google'ın ses tanıma servisi ile metne dönüştürür.
2. **Görevleri Yerine Getirme**: Algılanan komutlara göre `if` koşulları içinde tanımlanan görevleri yerine getirir.
3. **Kullanıcıya Yanıt Verme**: `speak` fonksiyonu ile kullanıcıya sesli olarak yanıt verir.

## Kurulum

Bu uygulamayı kullanmak için gerekli kütüphaneleri yükleyin:

```bash
pip install pyttsx3 speech_recognition opencv-python requests wikipedia webbrowser gtts playsound

