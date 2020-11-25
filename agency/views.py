from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import JsonResponse

from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.

from django.views.generic import CreateView
from .models import *
from django.views.generic.base import TemplateView

from datetime import datetime
from .random_populate import randpopulate


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

    lastname = request.POST.get('name','')
    firstname = request.POST.get('firstname','')
    password = request.POST.get('password','')
    reduction = request.POST.get('reduction','NC')

    # check here if client in bdd, else, create client

    newclient = False 

    try:
        client = Client.objects.get(firstname=firstname,lastname=lastname)
        print('client in database')
    except Client.DoesNotExist:
        client = None
        print('client not in database')

    if client is not None:

        if client.password == password:
            print('good password')
            resp = 'Welcome back !' 
        else:
            print('wrong password')
            return HttpResponse('wrong password !')
    
    else:
        client = Client(firstname=firstname,lastname=lastname,password=password,card=Reduction.objects.get(card=reduction))
        resp = 'Welcome !'
        # client.save()

    request.session['connected'] = True
    request.session['id_client'] = client.id
    request.session['name'] = client.lastname
    request.session['firstname'] = client.firstname
    request.session['reduction'] = str(client.card)
    request.session['password'] = client.password


    return HttpResponse(resp)

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
    departure_city = request.POST.get('from')
    arrival_city = request.POST.get('to')
    departure_date = request.POST.get('date')

    # recuperation des trajets qui verifient cette condition dans la BDD 
    dep_stations = Station.objects.raw('''SELECT * FROM agency_station WHERE (agency_station.city="{}") '''.format(departure_city))
    arr_stations = Station.objects.raw('''SELECT * FROM agency_station WHERE (agency_station.city="{}") '''.format(arrival_city))
    deps = [s.name_station for s in dep_stations]
    arrs = [s.name_station for s in arr_stations]

    rides = Ride.objects.filter(departure_station__in=deps,arrival_station__in=arrs,)


    # print(rides)

    # # id du client                
    # id_client = request.POST.get('id_client')

    # # récupération de 
    # card_type = Client.objects.raw('''SELECT * FROM agency_client
    #                                 WHERE first_name = request.session['firstname'], last_name = request.session['name']''').reduction_card_type # ne garde que le type de card, type str ex: 'JC' pour junior card

    # percentage = Reduction.objects.raw('''SELECT * FROM agency_reduction
    #                                     WHERE reduction_card_type = card_type ''').reduction_percentage # [1] ne garde que le pourcentage, type float ex: 0.3



    # construction de la liste de dictionnaires des trajets
    data=[]
    for r in rides :
        d={}
        d['id'] = r.id
        #d['departure_station'] = r.departure_station.name_station
        #d['arrival_station'] = r.arrival_station.name_station
        #d['date'] = r.date.strftime("%Y-%m-%d")
        d['departure'] = r.departure_time.strftime('%H:%M')
        d['arrival'] = r.arrival_time.strftime('%H:%M')
        d['price'] = r.price
        d['sits'] = 50
        data.append(d)

    return JsonResponse(data, safe=False)

def populate(request):

    randpopulate()

    return(HttpResponse('Population done'))
    


    # to do :
    # gérer la putin de relation trajet/gares pour pouvoir appliquer la condition WHERE