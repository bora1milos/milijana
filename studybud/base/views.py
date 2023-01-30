from django.shortcuts import render
from .models import Room

rooms = [
    {'id':1, 'name' : 'let learn python'},
    {'id':2, 'name' : 'design'},
    {'id':3, 'name' : 'front en developers'},
]
# Create your views here.
def home(request):
    rooms = Room.objects.all()
    contex =  {'rooms': rooms }
    return render(request, 'base/home.html', contex)

def room(request, pk):
    #rooms = Room.objects.all()
    print (rooms)
    room = None
    for i in rooms:
        print (pk,  i['id'])
        if int(pk) == i['id']:
            room = i
    

    contex = { 'room' : room }
    print (contex)
    return render(request, 'base/room.html', contex)
