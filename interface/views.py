from .models import Position, Sensor, SoundSource
from rest_framework import viewsets
from .serializers import PositionSerializer, SensorSerializer, SoundSourceSerializer


class PositionViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SoundSourceViewSet(viewsets.ModelViewSet):
    queryset = SoundSource.objects.all()
    serializer_class = SoundSourceSerializer
