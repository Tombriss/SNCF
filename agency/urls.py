from django.urls import path

from . import views

urlpatterns = [

    # je ne sais pas si on doit laisser une procédure initiale... ?
    path('', views.index, name='index'),

    # page d'accueil permettant de choisir si nouveau client ou client existant, et de consulter les réservations
    path('agency/homepage/', views.homepage, name='homepage'),

    # le nouveau client renseigne ses informations
    # le nc fait une recherche de trajet
    # le nc visualise les trajets dispos
    # le nc choisis son trajet et son ticket apparait
    path('agency/homepage/newclient/', views.newclient, name='newclient'),
    path('agency/homepage/newclient/ridesearch/', views.nc_ridesearch, name='nc_ridesearch'),
    path('agency/homepage/newclient/ridesearch/availablerides', views.nc_availablerides, name='nc_availablerides'),
    path('agency/homepage/newclient/ridesearch/availablerides/ticket', views.nc_ticket, name='nc_ticket'),

    # le client existant entre son identifiant
    # le ec fait une recherche de trajet
    # le ec visualise les trajets dispo
    # le ec choisis son trajet et son ticket apparait
    path('agency/homepage/existingclient/', views.existingclient, name='existingclient'),
    path('agency/homepage/existingclient/ridesearch/', views.ec_ridesearch, name='ec_ridesearch'),
    path('agency/homepage/existingclient/ridesearch/availablerides', views.ec_availablerides, name='ec_availablerides'),
    path('agency/homepage/existingclient/ridesearch/availablerides/ticket', views.ec_ticket, name='ec_ticket'),

    # le client renseigne son identifiant
    # il accède alors à sa liste de réservation
    path('agency/homepage/bookedrides/', views.bookedrides, name='bookedrides'),
    path('agency/homepage/bookedrides/listofrides', views.listofrides, name='listofrides')

]