from django.db import models


class Station(models.Model):
    station_name = models.CharField(max_length=20_000)

    class Meta:
        db_table = 'station'


class Bus(models.Model):
    bus_name = models.CharField(max_length=10_000)
    bus_number = models.IntegerField()

    class Meta:
        db_table = 'bus'
