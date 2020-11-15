from django.urls import path

from . import views

urlpatterns = [

    # je ne sais pas si on doit laisser une procédure initiale... ?
    path('', views.index, name='index'),

    # page d'accueil permettant au client (nouveau ou pas) de s'identifier
    path('login/', views.login, name='login'),
    path('login/logger', views.logger, name='logger'),

    # # page d'accueil permettant au client (nouveau ou pas) de s'identifier
    # path('homepage/login/<str:name>', views.login, name='login'),

    # le client renseigne les infos concernant son trajet (incluant la réduction)
    path('ridesearch/', views.ridesearch, name='ridesearch'),

    # le client visualise et choisis les trajets dispo (avec ou sans la réduction de prix affichée?)
    path('homepage/ridesearch/availability/', views.availability, name='availability'),

    # le client confirme sa réservation
    path('homepage/ridesearch/availability/confirmation/', views.confirmation, name='confirmation'),

   # affichage du ticket acheté
   path('homepage/ridesearch/availability/confirmation/ticket/', views.ticket, name='ticket')

]