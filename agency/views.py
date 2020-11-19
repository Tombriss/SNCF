from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.

from django.views.generic import CreateView
from .models import Client
from django.views.generic.base import TemplateView


class SessionVarView(TemplateView):
    def get(self, request, *args, **kwargs):
        return HttpResponse(request.session.get(kwargs['key'],''))

def logout(request):
    request.session['name'] = ''
    request.session['firstname'] = ''
    request.session['id'] = ''
    request.session['password'] = ''
    request.session['connected'] = False

    return HttpResponse('ok')

def login(request):

    return render(request, 'login.html')

def logger(request):
    
    request.session['name'] = request.POST.get('name','')
    request.session['firstname'] = request.POST.get('firstname','')
    request.session['id'] = request.POST.get('id','')
    request.session['connected'] = True

    print(request.session['firstname'])
    print(request.session['name'])
    
    print('logger',request.session)

    # check here if client in bdd, else, create client

    return HttpResponse('ok')




def availability(request):
    return render(request, 'availability.html')

def confirmation(request):
    return render(request, 'confirmation.html')

def ticket(request):
    return render(request, 'ticket.html')

def ridesearch(request):
    print('ridesearch')
    print('session : ',request.session.get('name'))
    # username = request.POST['username']
    # password = request.POST['password']
    # print(user,password)
    # user = authenticate(request, username=username, password=password)
    # if user is not None:
    #     login(request, user)


    return render(request, 'ridesearch.html')

def search(request):
    trains.filter()


