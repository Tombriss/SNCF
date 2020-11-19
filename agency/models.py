from django.db import models

# Create your models here.


class Reduction(models.Model):

    # création d'un menu déroulant, correctement réalisée ?
    NO_CARD = 'NC'
    JUNIOR_CARD = 'JC'
    SENIOR_CARD = 'SC'
    REDUCTION_CARD_CHOICES = [(NO_CARD, 'no reduction'), (JUNIOR_CARD, 'junior reduction'), (SENIOR_CARD, 'senior reduction')]
    reduction_card_type = models.CharField(max_length=2, choices=REDUCTION_CARD_CHOICES, default=NO_CARD)

    # valeur de la réduction : 30% pour les jeunes et 20% pour les seniors
    NO_REDUCTION = 0
    JUNIOR_REDUCTION = 0.3
    SENIOR_REDUCTION = 0.2
    PERCENTAGES = [(NO_REDUCTION, '0%'), (JUNIOR_REDUCTION, '30%'), (SENIOR_REDUCTION, '20%')]
    reduction_percentage = models.FloatField(choices=PERCENTAGES, default=NO_REDUCTION)


    def __str__(self):
        return self.reduction_card_type



class Client(models.Model):

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    # création d'un menu déroulant, correctement réalisée ?
    NO_CARD = 'NC'
    JUNIOR_CARD = 'JC'
    SENIOR_CARD = 'SC'
    REDUCTION_CARD_CHOICES = [(NO_CARD, 'no reduction'), (JUNIOR_CARD, 'junior reduction'), (SENIOR_CARD, 'senior reduction')]
    reduction_card_type = models.CharField(max_length=2, choices=REDUCTION_CARD_CHOICES, default=NO_CARD)

    reduction_card_type = models.ForeignKey(Reduction, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.last_name)


class Train(models.Model):

    id_train = models.IntegerField()

    def __str__(self):
        return str(self.id_train)




class Station(models.Model):

    name_station = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name_station)



class Car(models.Model):

    number_available_places_car = models.IntegerField()
    number_reserved_places_car = models.IntegerField()
    car_number = models.IntegerField()
    id_car = models.IntegerField()

    # FK pour id_train
    id_train = models.ForeignKey('Train', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_car)




class Ride(models.Model):

    id_ride = models.CharField(max_length=200)
    price_ride = models.FloatField()
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()

    # FK pour id_train
    # FK pour id_gare_départ
    # FK pour id_gare_arrivée
    id_train = models.ForeignKey('Train', on_delete=models.CASCADE)
    departure_station = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='departure')
    arrival_station = models.ForeignKey('Station', on_delete=models.CASCADE, related_name='arrival')

    def __str__(self):
        return str(self.id_ride)


class Reservation(models.Model):

    price_ticket = models.FloatField()
    place_number = models.IntegerField()
    id_reservation = models.CharField(max_length=200)

    # vérifier que les foreign keys ont du sens :
    # ForeignKey (FK) pour id_ride
    # ForeignKey (FK) pour id_voiture
    # ForeignKey (FK) pour id_client

    id_ride = models.ForeignKey('Ride', on_delete=models.CASCADE)
    id_car = models.ForeignKey('Car', on_delete=models.CASCADE)
    id_client = models.ForeignKey('Client', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id_reservation)


class Place(models.Model):

    id_place = models.IntegerField()
    number_available_places_train = models.IntegerField()

    # FK pour id_trajet
    id_ride = models.ForeignKey('Ride', on_delete=models.CASCADE)


    def __str__(self):
        return str(self.id_place)

