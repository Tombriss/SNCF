from django.urls import path

from . import views

urlpatterns = [

    # je ne sais pas si on doit laisser une procédure initiale... ?
    path('', views.index, name='index'),

    # page d'accueil permettant de choisir si nouveau client ou client existant, et de consulter les réservations
    path('homepage/', views.homepage, name='homepage'),

    # le nouveau client renseigne ses informations
    # le nc fait une recherche de trajet
    # le nc visualise les trajets dispos
    # le nc choisis son trajet et son ticket apparait
    path('homepage/newclient/', views.newclient, name='newclient'),
    path('homepage/newclient/ridesearch/', views.nc_ridesearch, name='nc_ridesearch'),
    path('homepage/newclient/ridesearch/availablerides', views.nc_availablerides, name='nc_availablerides'),
    path('homepage/newclient/ridesearch/availablerides/ticket', views.nc_ticket, name='nc_ticket'),

    # le client existant entre son identifiant
    # le ec fait une recherche de trajet
    # le ec visualise les trajets dispo
    # le ec choisis son trajet et son ticket apparait
    path('homepage/existingclient/', views.existingclient, name='existingclient'),
    path('homepage/existingclient/ridesearch/', views.ec_ridesearch, name='ec_ridesearch'),
    path('homepage/existingclient/ridesearch/availablerides', views.ec_availablerides, name='ec_availablerides'),
    path('homepage/existingclient/ridesearch/availablerides/ticket', views.ec_ticket, name='ec_ticket'),

    # le client renseigne son identifiant
    # il accède alors à sa liste de réservation
    path('homepage/bookedrides/', views.bookedrides, name='bookedrides'),
    path('homepage/bookedrides/listofrides', views.listofrides, name='listofrides')

]