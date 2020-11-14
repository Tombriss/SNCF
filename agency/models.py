from django.db import models

# Create your models here.



class Reduction(models.Model):

    # création d'un menu déroulant, correctement réalisée ?
    NO_CARD = 'NC'
    JUNIOR_CARD = 'JC'
    SENIOR_CARD = 'SC'
    REDUCTION_CARD_CHOICES = [(NO_CARD, 'no reduction'), (JUNIOR_CARD, 'junior reduction'), (SENIOR_CARD, 'senior reduction')]
    reduction_card_type = models.CharField(max_length=2, choices=REDUCTION_CARD_CHOICES, default=NO_CARD)

    # il reste à définir la variable de pourcentage de la réduction, disons 30% pour les jeunes et 20% pour les seniors

    def __str__(self):
        return self.reduction_card_type



class Client(models.Model):

    prenom = models.CharField(max_length=200)
    nom = models.CharField(max_length=200)
    id_client = models.IntegerField()

    # création d'un menu déroulant, correctement réalisée ?
    NO_CARD = 'NC'
    JUNIOR_CARD = 'JC'
    SENIOR_CARD = 'SC'
    REDUCTION_CARD_CHOICES = [(NO_CARD, 'no reduction'), (JUNIOR_CARD, 'junior reduction'), (SENIOR_CARD, 'senior reduction')]
    reduction_card_type = models.CharField(max_length=2, choices=REDUCTION_CARD_CHOICES, default=NO_CARD)

    def __str__(self):
        return str(self.id_client)



class Reservation(models.Model):

    price_ticket = models.FloatField()
    place_number = models.IntegerField()
    id_reservation = models.IntegerField()

    # à définir avec la bonne syntaxe correspond à la relation souhaitée :
    # ForeignKey (FK) pour id_ride
    # ForeignKey (FK) pour id_voiture
    # ForeignKey (FK) pour id_client

    def __str__(self):
        return str(self.id_reservation)




class Car(models.Model):

    number_available_places_car = models.IntegerField()
    number_reserved_places_car = models.IntegerField()
    car_number = models.IntegerField()
    id_car = models.IntegerField()

    # FK pour train_number

    def __str__(self):
        return str(self.id_car)


class Train(models.Model):

    train_number = models.IntegerField()

    def __str__(self):
        return str(self.train_number)


class Ride(models.Model):

    id_ride = models.IntegerField()
    price_ride = models.FloatField()
    departure = models.DateTimeField()
    arrival = models.DateTimeField()

    # FK pour train_number
    # FK pour id_gare_départ
    # FK pour id_gare_arrivée

    def __str__(self):
        return str(self.id_ride)


class Station(models.Model):

    id_station = models.IntegerField()
    name_station = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

    def __str__(self):
        return str(self.id_station)


class Place(models.Model):

    id_place = models.IntegerField()
    number_available_places_train = models.IntegerField()

    # FK pour id_trajet

    def __str__(self):
        return str(self.id_place)