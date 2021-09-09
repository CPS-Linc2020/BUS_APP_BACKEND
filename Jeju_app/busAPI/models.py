from django.db import models

# Create your models here.
class Station(models.Model) :
    station_id = models.IntegerField()
    bus_station_name = models.CharField(max_length=100)
    city_type = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.bus_station_name