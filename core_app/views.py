from typing import Set, Any

from django.shortcuts import render, redirect
from core_app.models import Event

# Create your views here.


def events_list(req):
    # Para 1 evento
    # event_item = Event.objects.get(id=1)
    # data = {'event': event_item}
    # return render(req, 'agenda.html', data)

    # Para todos eventos
    events = Event.objects.all()
    data = {'events': events}
    return render(req, 'agenda.html', data)

    # Apenas do usuário logado sem resolver o erro de crash se deslogado
    # user = req.user
    # events = Event.objects.filter(user=user)
    # data = {'events': events}
    # return render(req, 'agenda.html', data)


# forma de criar um index usando o redirect em uma rota vazia
# def index(req):
    # return redirect('/agenda/')
