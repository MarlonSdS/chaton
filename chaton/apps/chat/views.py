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