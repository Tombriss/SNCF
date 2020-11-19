from django.urls import path,re_path

from . import views

urlpatterns = [

    # je ne sais pas si on doit laisser une procédure initiale... ?

    # page d'accueil permettant au client (nouveau ou pas) de s'identifier
    path('login/', views.login, name='login'),

    path('logger/', views.logger, name='logger'),

    path('logout/', views.logout, name='logout'),

    re_path(r'^session/(?P<key>[^/]+)$', views.SessionVarView.as_view(), name='session-var'),

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