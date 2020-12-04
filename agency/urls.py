from django.urls import path,re_path

from . import views

urlpatterns = [


    # page d'accueil permettant au client (nouveau ou pas) de s'identifier
    path('login/', views.login, name='login'),

    # pour connecter un utilisateur
    path('logger/', views.logger, name='logger'),

    # pour déconnecter un utilisateur
    path('logout/', views.logout, name='logout'),

    # pour get un paramètre de session
    re_path(r'^session/(?P<key>[^/]+)$', views.SessionVarView.as_view(), name='session-var'),

    # page pour chercher un trajet
    path('ridesearch/', views.ridesearch, name='ridesearch'),

    # page pour visualiser un trajet
    path('payement/<str:id_ride>', views.payement, name='payement'),

    # pour payer
    path('payement/confirmation/', views.confirmation, name='confirmation'),

    # pour chercher un trajet
    path('search/', views.search, name='search'),

    # pour peupler la bdd
    path('populate/',views.populate,name='populate')

]