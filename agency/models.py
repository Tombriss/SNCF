from django.db import models
from datetime import date
from datetime import time
import numpy as np

# Create your models here.


class Reduction(models.Model):

    # création d'un menu déroulant, correctement réalisée ?
    NO_CARD = 'NC'
    JUNIOR_CARD = 'JC'
    SENIOR_CARD = 'SC'
    REDUCTION_CARD_CHOICES = [(NO_CARD, 'no reduction'), (JUNIOR_CARD, 'junior reduction'), (SENIOR_CARD, 'senior reduction')]
    card = models.CharField(max_length=2, choices=REDUCTION_CARD_CHOICES, default=NO_CARD,primary_key=True)

    # valeur de la réduction : 30% pour les jeunes et 20% pour les seniors
    NO_REDUCTION = 0
    JUNIOR_REDUCTION = 0.3
    SENIOR_REDUCTION = 0.2
    PERCENTAGES = [(NO_REDUCTION, '0%'), (JUNIOR_REDUCTION, '30%'), (SENIOR_REDUCTION, '20%')]
    percentage = models.FloatField(choices=PERCENTAGES, default=NO_REDUCTION)


    def __str__(self):
        return str(self.card)



class Client(models.Model):

    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    card = models.ForeignKey('Reduction', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.firstname +' '+self.lastname)


class Train(models.Model):

    def __str__(self):
        return str(self.id)




class Station(models.Model):

    name_station = models.CharField(max_length=200, primary_key=True)
    city = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name_station)



class CarRide(models.Model):

    number_available_places_car = models.IntegerField(default=0)
    total_places = models.IntegerField(default=50)
    car_number = models.IntegerField(default=0)

    # FK pour id_train
    id_ride = models.ForeignKey('Ride', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    class Meta:
        unique_together = (("id_ride", "car_number"),) 




class Ride(models.Model):

    price = models.FloatField(default=35.0)
    date = models.DateField(default=date.today)
    departure_time = models.TimeField(default=time)
    arrival_time = models.TimeField(default=time)
    departure_station =  models.ForeignKey('Station', related_name='departure_station',on_delete=models.CASCADE)
    arrival_station = models.ForeignKey('Station', related_name='arrival_station',on_delete=models.CASCADE)

    # FK pour id_train
    id_train = models.ForeignKey('Train', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)


class Reservation(models.Model):

    final_price = models.FloatField()
    
    place_situation = models.CharField(max_length=200,default=None)

    # vérifier que les foreign keys ont du sens :
    # ForeignKey (FK) pour id_ride
    # ForeignKey (FK) pour id_voiture
    # ForeignKey (FK) pour id_client

    id_car = models.ForeignKey('CarRide', on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    @classmethod
    def create(cls, *args,**kwargs):
        
        resa = cls(*args,**kwargs)
    
        
        if resa.final_price is None:
            resa.final_price = resa.id_car.id_ride.price * (1-resa.id_client.card.percentage)
        if resa.place_situation is None:
            # situation = 'fenêtre' if (resa.id % 2 == 0) else 'couloir'
            resa.place_situation = np.random.choice(['couloir','fenêtre'])

        # do something with the book
        return resa



