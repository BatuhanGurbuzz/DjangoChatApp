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

# EN

# WhatsApp Clone Chat Application

This project represents an experience of developing a web-based chat application using Python and JavaScript technologies. This WhatsApp-like application is built using Redix server and web sockets in Django.

## Features

- **Message History and Database Operations:** Utilizing Redix server, both users' message histories are securely stored and managed.
- **Media File Processing:** Capable of detecting and processing photo, video, or audio files within messages sent via JavaScript.

- **Voice Recording Support:** Users can easily send voice files through a specialized infrastructure when they wish to record a voice message.

## Installation

1. Clone the project:

```bash
git clone https://github.com/your-username/whatsapp-clone.git
cd whatsapp-clone
```

2. Create a virtual environment and install dependencies:
```bash
python -m venv venv
source venv/bin/activate   # or 'venv\Scripts\activate' for Windows
pip install -r requirements.txt
```

3. Apply Django migrations:
```bash
python manage.py migrate
```

4. Start the Redix server::
```bash
redis-server
```

5. Start the Django development server:
```bash
python manage.py runserver
```

## Usage

1. Open your browser and go to http://localhost:8000.
2. Start using the chat application.
3. Explore the application's features by sending photos, videos, or audio files and recording voice messages.

## Contributing

If you would like to contribute to the project, please open an issue or submit a pull request. Your contributions are welcome!
