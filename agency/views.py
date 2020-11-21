from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import JsonResponse

from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.

from django.views.generic import CreateView
from .models import Client,Ride
from django.views.generic.base import TemplateView

from datetime import datetime


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


def search(request):

    # conditions sur le trajet souhaités 
    departure_station = request.POST.get('from')
    arrival_station = request.POST.get('to')
    departure_date = request.POST.get('date')

    # recuperation des trajets qui verifient cette condition dans la BDD 
    rides = Ride.objects.raw('''SELECT * FROM agency_ride 
                                WHERE departure_station = departure_station, arrival_station = arrival_station, departure_date = departure_date
                                    ''')

    # id du client                
    id_client = request.POST.get('id_client')

    # récupération de 
    card_type = Client.objects.raw('''SELECT * FROM agency_client
                                    WHERE first_name = request.session['firstname'], last_name = request.session['name']''').reduction_card_type # ne garde que le type de card, type str ex: 'JC' pour junior card

    percentage = Reduction.objects.raw('''SELECT * FROM agency_reduction
                                        WHERE reduction_card_type = card_type ''').reduction_percentage # [1] ne garde que le pourcentage, type float ex: 0.3



    # construction de la liste de dictionnaires des trajets
    data=[]
    for r in rides :
        d={}
        d['id_train'] = r.id_train.id_train
        d['departure_station'] = r.departure_station.name_station
        d['departure_date'] = r.departure_date.strftime("%Y-%m-%d")
        d['departure_time'] = r.departure_time.strftime('%H:%M')
        d['arrival_station'] = r.arrival_station.name_station
        d['arrival_date'] = r.arrival_date.strftime("%Y-%m-%d")
        d['arrival_time'] = r.arrival_time.strftime('%H:%M')
        d['price'] = r.price_ride * (1-percentage)
        data.append(d)
    

    return JsonResponse(data, safe=False)
    


    # to do :
    # gérer la putin de relation trajet/gares pour pouvoir appliquer la condition WHERE