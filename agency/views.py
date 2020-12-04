import numpy as np

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

    # view assez générale pour get un paramètre de session

    def get(self, request, *args, **kwargs):
        return HttpResponse(request.session.get(kwargs['key'],''))

def logout(request):

    # view pour logout l'utilisateur 

    request.session['id_client'] = ''
    request.session['name'] = ''
    request.session['firstname'] = ''
    request.session['password'] = ''
    request.session['reduction'] = ''
    request.session['connected'] = False

    return HttpResponse('ok')

def login(request):

    # view qui renvoie la page de login

    return render(request, 'login.html')

def logger(request):

    # view pour connecter/créer l'utilisateur

    lastname = request.POST.get('name','')
    firstname = request.POST.get('firstname','')
    password = request.POST.get('password','')
    reduction = request.POST.get('reduction','NC')
    
    REDS = {'No Card' : 'NC','Junior Card':'JC','Senior Card':'SC'}
    reduction = REDS.get(reduction,'')

    newclient = False 

    try:
        # On regarde si le client est dans la bdd
        client = Client.objects.get(firstname=firstname,lastname=lastname)
        print('client in database')
    except Client.DoesNotExist:
        client = None
        print('client not in database')

    if client is not None:

        # si oui, on check le mot de passe

        if client.password == password:
            print('good password')
            resp = 'Welcome back !' 
            if len(reduction)>0 and reduction != client.card.card:
                client.delete()
                client = Client(firstname=firstname,lastname=lastname,password=password,card=Reduction.objects.get(card=reduction))
                client.save()
        else:
            print('wrong password')
            return HttpResponse('wrong password !')
    
    else:

        # si non, on crée un nouvel utilisateur

        reduction = 'NC' if reduction == '' else reduction
        client = Client(firstname=firstname,lastname=lastname,password=password,card=Reduction.objects.get(card=reduction))
        client.save()
        resp = 'Welcome !'

    # on rentre les infos de l'utilisateurs 

    request.session['connected'] = True
    request.session['id_client'] = client.id
    request.session['name'] = client.lastname
    request.session['firstname'] = client.firstname
    request.session['reduction'] = str(client.card)
    request.session['password'] = client.password


    return HttpResponse(resp)

def payement(request,id_ride='67855'):

    # View pour visualiser le ticket et payer

    context = {}

    ride = Ride.objects.get(id=id_ride)
    client = Client.objects.get(id=request.session["id_client"])

    weekdays = ["Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi","Dimanche"]
    mois=['Janvier','Fevrier','Mars','Avril','Mai','Juin','Juillet','Août','Septembre','Octobre','Novembre','Décembre']

    context["id_train"] = id_ride
    context["from"] = ride.departure_station
    context["to"] = ride.arrival_station
    context["wday"] = weekdays[ride.date.weekday()]
    context["day"] = str(ride.date)[-2:]
    context["month"] = mois[ride.date.month-1]
    context["short_month"] = context["month"][:3]
    context["year"] = ride.date.year
    context["time_departure"] = ride.departure_time.strftime('%H:%M')
    context["time_arrival"] = ride.arrival_time.strftime('%H:%M')

    for car in CarRide.objects.filter(id_ride=ride.id):
        if car.number_available_places_car > 0:
            context["id_car"] = car.id
            context["car"] = car.car_number + 1
            context["sit"] = car.total_places - car.number_available_places_car + 1
            break

    context["sit_situation"] = np.random.choice(['couloir','fenêtre'])
    
    context["price"] = ride.price
    context["reduction"] = request.session.get('reduction','Pas de réduction')
    context["final_price"] = np.round(ride.price * (1-client.card.percentage),1)

    return render(request, 'payement.html',context)

def confirmation(request):

    # View pour confirmer le payement

    id_train = request.POST.get('id_train')
    id_car = request.POST.get('car')
    sit = request.POST.get('sit')
    sit_situation = request.POST.get('sit_situation')

    car = CarRide.objects.get(id=id_car)
    client = Client.objects.get(id=request.session["id_client"])

    try:
        resa = Reservation.create(place_situation=sit_situation,id_car=car,id_client=client)
        resa.save()
        resp = 'Travel Confirmed !'
    except:
        resp = 'An error occured, please return to menu'

    return(HttpResponse(resp))

def ridesearch(request):

    # view pour la recherche de trajet

    return render(request, 'ridesearch.html')


def search(request):

    # view pour get les trajets recherchés par l'utilisateur

    # conditions sur le trajet souhaités 
    departure_city = request.POST.get('from')
    arrival_city = request.POST.get('to')
    departure_date = request.POST.get('date')

    # recuperation des trajets qui verifient cette condition dans la BDD 

    # (utilisation des requêtes brutes SQL pour l'exemple, parfois impossible d'utiliser le raw sql avec django. ex: lorqu'on veut joindre deux tables notamment)
    dep_stations = Station.objects.raw('''SELECT * FROM agency_station WHERE (agency_station.city="{}") '''.format(departure_city))
    arr_stations = Station.objects.raw('''SELECT * FROM agency_station WHERE (agency_station.city="{}") '''.format(arrival_city))
    deps = [s.name_station for s in dep_stations]
    arrs = [s.name_station for s in arr_stations]

    rides = Ride.objects.filter(departure_station__in=deps,arrival_station__in=arrs,date=departure_date).order_by('departure_time')

    data=[]

    for r in rides :
        d={}

        available = False

        for car in CarRide.objects.filter(id_ride=r.id):
            if car.number_available_places_car > 0:
                available = True
                break

        d['id'] = r.id
        d['departure'] = r.departure_time.strftime('%H:%M')
        d['arrival'] = r.arrival_time.strftime('%H:%M')
        d['availability'] = 'AVAILABLE' if available else 'SOLD OUT'
        d['price'] = r.price
        data.append(d)

    # On renvoie les trains sous forme de json

    return JsonResponse(data, safe=False)

def populate(request):

    # view pour peupler aléatoirement la base de donnée

    randpopulate()

    return(HttpResponse('Population done'))
    