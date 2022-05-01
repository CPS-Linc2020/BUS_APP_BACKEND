from rest_framework import viewsets
from rest_framework.response import Response

from .models import BusStation
from .serializers import BusSerializer


class BusApiViewSet(viewsets.ViewSet):

    def list(self):
        queryset = BusStation.objects.all()
        serializer = BusSerializer(queryset, many=True)
        return Response(serializer.data)
