from django.urls import path

from chat.views import index, room, start_chat

urlpatterns = [
    path("", index, name="index"),
    path('chat/<str:room_name>/', room, name = 'room'),
    path('chat/start_chat/<str:username>/', start_chat, name = 'start_chat')
    
]
