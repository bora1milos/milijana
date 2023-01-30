from django.shortcuts import render
from django.http import HttpResponse


rooms = [
    {'id':1, 'name' : 'let learn python'},
    {'id':2, 'name' : 'design'},
    {'id':3, 'name' : 'front en developers'},
]

# Create your views here.
def home(request):
    return render(request, 'home.html')

def room(request):
    return render(request, 'room.html')