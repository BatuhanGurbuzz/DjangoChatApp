from django.contrib import admin
from chat.models import Room, Message
# Register your models here.

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_user', 'second_user']
    
@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['user', 'room', 'created_date']
    readonly_fields = ['user', 'room', 'content', 'created_date']