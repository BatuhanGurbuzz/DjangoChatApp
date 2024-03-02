# WhatsApp Klonu Chat Uygulaması

Bu proje, web tabanlı bir chat uygulamasını geliştirmek için Python ve JavaScript teknolojilerini kullanan bir deneyimi temsil etmektedir. WhatsApp benzeri bu uygulama, Redix server ve Django üzerinde web soketleri kullanılarak geliştirilmiştir.

## Özellikler

- **Mesaj Geçmişi ve Veritabanı İşlemleri:** Redix server kullanılarak her iki kullanıcının mesaj geçmişi güvenli bir şekilde saklanır ve yönetilir.
- **Medya Dosyalarını İşleme:** JavaScript tarafında gelen mesajlar içindeki fotoğraf, video veya ses dosyalarını algılayarak işleme yeteneği.

- **Ses Kaydı Desteği:** Kullanıcılar ses kaydı atmak istediklerinde özel bir altyapı sayesinde ses dosyalarını kolayca gönderebilirler.

## Kurulum

1. Projeyi kopyalayın:

```bash
git clone https://github.com/sizin-kullanici-adi/whatsapp-klonu.git
cd whatsapp-klonu
```

2. Virtual environment oluşturun ve bağımlılıkları yükleyin:
```bash
python -m venv venv
source venv/bin/activate   # veya 'venv\Scripts\activate' Windows için
pip install -r requirements.txt
```

3. Django migrasyonları uygulayın:
```bash
python manage.py migrate
```

4. Redix server'ı başlatın::
```bash
redis-server
```

5. Django development server'ı başlatın:
```bash
python manage.py runserver
```

## Kullanım
1. Tarayıcınızdan http://localhost:8000 adresine gidin.
2. Chat uygulamasını kullanmaya başlayın.
3. Fotoğraf, video veya ses dosyaları göndererek ve ses kaydı yaparak uygulamanın özelliklerini keşfedin.

## Katkıda bulunma

### Eğer projeye katkıda bulunmak istiyorsanız, lütfen bir konu açın veya bir çekme isteği gönderin. Katkılarınızı bekliyoruz!

