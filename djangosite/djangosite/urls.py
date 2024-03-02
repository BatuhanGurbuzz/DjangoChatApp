from django.contrib import admin
from django.urls import path, include
from chat.views import login

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('chat.urls')),
    path('giris-yap/', login, name = 'login')
]
