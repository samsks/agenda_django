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
    evnt = Event.objects.filter(user=user)
    data = {'events': evnt}
    return render(req, 'agenda.html', data)


# forma de criar um index usando o redirect em uma rota vazia
# def index(req):
    # return redirect('/agenda/')

@login_required(login_url='/login/')
def event(req):
    evnt_id = req.GET.get('id')
    data = dict()
    if evnt_id:
        data['event'] = Event.objects.get(id=evnt_id)
    return render(req, 'evento.html', data)


@login_required(login_url='/login/')
def submit_event(req):
    if req.POST:
        title = req.POST.get('title')
        event_date = req.POST.get('event_date')
        description = req.POST.get('description')
        user = req.user
        event_id = req.POST.get('event_id')
        if event_id:
            evnt = Event.objects.get(id=event_id)
            if evnt.user == user:
                evnt.title = title
                evnt.description = description
                evnt.event_date = event_date
                evnt.save()
            # Event.objects.filter(id=event_id).update(title=title, event_date=event_date, description=description)
        else:
            Event.objects.create(title=title, event_date=event_date, description=description, user=user)
    return redirect('/agenda/')


@login_required(login_url='/login/')
def delete_event(req, event_id):
    user = req.user
    evnt = Event.objects.get(id=event_id)
    if user == evnt.user:
        evnt.delete()
    return redirect('/agenda/')