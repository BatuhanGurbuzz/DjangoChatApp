from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.

# İhtiyaçlar 
## 1. Mesaj modeli, Oda modeli, ChatUser modeli,

class Room(models.Model):
    id = models.UUIDField(verbose_name = 'Oda ID', primary_key = True, default = uuid.uuid4) # Rastgele bir oda ID'si oluşturulacak
    first_user = models.ForeignKey(User, related_name = 'first_user', on_delete = models.CASCADE, verbose_name = 'İlk Kullanıcı', null=True)
    
    second_user = models.ForeignKey(User, related_name = 'second_user', on_delete = models.CASCADE, verbose_name = 'İkinci Kullanıcı',null=True)
    
    class Meta:
        verbose_name = 'Oda'
        verbose_name_plural = 'Odalar'
    
class Message(models.Model):
    user = models.ForeignKey(User, related_name = 'messages', on_delete = models.CASCADE, verbose_name = 'Kullanıcı')
    
    room = models.ForeignKey(Room, related_name = 'messages', on_delete = models.CASCADE, verbose_name = 'Oda')
    
    content = models.TextField(verbose_name = 'Mesaj İçeriği')
    
    created_date = models.DateTimeField(auto_now_add = True, verbose_name = 'Oluşturulma Tarihi')
    
    what_is_it = models.CharField(max_length = 50, null = True, verbose_name = 'Dosya')
    
    class Meta:
        verbose_name = 'Mesaj'
        verbose_name_plural = 'Mesajlar'
        
    def get_short_date(self):
        return str(self.created_date.hour) + ':' + str(self.created_date.minute)