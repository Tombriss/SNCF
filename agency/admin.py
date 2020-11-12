from django.contrib import admin

# Register your models here.


# permet d'ajouter la table Ride au site admin
from .models import Ride
admin.site.register(Ride)