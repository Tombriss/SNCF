from django.contrib import admin

# Register your models here.


# permet d'ajouter la table Ride au site admin
from .models import Ride, Reduction, Client, Reservation, Car, Train, Station, Place

admin.site.register(Ride)
admin.site.register(Reduction)
admin.site.register(Client)
admin.site.register(Reservation)
admin.site.register(Car)
admin.site.register(Train)
admin.site.register(Station)
admin.site.register(Place)
