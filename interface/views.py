from .models import (Position, Sensor, SoundSource, World, Computer, NetworkAdapter, SoftwareState, IntBound,
                     IntInterval, NetworkConnection)
from rest_framework import viewsets
from .serializers import (PositionSerializer, SensorSerializer, SoundSourceSerializer, WorldSerializer, ComputerSerializer,
                          IntBoundSerializer, IntIntervalSerializer, NetworkAdapterSerializer,
                          NetworkConnectionSerializer, SoftwareStateSerializer)


class PositionViewSet(viewsets.ModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class SoundSourceViewSet(viewsets.ModelViewSet):
    queryset = SoundSource.objects.all()
    serializer_class = SoundSourceSerializer


class WorldViewSet(viewsets.ModelViewSet):
    queryset = World.objects.all()
    serializer_class = WorldSerializer


class ComputerViewSet(viewsets.ModelViewSet):
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer


class SoftwareStateViewSet(viewsets.ModelViewSet):
    queryset = SoftwareState.objects.all()
    serializer_class = SoftwareStateSerializer


class IntBoundViewSet(viewsets.ModelViewSet):
    queryset = IntBound.objects.all()
    serializer_class = IntBoundSerializer


class IntIntervalViewSet(viewsets.ModelViewSet):
    queryset = IntInterval.objects.all()
    serializer_class = IntIntervalSerializer


class NetworkAdapterViewSet(viewsets.ModelViewSet):
    queryset = NetworkAdapter.objects.all()
    serializer_class = NetworkAdapterSerializer


class NetworkConnectionViewSet(viewsets.ModelViewSet):
    queryset = NetworkConnection.objects.all()
    serializer_class = NetworkConnectionSerializer

# class WorldRelatedViewSet(viewsets.ModelViewSet):
#     queryset = WorldRelated.objects.all()
#     serializer_class = WorldRelatedSerializer
