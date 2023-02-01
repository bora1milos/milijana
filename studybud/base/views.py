from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm
rooms = [
    {'id':1, 'name' : 'let learn python'},
    {'id':2, 'name' : 'design'},
    {'id':3, 'name' : 'front en developers'},
]
# Create your views here.
def home(request):
    rooms = Room.objects.all()
    topics = Topic.objects.all()
    contex =  {'rooms': rooms, 'topics' : topics }
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



