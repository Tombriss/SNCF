from .models import Client,CarRide,Station,Ride,Train,Reduction,Reservation
import numpy as np
import datetime


def randpopulate():

    n_trains = 200
    n_rides = 100

    stations = {
        'Paris':['Paris Gare de Lyon'],
        'Lyon': ['Lyon Part Dieu','Lyon Perrache'],
        'Marseille':['Marseille-Saint-Charles','Marseille Blancarde']
    }

    reductions = [('NC',0),('JC',0.3),('SC',0.2)]

    Station.objects.all().delete()

    for ville,gares in stations.items():
        for gare in gares:
            obj = Station(name_station=gare,city=ville)
            obj.save()

    Train.objects.all().delete()

    for _ in range(n_trains):
        obj = Train()
        obj.save()

    Ride.objects.all().delete()

    for _ in range(n_rides):

        price = np.round(25+30*np.random.random(),2)

        t = datetime.datetime.now()+datetime.timedelta(np.random.randint(0,7))
        delta = datetime.timedelta(hours=2,minutes=15-np.random.randint(0,30))

        date = str(t.date())
        departure_time = str(t.time())[:5]
        arrival_time = str((t+delta).time())[:5]

        gares = np.random.choice(list(stations.keys()),size=(2,),replace=False)

        departure_station = Station.objects.get(name_station=np.random.choice(stations[gares[0]]))
        arrival_station =  Station.objects.get(name_station=np.random.choice(stations[gares[1]]))
        id_train = np.random.choice(Train.objects.all())

        obj = Ride(price=price,
        date=date,
        departure_time=departure_time,
        arrival_time=arrival_time,
        departure_station=departure_station,
        arrival_station=arrival_station,
        id_train=id_train)

        obj.save()


    for id_ride in range(1,n_rides):

        for car_number in range(8):

            nbre_available = np.random.randint(0,50)
            obj = CarRide(number_available_places_car=nbre_available,car_number=car_number,id_ride=Ride.objects.get(id=id_ride))
            obj.save()

    for card,percentage in reductions:

        obj = Reduction(card=card,percentage=percentage)
        obj.save()

    firstname = 'Thomas'
    lastname = 'Brisson'
    password = 'sncf'
    reduc = Reduction.objects.get(card='JC')
    n_reservation=2

    brisson = Client(firstname=firstname,lastname=lastname,password=password,card=reduc)
    brisson.save()

    for _ in range(n_reservation):

        id_car = np.random.choice(CarRide.objects.all())

        obj = Reservation.create(id_car=id_car,id_client=brisson)

        obj.save()


        






