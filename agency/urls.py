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

    # le client confirme sa réservation
    path('payement/<str:id_ride>', views.payement, name='payement'),

    path('payement/confirmation/', views.confirmation, name='confirmation'),

    path('search/', views.search, name='search'),

    path('populate/',views.populate,name='populate')

]