from django.shortcuts import render
from .models import Message, Room
# Create your views here.
from django.http import HttpResponse


def index(request):
    messages = Message.objects.all()
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {
        'messages':messages,
        'rooms': rooms})