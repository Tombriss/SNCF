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
    request.session['id_client'] = ''
    request.session['name'] = ''
    request.session['firstname'] = ''
    request.session['password'] = ''
    request.session['reduction'] = ''
    request.session['connected'] = False

    return HttpResponse('ok')

def login(request):

    return render(request, 'login.html')

def logger(request):
    
    request.session['id_client'] = request.POST.get('id_client','TB87382')
    request.session['name'] = request.POST.get('name','')
    request.session['firstname'] = request.POST.get('firstname','')
    request.session['password'] = request.POST.get('reduction','')
    request.session['password'] = request.POST.get('password','')
    request.session['connected'] = True

    # check here if client in bdd, else, create client

    return HttpResponse('ok')

def search(request):

    id_client = request.POST.get('id_client')
    from_station = request.POST.get('from')
    to_station = request.POST.get('to')
    date = request.POST.get('date')

    print(from_station,to_station,date,id_client)

    return(HttpResponse('ok'))


def payement(request,id_train='67855'):

    context = {}
    
    context["id_train"] = id_train
    context["from"] = "Paris"
    context["to"] = "Lyon"
    context["wday"] = "vendredi"
    context["day"] = "02"
    context["month"] = "décembre"
    context["short_month"] = context["month"][:3]
    context["year"] = "2020"
    context["time_departure"] = "08:00" 
    context["time_arrival"] = "10:00"
    context["available"] = True
    context["car"] = 6
    context["sit"] = 43

    context["price"] = 50
    context["reduction"] = 'Carte Jeune'
    context["final_price"] = 42

    return render(request, 'payement.html',context)

def confirmation(request):

    id_client = request.POST.get('id_client')
    id_train = request.POST.get('id_train')
    car = request.POST.get('car')
    sit = request.POST.get('sit')

    print(id_client,id_train,car,sit)
    
    return(HttpResponse('ok'))

def ticket(request):
    return render(request, 'ticket.html')

def ridesearch(request):
    return render(request, 'ridesearch.html')




