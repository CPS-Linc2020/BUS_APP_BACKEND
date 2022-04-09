from django.db import models


class BusStation(models):
    city_types = {
        1: "시내",
        2: "시외"
    }
station_name = models.TextField(max_length=300)
    bus_city_type = models.IntegerField(choices=city_types)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)


class RoadNode(models):
    node_id = models.IntegerField()
    node_name = models.TextField(max_length=300)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)


class BusRoute(models):
    route_id = models.IntegerField()
    route_number = models.TextField(max_length=300)
    route_name = models.TextField(max_length=300)
    station_number = models.IntegerField()
    route_length = models.IntegerField()
    transferability = models.BooleanField(default=True)


class NodeLink(models):
    link_id = models.IntegerField()
    start_node_id = models.IntegerField()
    end_node_id = models.IntegerField()
    road_name = models.TextField(max_length=300, blank=True)
