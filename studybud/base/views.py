from django.shortcuts import render, redirect
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

from .models import Room, Topic
from .forms import RoomForm


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
            password = User.objects.get(password=password)
        except:
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect('home')
        else:
             messages.error(request, 'User and password does not exist')

    contect = {}
    return render(request, 'base/login_register.html', contect)

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter( 
        Q(topic__name__icontains = q) |
        Q(name__icontains = q) |
        Q(description__icontains = q)
    )

    room_counts = rooms.count
    topics = Topic.objects.all()
    contex =  {'rooms': rooms, 'topics' : topics, 'room_counts' : room_counts }
    return render(request, 'base/home.html', contex)

def room(request, pk):
    room = Room.objects.get(id=pk)
    contex = { 'room' : room }
    return render(request, 'base/room.html', contex)

def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form' : form}
    return render(request, "base/room-form.html", context)

def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    contex = { 'form' : form }
    return render(request, "base/room-form.html", contex)

def deleteRoom(request, pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    
    contex = { 'obj' : room }
    return render(request, "base/delete.html", contex)



