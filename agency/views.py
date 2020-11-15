from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.

from django.views.generic import CreateView
from .models import Client


def index(request):
    logout(request)
    return redirect(ridesearch)

def login(request):
    return render(request, 'login.html')

def logger(request):

    print('laaaaa')
    return(None)

def availability(request):
    return render(request, 'availability.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def ticket(request):
    return render(request, 'ticket.html')

@login_required(login_url='/agency/login/')
def ridesearch(request):
    print(request)
    username = request.POST['username']
    password = request.POST['password']
    print(user,password)
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)

    return render(request, 'ridesearch.html')