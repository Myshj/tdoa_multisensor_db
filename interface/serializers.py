from rest_framework import serializers

from .models import (Position, Sensor, SoundSource, World, WorldRelated, NetworkAdapter, IntBound, Computer,
                     IntInterval, NetworkConnection)


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


class IntBoundSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntBound
        fields = ('id', 'value', 'bound_type')


class IntIntervalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IntInterval
        fields = ('id', 'lower_bound', 'upper_bound')


class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Computer
        fields = ('id', 'sensors', 'network_adapters', 'position', 'world', 'is_active_sensor_controller',
                  'is_active_tdoa_controller')


class NetworkConnectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = NetworkConnection
        fields = ('id', 'adapter_from', 'adapter_to', 'possible_latency')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'radius', 'heartbeat_interval', 'state', 'failure_probability', 'position', 'world')


class SoundSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoundSource
        fields = ('id', 'interval', 'state', 'position', 'world')


class WorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'speed_of_sound')
