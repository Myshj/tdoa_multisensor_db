from .models import Position, Sensor, SoundSource, World
from rest_framework import serializers
from enumfields import EnumField


class PositionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Position
        fields = ('id', 'x', 'y', 'z')


class SensorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sensor
        fields = ('id', 'position', 'radius', 'heartbeat_interval', 'state', 'world')


class SoundSourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SoundSource
        fields = ('id', 'position', 'interval', 'state', 'world')


class WorldSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = World
        fields = ('id', 'name', 'speed_of_sound')
