from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from chat.models import Room, Message
from django.contrib.auth.decorators import login_required
def getContextData(request):
    users = User.objects.all().exclude(username = request.user)
    
    context = {
        'users': users
    }
    
    return context
@login_required(login_url="giris-yap/")
def index(request):
    return render(request, "chat/index.html", getContextData(request))

@login_required(login_url="/giris-yap")
def room(request, room_name):
    users = User.objects.all().exclude(username = request.user)
    room = Room.objects.get(id = room_name)
    messages =  Message.objects.filter(room = room).order_by('created_date')
    
    
    return render(request, 'chat/room_v2.html', {'room_name': room_name, 'users': users, 'room': room, 'messages':messages})

@login_required(login_url="/giris-yap")
def start_chat(request, username):
    second_user = User.objects.get(username = username)
    
    try:
        room = Room.objects.get(first_user = request.user, second_user = second_user)
    except Room.DoesNotExist:
        try:
            room = Room.objects.get(second_user = request.user, first_user = second_user)
        except Room.DoesNotExist: 
            room = Room.objects.create(first_user = request.user, second_user = second_user)
    return redirect('room', room.id)
    
    

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username = username, password = password)
        if user:
            auth_login(request, user)
            return redirect("index")
    return render(request, 'chat/login.html')
