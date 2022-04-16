from rest_framework import serializers


class BusSerializer(serializers.Serializer):
    station_name = serializers.CharField(max_length=300)
    bus_city_type = serializers.IntegerField()
    longitude = serializers.FloatField()
    latitude = serializers.FloatField()
