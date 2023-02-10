from typing import Set, Any

from django.shortcuts import render, redirect
from core_app.models import Event
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.


def login_user(req):
    return render(req, 'login.html')


def logout_user(req):
    logout(req)
    return redirect('/')


def submit_login(req):
    if req.POST:
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(req, user)
            return redirect('/')
        else:
            messages.error(req, 'Usuário ou senha inválido')
    return redirect('/')


@login_required(login_url='/login/')
def events_list(req):
    # Para 1 evento
    # event_item = Event.objects.get(id=1)
    # data = {'event': event_item}
    # return render(req, 'agenda.html', data)

    # Para todos eventos
    # events = Event.objects.all()
    # data = {'events': events}
    # return render(req, 'agenda.html', data)

    # Apenas do usuário logado sem resolver o erro de crash se deslogado
    user = req.user
    events = Event.objects.filter(user=user)
    data = {'events': events}
    return render(req, 'agenda.html', data)


# forma de criar um index usando o redirect em uma rota vazia
# def index(req):
    # return redirect('/agenda/')
