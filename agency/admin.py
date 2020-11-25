from django.contrib import admin

# Register your models here.


# permet d'ajouter la table Ride au site admin
from .models import *

admin.site.register(Ride)
admin.site.register(Reduction)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(CarRide)
admin.site.register(Train)
admin.site.register(Station)