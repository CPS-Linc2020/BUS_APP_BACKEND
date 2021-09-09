from django.shortcuts import render
from rest_framework.response import Response
from .models import Station
from rest_framework.views import APIView
from .serializers import StationSerializer

# Create your views here.

class StationListAPI(APIView) :
    def get(self, request):
        queryset = Station.objects.all()
        print(queryset)
        serializer = StationSerializer(queryset, many=True)
        return Response(serializer.data)