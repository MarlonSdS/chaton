import json
from django.shortcuts import render
from .models import Message, Room
from django.views.generic.detail import DetailView
# Create your views here.
from django.http import HttpResponse


def index(request):
    rooms = Room.objects.all()
    return render(request, 'chat/index.html', {
        'rooms': rooms})

def root(request):
    return HttpResponse("Não há nada na raiz do servidor, tente colocar '/chat' no fim da url")

class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


def send_message(request, pk):
    data = json.loads(request.body)
    room = Room.objects.get(id=pk)
    #data = data['data']
    new_message = Message.objects.create(user=request.user, text=data['message'])
    room.messages.add(new_message)
    return render(request, 'chat/message.html', {
        'msg': new_message
    })