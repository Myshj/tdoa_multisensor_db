from .models import (Position, Sensor, SoundSource, World, WorldRelated, NetworkAdapter, HasNetworkAdapter, IntBound,
                     IntInterval, NetworkConnection)
from rest_framework import serializers


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'x', 'y', 'z')


class WorldRelatedSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = WorldRelated
        fields = ('id', 'position', 'world')


class NetworkAdapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkAdapter
        fields = ('id', 'position', 'world')


class HasNetworkAdapterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = HasNetworkAdapter
        fields = ('id', 'network_adapter')


class IntBoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntBound
        fields = ('id', 'value', 'bound_type')


class IntIntervalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntInterval
        fields = ('id', 'lower_bound', 'upper_bound')


class NetworkConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkConnection
        fields = ('id', 'adapter_from', 'adapter_to', 'possible_latency')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'radius', 'heartbeat_interval', 'state', 'failure_probability', 'position', 'world', 'adapter')


class SoundSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoundSource
        fields = ('id', 'interval', 'state')


class WorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'speed_of_sound')
