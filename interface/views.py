from .models import Position, Sensor
from rest_framework import viewsets
from .serializers import PositionSerializer, SensorSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
