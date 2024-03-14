# TR
##  WhatsApp Klonu Chat Uygulaması
Bu proje  **Python** ve **Javascript** teknolojileri kullanılarak geliştirilmiştir. Projenin ana amacı web socketler ile çalışma deneyimini kendime katabilmektir. 

### Proje özellikleri:
----
 1. Redix server kullanılmıştır.
 2. Mesaj geçmişi veritabanına kayıt edilerek kullanıcıların mesaj geçmişlerinin görüntülenmesi hedeflenmiştir.
 3. Kullanıcılar birbirilerine **resim**, **video** gibi medya dosyaları gönderebilir ve bunları görüntüleyebilirler.
 4. Ses kaydı göndermek isteyen kullanıcılar için oluşturulmuş olan alt yapı sayesinde kullanıcılar birbirlerine ses kaydı gönderebilirler.

### Kurulum
-------

 - Projeyi Kopyalayın:
	`git clone https://github.com/BatuhanGurbuzz/DjangoChatApp.git`
	
- Virtual environment oluşturun ve bağımlılıkları yükleyin(Opsiyoneldir):
	`python -m venv venv source venv/bin/activate veya  venv\Scripts\activate' Windows için pip install -r requirements.txt`
	
- Terminali açın, dosyanın bulunduğu dizine gidin django migrasyonları uygulayın:
	`python manage.py migrate veya django-admin migrate`
	
-   Redix server'ı başlatın:
	`redis-server`

- 5.  Django development server'ı başlatın:
	`python manage.py runserver veya django-admin runserver`

### Nasıl Kullanabilirsiniz?
-	Projeyi çalıştırdıktan sonra tarayıcıyı açın ve [http://localhost:8000](http://localhost:8000/) adlı adrese gidin ve kayıtlı olan kullanıcılardan bir tanesine giriş yapın.
-	Giriş işlemini yaptıktan sonra kullanmaya başlayabilirsiniz.

# Proje Fotoğrafları
1. Giriş Sayfası
![Opera-Anlik-Goruntu_2024-03-14_143117_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143117_127.0.0.1.png)
2. Anasayfa 
![Opera-Anlik-Goruntu_2024-03-14_143141_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143141_127.0.0.1.png)
3. Sohbet sayfası iki kullanıcı arasında
![Opera-Anlik-Goruntu_2024-03-14_143152_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143152_127.0.0.1.png)
# EN
## WhatsApp Clone Chat Application
This project is developed using **Python** and **Javascript** technologies. The main purpose of the project is to gain experience working with web sockets.

### Project features:
1.  Redis server is used.
2.  User message history is saved to the database to allow users to view their message histories.
3.  Users can send each other media files such as **images** and **videos** and view them.
4.  Thanks to the infrastructure created for users who want to send voice recordings, users can send voice recordings to each other.

##  Installation

-   Clone the Project: `git clone https://github.com/BatuhanGurbuzz/DjangoChatApp.git`
    
-   Create a virtual environment and install dependencies (Optional): `python -m venv venv source venv/bin/activate` or `venv\Scripts\activate` for Windows `pip install -r requirements.txt`
    
-   Open a terminal, navigate to the directory where the file is located, and apply Django migrations: `python manage.py migrate` or `django-admin migrate`
    
-   Start the Redis server: `redis-server`
    
-   Start the Django development server: `python manage.py runserver` or `django-admin runserver`
    

## How to Use?

-   After running the project, open a browser and go to [http://localhost:8000](http://localhost:8000/), then log in with one of the registered users.
-   After logging in, you can start using it.

# Project Photos
 1. Login Page
![Opera-Anlik-Goruntu_2024-03-14_143117_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143117_127.0.0.1.png)

2. Home
![Opera-Anlik-Goruntu_2024-03-14_143141_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143141_127.0.0.1.png)
3. Chat Page
![Opera-Anlik-Goruntu_2024-03-14_143152_127.0.0.1.png](https://www.resimupload.org/images/2024/03/14/Opera-Anlik-Goruntu_2024-03-14_143152_127.0.0.1.png)
