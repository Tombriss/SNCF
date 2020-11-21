from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404

from django.http import HttpResponse
from django.http import JsonResponse

from django.template import loader
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login,logout

# Create your views here.

from django.views.generic import CreateView
from .models import Client
from django.views.generic.base import TemplateView

from datetime import datetime


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

    # récupération des trajets correspondants à la requête du client
    request.session['departure_station'] = request.POST.get('departure_station','')
    request.session['arrival_station'] = request.POST.get('arrival_station','')
    request.session['departure_date'] = request.POST.get('departure_date','')

    rides = Ride.objects.raw('''SELECT * FROM agency_ride 
                                WHERE departure_station = request.session['departure_station'], arrival_station = request.session['arrival_station'], departure_date = request.session['departure_date']
                                    ''')




    # récupération du pourcentage de réduction à appliquer
    request.session['firstname'] = request.POST.get('firstname','')
    request.session['name'] = request.POST.get('name','')

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