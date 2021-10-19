from django.db import models

# Create your models here.
class Station(models.Model) :
    station_id = models.IntegerField()
    bus_station_name = models.CharField(max_length=100)
    city_type = models.CharField(max_length=100)
    longitude = models.FloatField()
    latitude = models.FloatField()

    #수행 시 버스정류소 이름 출력.
    def __str__(self):
        return self.bus_station_name

class RoadNode(models.Model) :
    node_id = models.CharField(max_length=5000)
    node_name = models.CharField(max_length=500)
    rlatitude = models.FloatField()
    rlongitude = models.FloatField()
    
    def __str__(self):
        return self.node_name

class RoadLink(models.Model) :
    link_id = models.CharField(max_length=5000)
    start_node_id = models.CharField(max_length=5000)
    end_node_id = models.CharField(max_length=5000)
    road_name = models.CharField(max_length=5000)
    
    def __str__(self):
        return self.road_name

class BusRoute(models.Model) :
    num = models.IntegerField()
    bus_route_id = models.IntegerField()
    bus_route_number = models.CharField(max_length=100)
    bus_route_name = models.CharField(max_length=200)
    bus_station_count = models.IntegerField()
    bus_route_length = models.IntegerField()
    bus_transferability = models.CharField(max_length=100)
    
    def __str__(self):
        return self.bus_route_name

class StationUsing(models.Model) :
    base_date = models.CharField(max_length=5000)
    day_of_week = models.CharField(max_length=5000)
    base_hour = models.IntegerField()
    bus_station_id = models.IntegerField()
    bus_station_name = models.CharField(max_length=5000)
    get_on_off_type = models.CharField(max_length=300)
    user_count = models.IntegerField()

    def __str__(self):
        return self.bus_station_name
